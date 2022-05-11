import boto3
import os
import re
import time
import click
from tqdm import tqdm
import uuid

dx = boto3.client("dataexchange", region_name="us-east-1")
s3 = boto3.client("s3")


def get_all_revisions(data_set_id):

    revisions = []
    res = dx.list_data_set_revisions(DataSetId=data_set_id)
    next_token = res.get("NextToken")

    revisions += res.get("Revisions")
    while next_token:
        res = dx.list_data_set_revisions(DataSetId=data_set_id, NextToken=next_token)
        revisions += res.get("Revisions")
        next_token = res.get("NextToken")

    return revisions


def get_all_assets(data_set_id, revision_id):
    assets = []
    res = dx.list_revision_assets(DataSetId=data_set_id, RevisionId=revision_id)
    next_token = res.get("NextToken")

    assets += res.get("Assets")
    while next_token:
        res = dx.list_revision_assets(
            DataSetId=data_set_id, RevisionId=revision_id, NextToken=next_token
        )
        assets += res.get("Assets")
        next_token = res.get("NextToken")

    return assets


def export_revision(revision, bucket):
    # Do nothing if revision is revoked
    if revision.get("Revoked"): return

    revision_destinations = [{"RevisionId":revision.get("Id"), "Bucket":bucket, "KeyPattern":"${Asset.Name}"}]

    job = dx.create_job(
        Type="EXPORT_REVISIONS_TO_S3",
        Details={
            "ExportRevisionsToS3": {
                "DataSetId": revision.get("DataSetId"),
                "RevisionDestinations": revision_destinations,
            }
        },
    )

    job_id = job.get("Id")
    dx.start_job(JobId=job_id)

    # Wait until job is complete
    while True:
        job = dx.get_job(JobId=job_id)

        if job.get("State") == "COMPLETED":
            break
        elif job.get("State") == "ERROR":
            raise Exception(
                "Job {} failed to complete - {}".format(
                    job_id, job.get("Errors")[0].get("Message")
                )
            )
    time.sleep(0.25)


def to_url(s):
    s = re.sub(r"[^\w\s]", "", s)
    s = re.sub(r"\s+", "-", s)

    return s


def download_assets(assets, bucket, asset_dir):
    for asset in assets:
        asset_name = asset.get("Name")
        sub_dir = os.path.dirname(asset_name)
        full_dir = os.path.join(asset_dir, sub_dir)

        if not os.path.exists(full_dir):
            os.makedirs(full_dir)

        asset_file = os.path.join(full_dir, os.path.basename(asset_name))

        s3.download_file(bucket, asset_name, asset_file)

        print("Downloaded file {}".format(asset_file))


def make_s3_staging_bucket():
    bucket_name = "rearc_adx_exported_staging_" + str(uuid.uuid4())
    s3.create_bucket(Bucket=bucket_name)
    return bucket_name


def remove_s3_bucket(bucket_name):
    s3_resource = boto3.resource("s3")
    bucket = s3_resource.Bucket(bucket_name)
    bucket.objects.all().delete()
    bucket.delete()


@click.command()
@click.option("--s3-bucket", "-s", help="Destination S3 bucket.")
@click.option("--resume-at", "-r", help="Revision ID to resume at. Good for resuming stopped or crashed jobs.")
@click.option(
    "--download/--dont-download",
    default=False,
    help="Download all revision assets to local disk? (Defaults to False)",
)
@click.option(
    "--export/--dont-export",
    default=True,
    help="Export assets to S3 bucket? (Defaults to True)",
)
@click.argument("dataset-id")
def main(s3_bucket, resume_at, dataset_id, download, export):
    temp_bucket = None
    if s3_bucket is None:
        print("No s3 bucket provided, creating temporary staging bucket")
        temp_bucket = make_s3_staging_bucket()
        print("Created temporary bucket {}".format(temp_bucket))

    try:
        data_sets = [dx.get_data_set(DataSetId=dataset_id)]

        staging_bucket = s3_bucket or temp_bucket

        for ds in data_sets:
            print("Getting all assets for dataset: {}".format(ds.get("Name")))

            revisions = get_all_revisions(ds.get("Id"))
            progress_bar = tqdm(revisions)
            for rev in progress_bar:
                if resume_at is not None:
                    if rev.get("Id") != resume_at:
                        continue
                    else:
                        resume_at = None
                progress_bar.set_description("Exporting Revision: " + rev.get("Id"))
                if export:
                    export_revision(rev, staging_bucket)
                if download:
                    assets = get_all_assets(ds.get("Id"), rev.get("Id"))

                    destination_dir = os.path.join(to_url(ds.get("Name")), rev.get("Id"))
                    download_assets(assets, staging_bucket, destination_dir)

            print("---")
    finally:
        if temp_bucket:
            print("Removing temporary bucket {}".format(temp_bucket))
            remove_s3_bucket(temp_bucket)


if __name__ == "__main__":
    main()

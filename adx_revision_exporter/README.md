<a href="https://www.rearc.io/data/">
    <img src="./rearc_logo_rgb.png" alt="Rearc Logo" title="Rearc Logo" height="52" />
</a>

# ADX Revision Exporter

You can use the following code snippet to export any number of desired revisions from this dataset. There are two input avariables required for this:

1. The name of the S3 bucket that you would like the data to be exported to.
2. The dataset ID for this product which you can access from the AWS Data Exchange console after you subscribe to the product.

This tool requires Python 3.7+, and `click`, `tqdm`, and `boto3`.

### Example Usage
```
$ cd adx_revision_exporter
$ python adx_revision_exporter.py --s3-bucket <DESTINATION_BUCKET_NAME> <DATASET_ARN>
```

### Command Info

```
$ python adx_revision_exporter.py --help
Usage: adx_revision_exporter.py [OPTIONS] DATASET_ID

Options:
  -s, --s3-bucket TEXT          Destination S3 bucket (if both --download and --dont-export flags are
                                enabled, this is used as a temporary staging bucket).
  -r, --resume-at TEXT          Revision ID to resume at. Good for resuming
                                stopped or crashed jobs.
  --download / --dont-download  Download all revision assets to local disk?
                                (Defaults to False)
  --export / --dont-export      Export assets to S3 bucket? (Defaults to True)
  --help                        Show this message and exit.
```

Please keep in mind that the `--download` flag will first export files to S3, then download them to your local disk. If the `--download` and `--dont-export` flags are used together, the script will use S3 as a temporary staging area, exporting each revision to S3, downloading from S3 to disk, and then removing the revision files from S3. 

### Contact Details
- If you find any issues with or have enhancement ideas for this product, open up a GitHub issue and we will gladly take a look at it. Better yet, submit a pull request. Any contributions you make are greatly appreciated :heart:.
- If you have any questions or feedback, send us an email at data@rearc.io.

### About Rearc
Rearc is a cloud, software and services company. We believe that empowering engineers drives innovation. Cloud-native architectures, modern software and data practices, and the ability to safely experiment can enable engineers to realize their full potential. We have partnered with several enterprises and startups to help them achieve agility. Our approach is simple — empower engineers with the best tools possible to make an impact within their industry.
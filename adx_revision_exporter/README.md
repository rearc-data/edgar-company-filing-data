<a href="https://www.rearc.io/data/">
    <img src="./rearc_logo_rgb.png" alt="Rearc Logo" title="Rearc Logo" height="52" />
</a>
# ADX Revision Exporter

You can use the following code snippet to export any number of desired revisions from this dataset. There are two input avariables required for this:

1. The name of the S3 bucket that you would like the data to be exported to.
2. The dataset ARN for this product which you can access from the AWS Data Exchange console after you subscribe to the produc.

### Example usage
```
$ cd adx_revision_exporter
$ python adx_revision_exporter.py --s3-bucket <DESTINATION_BUCKET_NAME> <DATASET_ARN>
```

Requires Python 3.7+ and `boto3`.

### Contact Details
- If you find any issues with or have enhancement ideas for this product, open up a GitHub issue and we will gladly take a look at it. Better yet, submit a pull request. Any contributions you make are greatly appreciated :heart:.
- If you have any questions or feedback, send us an email at data@rearc.io.

### About Rearc
Rearc is a cloud, software and services company. We believe that empowering engineers drives innovation. Cloud-native architectures, modern software and data practices, and the ability to safely experiment can enable engineers to realize their full potential. We have partnered with several enterprises and startups to help them achieve agility. Our approach is simple — empower engineers with the best tools possible to make an impact within their industry.
import argparse
import boto3

class S3Read:
    def __init__(self, parser):
        self.aws_seceret_key = parser.parse_args().secretkey
        self.aws_access_key = parser.parse_args().accesskey
        session = boto3.Session(
            aws_access_key_id=self.aws_access_key,
            aws_secret_access_key=self.aws_seceret_key,
        )
        self.s3 = session.resource('s3')

    def listOfObject(self):
        bucket = self.s3.Bucket('scoredata-data-warehouse')
        for obj in bucket.objects.all():
            print(obj.key, obj.last_modified)



if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-accesskey', action='store',
                        dest='accesskey',
                        help='AWS access key')
    parser.add_argument('-secretkey', action='store',
                        dest='secretkey',
                        help='AWS secret key')

    s3Read = S3Read(parser)
    s3Read.listOfObject()




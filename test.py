import boto3

s3 = boto3.resource(
    service_name='s3',
    aws_access_key_id='AKIARHRJOYUUVWCOKSPF',
    aws_secret_access_key='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'
)

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

for obj in s3.bucket.getall_keys():
    print(key['key'])



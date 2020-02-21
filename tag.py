import boto3
import sys

ec2 = boto3.client('ec2')


instances = ec2.describe_instances()

ids = ['instance id]


print ("Changing tags for %d instances" % len(ids))

ec2.create_tags(
    Resources=ids,
    Tags=[
        {
            'Key': 'Name',
            'Value': 'Value'
        }
    ]
)
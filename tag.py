import boto3
import sys

ec2 = boto3.client('ec2')


instances = ec2.describe_instances()
#Write the particular instance id which was generated at the time of creation in next line.
ids = ['instance id]


print ("Changing tags for %d instances" % len(ids))

ec2.create_tags(
    Resources=ids,
    Tags=[
        {
            'Key': 'Name',                 #Give the particular key and value which you  want to give your instance.
            'Value': 'Value'
        }
    ]
)                                         #Tag is updated in the instance.

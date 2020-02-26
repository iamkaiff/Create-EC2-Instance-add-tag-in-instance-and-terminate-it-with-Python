import boto3
client=boto3.client('ec2')
#You can choose your particular ami and size according to your need and paste it ami id and size below in the code. 
resp=client.run_instances(ImageId='ami-0d9462a653c34dab7',              
				InstanceType='t2.micro',
				MinCount=1,
				MaxCount=1)
for instance in resp['Instances']:
	print(instance['InstanceId'])
#After this your instance will be shown here with its respective id.
#Your instance is created.

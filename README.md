# Create-EC2-Instance-add-tag-in-instance-and-terminate-it-with-Python

Phase-1: Creation of an EC2 instance.

In this project we will learn how to create an EC2 instance in AWS using Python Boto3. 
Before we proceed further for the creation of an EC2 instance ,firstly we should learn that what is an AWS and EC2?
AWS stands for Amazon Web Services which is worldwide famous for providing their secure cloud computing services.Its not only provide the cloud services but they also provide database storage,compute power etc. and can perform different functionalities according to the need.This will help to transform many business to grow them up in the market.It can be managed by many databases like MySQL,Oracle,PostgreSQL.

EC2 stands for Elastic Compute Cloud it is a secure web service provided by AWS which mainly has some key features like it is resizeable in the cloud you can resize it according to your need several times.It has very user friendly interface,easy to learn,easy to understand for the developers.

That was the concise description of AWS and EC2 now we can proceed to our aim which was create EC2 instance in AWS by Python Boto3.

•	Step-1 
To create an EC2 instance the most basic requirement is that you must have a AWS account.
The second most basic requirement is that Python must be installed on your PC. 

•	Step-2
After getting all things done you need to create a IAM user in your AWS account.
To create IAM user just search IAM on your AWS account and then click on Add User Button.

Then give  a suitable name to the user and then give the access for EC2 to the user. 
Then give the suitable KeyName to it and then click on Create User.And then download the .csv file which has Access ID and Secret Access Key of the IAM User.

•	Step-3
Now after this install Boto3 on your by giving this command on your cmd.

#pip install boto3

•	Step-4
Now install awscli on your pc by giving this command on cmd.

#pip install awscli

•	Step-5
Now you need to configure your IAM  user details in your pc by giving this command on your cmd and write all details provided by .csv files in it.

#aws configure 

•	Step-6
When all the above things get done completely then the most important part of our project is come which is creation of an EC2 instance.

To create an EC2 instance first you need to decide which particular instance you want to create which you can choose in EC2 option in AWS Console. 

After choosing the particular AMI just copy the ami. Now you are ready to make a EC2 instance.Now write this piece of code in pyhton.

#gitpull create.py file


After executing this code you can check simply in your AWS account that an EC2 instance will be created.


Phase-2:  Add Tag in EC2 Instance.

To give a tag in EC2 instance you need to write this piece of code in python.

#gitpull tag.py file


Now you can check simply on your EC2 section that a tag is created.


Phase-3: Termination of an EC2 Instance.


Now here we are in our final phase of the project the termination of an EC2 instance.To terminate the instance just simply follow the below code.

#gitpull terminate.py file



After executing the above program accurately then the instance will be terminated.


Now we have completed our aim and have performed each and every step with Python Boto3 in  AWS.


So that,s all for now.These were the all necessary steps and programming for create,add tag and terminate the ec2 instance. 


          

  



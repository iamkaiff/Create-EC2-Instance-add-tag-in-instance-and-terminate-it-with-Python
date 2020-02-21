import boto.ec2
import sys
auth = {"aws_access_key_id": "id", "aws_secret_access_key": "access key"}
def main():
	if(len(sys.argv) < 2):
		print ("Usage: starst.py {start|terminate}\n")
		sys.exit(0)
	else:
		action = sys.argv[1] 
	if(action == "start"):
		startInstance()
	elif(action == "terminate"):
		terminateInstance()
	else:
		print("Usage: starst.py {start|terminate}\n")
def startInstance():
    print ("Starting the instance...")
    try:
        ec2 = boto.ec2.connect_to_region("ap-south-1", **auth)
    except Exception as e1:
        error1 = "Error1: %s" % str(e1)
        print(error1)
        sys.exit(0)
    try:
         ec2.start_instances(instance_ids="instance id")
    except Exception as e2:
        error2 = "Error2: %s" % str(e2)
        print(error2)
        sys.exit(0)
def terminateInstance():
    print("Terminating the instance...")
    try:
        ec2 = boto.ec2.connect_to_region("ap-south-1", **auth)
    except Exception as e1:
        error1 = "Error1: %s" % str(e1)
        print(error1)
        sys.exit(0)
    try:
         ec2.terminate_instances(instance_ids="instance id")
    except Exception as e2:
        error2 = "Error2: %s" % str(e2)
        print(error2)
        sys.exit(0)
if (__name__ == '__main__'):
    main()

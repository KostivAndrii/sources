# AWS Bash

This is very simple bash script to deploy an EC2 instance in AWS.

## What does this script do?

One the script is executed, it will perform the following:

-Create a new AWS key named “devenv-key” and store the corresponding key in your local machine.

-Deploy an t2.micro ubuntu EC2 instance.
-Upon deployment, it will wait for 60 seconds and SSH into the newly deployed ubuntu ec2 instance.

### Prerequisites:

-An Amazon AWS account.(Free or Paid account).

-An IAM user with Access Key and secret access key.

–Pre-configured VPC, Subnets, Routes, Internet gateways, Security policy.

-Any Linux Machine with aws cli utlity installed.

-You could Refer to blog post on how to install AWS CLI tool.
* [Tech Antidote](https://techantidote.com/how-to-install-aws-cli-in-linux-auto-command-completion/) - How to install aws cli tool and setup auto completion


– Host machine must have IAM user details added. You can run “aws configure” to configure the same.

### Variable used in the script:

-I have created different variable such as:
```
“vpc_id”            => VPC ID
“sub_id”            => Subnet ID
“route_table”       => Route Table [For Future use]
“internet_gateway”  => Internet Gateway
“sec_id”            => Security Group
“aws_image_id”      => Aws Image ID that you would like to deploy
“i_type”            => Instance type for example "t2.micro"
```
You can substitute these values in the script with that of your environment.

### How do I run this script?
```
git clone https://gitlab.com/techantidote/aws-bash.git
cd aws-bash
```
-Edit the file "getaws.sh" and provide values for variables mentioned above.

-Save the file and exit.

-To execute script, run the following:
```
./getaws.sh
```
More information: [Tech Antidote](https://techantidote.com/how-to-install-aws-cli-in-linux-auto-command-completion/) 

### Contact Information

-Would you like to contribute to this project? Or if you have any feedback, you can reach out to me in twitter.

https://twitter.com/techantidote



#### Disclaimer:
-This script has been tested on Linux Mint 18.3. 

-The intention of this script was to deploy ec2 instances quickly + learn about AWS CLI.

### Future Plans

-Clean up the code. (Like a lot. lol)

-Add functions.

-Add options to create VPC, Subnets, Internet Gateways and Security Policy

-Hopefully in the future, I will clea create functions to create and control which VPC/Subnet/IG/Security policy that an EC2 instance needs to be attached on the fly.

-[PS: I am not expert in Scripting. I am just someone trying to learn about AWS CLI + basic scripting.]


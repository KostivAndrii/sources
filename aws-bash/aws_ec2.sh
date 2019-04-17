#!/bin/bash

aws_image_id="ami-0dd7e7ed60da8fb83"
i_type="t2.micro"
aws_key_name="aws-test-key"
ssh_key="aws-test-key.pem"
sec_name=JenkinsSG
sec_desc="Jenkins SG"

aws ec2 create-key-pair --key-name $aws_key_name --query 'KeyMaterial' --output text 2>&1 | tee $ssh_key
echo "Setting permissions for ssh key $ssh_key"
chmod 400 $ssh_key

echo "Creating sec group $sec_name"
ec2_sg=$(aws ec2 create-security-group --group-name $sec_name --description "$sec_desc")

echo $ec2_sg > ec2_sg.txt
sec_ids=$(echo $ec2_sg | cut -d":" -f2 | cut -d'"' -f2)
echo 'sec group ids ' $sec_ids

echo "add 22 rule"
aws ec2 authorize-security-group-ingress --group-name $sec_name --protocol tcp --port 22 --cidr 0.0.0.0/0

echo "Creating instance ..."
ec2_id=$(aws ec2 run-instances --image-id $aws_image_id --count 1 --instance-type $i_type --key-name $aws_key_name --security-group-ids "$sec_ids" --associate-public-ip-address)
echo  $ec2_id > ec2_id.txt

inst_ids=$(echo $ec2_id | sed -n 's/.*InstanceId": "\(.*\)", "ImageId.*/\1/p')
echo 'InstanceId: '$inst_ids

echo "Obtaining instance description ..."
ec2_IP=$(aws ec2 describe-instances --instance-ids $inst_ids | grep PublicIpAddress | cut -d\" -f4)
echo 'PublicIpAddress: '$ec2_IP

countdown_timer=120
temp_cnt=${countdown_timer}
while [[ ${temp_cnt} -gt 0 ]];
do
    printf "\rYou have %2d second(s) remaining to hit Ctrl+C to cancel that operation!" ${temp_cnt}
    sleep 1
    ((temp_cnt--))
done
echo ""

ssh -o "StrictHostKeyChecking no" -i $ssh_key ec2-user@$ec2_IP

echo ""

#! /bin/bash -x

# the name of the bucket you will be put your cloudformation templates
# it has to be created first
bucket=uno-week9-cf
stack_name=week9
sshKeyPair=HaoyuSSH

# the role arn for cloudformation to create stack
# for this stack, it has to have access to S3, VPC, EC2
role_arn=arn:aws:iam::590183815216:role/CloudFormation_Role

# template url for the root template
template_url=https://${bucket}.s3.amazonaws.com/root9.yml

aws s3 sync ./cf s3://${bucket}

aws cloudformation describe-stacks --stack-name ${stack_name} --region us-east-1 &>/dev/null
exist=$?

if test $exist = 0
then
  echo "update stack"
  aws cloudformation update-stack \
    --stack-name ${stack_name} \
    --template-url  ${template_url}\
    --region us-east-1\
    --role-arn ${role_arn} \
    --parameters ParameterKey=SSHKeyPair,ParameterValue=${sshKeyPair} \
                ParameterKey=TemplatePath,ParameterValue=${bucket}
else
  echo "create stack"
  aws cloudformation create-stack \
    --stack-name ${stack_name} \
    --template-url  ${template_url}\
    --region us-east-1 \
    --role-arn ${role_arn} \
    --parameters ParameterKey=SSHKeyPair,ParameterValue=${sshKeyPair} \
                 ParameterKey=TemplatePath,ParameterValue=${bucket}
fi

sleep 60
status="UPDATE_IN_PROGRESS"
while [[ ${status} == *"PROGRESS"* ]]
do
   sleep 10
   status=$(aws cloudformation describe-stacks --stack-name ${stack_name} --region us-east-1 | jq '.Stacks[0].StackStatus')
done
echo "${status}"
outputs=$(aws cloudformation describe-stacks --stack-name ${stack_name} --region us-east-1 | jq '.Stacks[0].Outputs')
echo "${outputs}"

ip=$(echo "${outputs}" | jq '.[0].OutputValue' | tr -d '"')
echo "${ip}"

if [ -z ${PRIVATE_KEY} ]
then
  ssh -o StrictHostKeyChecking=no -i "~/.ssh/HaoyuSSH.pem" "ec2-user@${ip}" 'cd /home/ec2-user/cloud-computing/nodejs;bash update.sh' | cat
else
  echo "$PRIVATE_KEY" > private_key && chmod 600 private_key
  ssh -o StrictHostKeyChecking=no -i private_key "ec2-user@${ip}" 'cd /home/ec2-user/cloud-computing/nodejs;bash update.sh' | cat
fi
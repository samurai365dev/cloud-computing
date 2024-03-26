stack_name=week9
outputs=$(aws cloudformation describe-stacks --stack-name ${stack_name} --region us-east-1 | jq '.Stacks[0].Outputs')

ip=$(echo "${outputs}" | jq '.[0].OutputValue' | tr -d '"')
echo "${ip}"
echo "${PRIVATE_KEY}"
if [[ -z "${PRIVATE_KEY}" ]]
then
  ssh -o StrictHostKeyChecking=no -i "~/.ssh/HaoyuSSH.pem" "ec2-user@${ip}" \
  'cd /home/ec2-user/cloud-computing/nodejs;git config --global --add safe.directory /home/ec2-user/cloud-computing;\
    sudo git checkout deploy; sudo bash update.sh' | cat
else
  echo "$PRIVATE_KEY" > private_key && chmod 600 private_key
  ssh -o StrictHostKeyChecking=no -i private_key "ec2-user@${ip}" \
    'cd /home/ec2-user/cloud-computing/nodejs; sudo bash update.sh' | cat
fi
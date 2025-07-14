export PRIVATE_IP_DB=$(aws ec2 describe-instances \
  --filters "Name=tag:Name,Values=Database" \
  --query "Reservations[*].Instances[*].PrivateIpAddress" \
  --output text)

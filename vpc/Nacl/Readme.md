## Craete NACL

```sh
aws ec2 create-network-acl --vpc-id vpc-084687a7bc466b414
```

## Add entry

```sh
aws ec2 create-network-acl-entry \
--network-acl-id acl-025c3195b6e289d4e \
--ingress \
--rule-number 90 \
--protocol -1 \
--port-range From=0, To=65535 \
--cidr-block 174.6.110.2/32 \
--rule-action deny
```

## get AMI for Amazon Linux 2

Grab the latest AML2 AMI
```sh
aws ec2 describe-images \
--owners amazon \
--filters "Name=name,Values=amzn2-ami-hvm-*-x86_64-gp2" "Name=state,Values=available" \
--query "Images[?starts_with(Name, 'amzn2')]|sort_by(@, &CreationDate)[-1].ImageId" \
--region ap-south-1
--output text
```
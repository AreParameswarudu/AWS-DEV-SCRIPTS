# For EC2   
[https://docs.aws.amazon.com/cli/latest/reference/ec2/](https://docs.aws.amazon.com/cli/latest/reference/ec2/)

```
aws ec2 run-instances --image-id ami-0402awse56c0a7afb78f --count 1 --instance-type t2.micro --key-name 4PMBATCH --security-group-ids sg-deb102b3 --subnet-id subnet-a6c089ce
```

```
aws ec2 stop-instances --instance-ids  i-0ebef50d9dbde0316
```

```
aws ec2 start-instances --instance-ids i-0ebef50d9dbde0316
```

```
aws ec2 describe-instances --instance-ids i-0ebef50d9dbde0316
```

describes the instance ( like instance type, id, key-pair, img-id,snap-id, launch-time, etc )

```
aws ec2 describe-instance-status --instance-ids i-0ebef50d9dbde0316
```
	
describes the status of the instance,  By default, only running instances are described, unless you specifically indicate to return the status of all instances. 

```
aws ec2 terminate-instances --instance-ids i-02409bfc8eeda1309
```

```
aws ec2 create-tags --resources  i-06d36004702700c3b  --tags Key=Name,Value=CLIDEMOnew
```

```
aws ec2 describe-volumes 
```

```
aws ec2 create-volume --size 10 --region ap-south-1 --availability-zone ap-south-1a --volume-type gp2
```

```
aws ec2 attach-volume  --volume-id vol-029092e045892da89 --instance-id  i-0b723bc87d5354dc2 --device /dev/sdh
```

```
aws ec2 detach-volume --volume-id vol-08e80264fc1ee947c
```

```
aws ec2 delete-volume --volume-id vol-08e80264fc1ee947c
```

```
aws ec2 describe-key-pairs
```

```
aws ec2 terminate-instances --instance-ids i-1234567890abcdef0
```

```
aws ec2 create-image --instance-id  i-0a76a216a9e73da33 --name "Dev AMI" --description "AMI for development server"
```

```
aws ec2 deregister-image --image-id ami-07c5e02e2031a3501
```

```
aws ec2 delete-snapshot --snapshot-id snap-0773147d6aab55ffe
```

```
curl http://169.254.169.254/latest/meta-data/
```

# S3 commands


[https://docs.aws.amazon.com/cli/latest/reference/s3/sync.html](https://docs.aws.amazon.com/cli/latest/reference/s3/sync.html)

```
aws s3 mb s3://mybucket
```

```
aws s3 mb s3://mybucket --region us-west-1
```

```
aws s3 mv test.txt s3://mybucket/test2.txt
```

```
aws s3 mv s3://mybucket/test.txt s3://mybucket2/test2.txt
```

```
aws s3 mv s3://mybucket/test.txt test2.txt
```


```
aws s3 mv s3://mybucket/test.txt s3://mybucket2/ (retain orginal name)
```

```
aws s3 mv s3://mybucket/ . --recursive
```

```
aws s3 mv myDir s3://mybucket/ --recursive --exclude "*.jpg"
```

```
aws s3 mv s3://mybucket/ s3://mybucket2/ --recursive --exclude "mybucket/another/*"
```
clear
  
```
aws s3 ls
```

```
aws s3 ls s3://mybucket
```

```
aws s3 ls s3://mybucket --recursive
```

```
aws s3 ls s3://mybucket--recursive --human-readable --summarize
```



Copying a local file to S3  
```
aws s3 cp test.txt s3://mybucket/test2.txt
```

Copying an S3 object to a local file  
```
aws s3 cp s3://myreya/text.txt text.txt
```

Copying an S3 object from one bucket to another  
```
aws s3 cp s3://mybucket/test.txt s3://mybucket2/
```

Recursively copying S3 objects to a local directory  
```
aws s3 cp s3://mybucket . --recursive
```

Recursively copying local files to S3  
```
aws s3 cp myDir s3://myreya/ --recursive --exclude "*.jpg"
```

Remove buckets

```
aws s3 rb s3://mybucket
```
```
aws s3 rb s3://mybucket --force
```

create two buckets and keep some files in bucket1 

```
aws s3 sync s3://mybucket1 s3://mybucket2
```

```
aws s3 sync . s3://mybucket
```
```
aws s3 sync s3://mybucket .
```
delete additional file in s3 if that is not in local.

```
aws s3 sync . s3://mybucket --delete
```
```
aws s3 website s3://my-bucket/ --index-document index.html --error-document error.html
```

provider "aws" {

    region = "ap-south-1"
}

resources "aws_instance" "my-instances" {

    instance_type = "t2.micro"
    ami = "ami-283ync349ry"
    
}

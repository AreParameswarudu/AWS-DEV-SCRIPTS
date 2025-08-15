# Terraform 
Terraform is an open-source **Infrastructure as Code** tool developed by HashiCorp.  
Terraform is cloud agnostic.  
It allows us to define and provision infrastructure resources in a cosistent, repeatable manner using a high-level configuration language known as **HasiCorp Configuration Language (HCL)**.  

It was developed in GO language.  


**Alternatives of Terraform:**
  1. OpenTufu
  2. PULUMIN
  3. Ansible (mainly for configuration not directly for infra provisioning).
  4. CHEF


Structure of Terraform:
Mostly defined using 3 major files, 
  1. **main.tf** - Contains all providers, resources and data resources.
  2. **variable.tf** - Contains all defined variables.
  3. **output.tf** - Contains all outputs resources.

  
Terraform, however, does not mandate this structure, it only requires a directory of Terraform files.  
Filenames do not matter to Terraform. To make it simple we prefer the following structure,   

```
projectname/
  |
  |-provider.tf - Plugins to connect to cloud.
  |-version.tf - Sets required Terraform and provider versions.
  |-backemd.tf - This file is used to configure the backend, which determines how and where Terraform stores its data.
  |-main.tf - Contains the cor resources definations.
  |-variable.tf - Declare input variables.
  |-terraform.tfvars - Assigns values to variables
  |-outputs.tf - Output of the resources that main.tf created.

```

provider.tf: contains the terraform block and provider block (AWS, Azure etc).  
data.tf: contains all data sources.  
variables.tf: contains all defined variables.  
locals.tf: contains all local variables.  
output.tf: contains all output resources.  

# Installing terraform

## On Amazon Linux 2 machine
Launch Amazon Linux 2023 machine and attach a role with admin permissions  

> [!NOTE]: 
> 1. This ec2 instance is going to create resources in the AWS so it requires related permissions, and hence the role to be attached.
> 2. We can fine tune the permissions as required if not a admin role permissions.

Create a srcipt and add the following and run the script.  
```
sudo yum update -y
sudo yum install -y yum-utils
sudo yum -config-manager --add-repo https://rpm.releases.hashicorp.com/AmazonLinux/hashicorp.repo
sudi yum install -y terraform
terraform version
```

## On Ubuntu Machine

Launch a machine, and attach a role with admin permissions.  

Create a srcipt and add the following and run the script.   
```
apt update -y
apt install awscli -y
wget -O- https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
sudo apt update && sudo apt install terraform
terraform -v
```

When ever wants to work with terraform, always keep a seprate directory fo the terraform.
```
mkdir terraform
cd terraform
```

### Terraform commands:
  
To know the version of terraform,
 ```
 terraform --version
 ```
#### Initialize infrastructure

1. Initialize a working directory, it will dowl=nload the providers plugins
   ```
   terraform init
   ```
2. Create an execution plan (dry run) , it wont create infra but gives what will be created
   ```
   terraform plan
   ```
3. Execute/ provision the infra on cloud, or execute changes to actual env,
   ```
   terraform apply
   ```
   It will ask for approval before actual provisioning ---> `yes`.

   To by pass this approval, use
   ```
   terraform apply --auto-approve
   ```
4. Destroy/ cleanup the infra that was provisioned.
   ```
   terraform destroy
   ```

   If want to bypass the approval,
   ```
   terraform destroy --auto-approve
   ```


**Terraform is all about,**
BLocks  
Labels  
Arguments


For example, its see following block which is defined in mian.tf, 

```
provider 'aws' {
  region = 'ap-south-1'
}
```

Here,   
`provider` is the block name.   
`aws` is label.  
`{ }` and insde content is arguments.





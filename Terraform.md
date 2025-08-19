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
5. Wild cards,

   ```
   terraform fmt
   ```
   to format your configuration files into a canonical format and style.
   ```
   terraform fmt -recursive
   ```
   for all files.


   ```
   terraform validate
   ```
   to check the syntax, anf or any errors in the configuration files.


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


# Initialls and terraform files.

1. **init command**:Whenever you have a new or existing Terraform directory (containing your Terraform configuration files), you need to run `terraform init` to prepare that directory for other Terraform commands.
2. **Provider Plugins**: Terraform uses plugins to interface with cloud providers (like AWS, Azure, Google Cloud, etc.). The init command checks the configuration files to see which providers you're using and fetches the required provider plugins.
3. **Provider Versions**: If you’ve specified a particular version of a provider in your configuration, terraform init will download that version. If not, it'll get the latest compatible version.

`+` : Creating  
`-` : Deleting  
`~`  : Update  

When ever we say `terrform init`, a `.terraform` files will be created and it contains lots of information (providers plugins will be stored in this directory). use `cat .terraform` and comprehend the content.  

## STATE FILE  `terraform.tfstate`

Terraform must store state about your managed infrastructure and configuration. This state is used by Terraform to map real world resources to your configuration, keep track of metadata, and to improve performance for large infrastructures.   
This state file is **extremely important**. It maps various resource metadata to actual resource IDs so that Terraform knows what it is managing. This file must be saved and distributed to anyone who might run Terraform.

### Local State and Remote State
By default, Terraform stores state locally in a file named terraform.tfstate.   
with a **local state** file refers to storing the `terraform.tfstate` file on local machine on which we were working. It may rise the risk of looisng or correpting it in some sense, also makes difficlut to work when multiple teams are working on same file. Not advised for professional use case.  
**Remote state** refers to storing the terraform.tfstate file in some remote state data store which can be secure, and can be shared between all members of team to use. Examples of remote store are S3 bucket.

  
```
terraform state list
```
Terraform command used to list all the resources that are currently being tracked in the Terraform state file.  


## Terraform lock file `.terraform.lock.hcl`

When you run terraform init, Terraform downloads the required providers and dependencies and generates the `.terraform.lock.hcl` file.  
If it doesn't already exist. If the file does exist, Terraform checks the versions specified in the lock file and installs those versions.

The `.terraform.lock.hcl` file is a lock file used by Terraform to manage the dependencies of your Terraform project. It ensures that the same versions of provider plugins and modules are used every time you run Terraform, making your infrastructure deployments more predictable and consistent.  

Purpose: Dependency Management, Consistency and Security.


## Current and desired state
**Current state** represent the actual state of our infrastructure resources as they exist in our cloud. _Terraform keeps track the cirrent state of our infra in a state file_ `terraform.tfsatate`.

  **Desired state** is what you defined in your terraform configuration files. It represents the infra that you want Terraform to create, update, or destroy. 

# count argument
Used to specify the count of the resource like an ec2 instance.
ex:
```
provider 'aws' {
  region = 'ap-south-1'
}

resource 'aws_instance' 'my_ec2_instance' {
  count = 5
  ami = 'ami-0492447090ced6eb5'
  instance_type = 't2.micro'
}
```

# Target - to delete a specific resource.
target is a flag that we use in/with `terraform destroy --auto-approve` to delete specific target.


EX:
```
terrafrom destroy --auto-approve -target=aws_instance.one[0]
```

If we want to use multiple specific targets, use `-target=....` multiple times.  
```
terraform destory --auto-approve -target=aws_instance.one[1] -target=aws_instance.one[2]
```

Once the command is executed, use `terraform state` to know the remaining resources list or to verify the destroy command success.  


-------------------------------------------------------------------



# Variables

Variables in terraform (every where) are used to make the configurations more dynamic and reusable.  
Terraform features are a core features that allows us to parameterize out terrafrom configurations.  

By using variables rather than hardcoding the values each time, makes code flexible, resuable, and easier to manage.  

## Types of variables

1. Input variables:
    THese allows us to pass the values into terraform configurations. They are defined uisng the **variable block**.
   
2. Outut variables:
   These are used to return values from the terraform configurations after thay have been applied.
   Often used for sharing data between configurations and modules.

3. Local variables:
   THese are used to assign values to an expression or values within a configuration for reuse, imporving readability and maintainability.

## Variable types:

  1. String - A sequesnce of characters. EX: _'hello'_, _'world'_
  2. Number - Any number value EX: _(-5, 1, 10, 15 etc)_
  3. Bool:    A boolean value (true or false).
  4. list(type):  An ordered list of elements EX: _["a", "b", "c"]_
  5. map(type):  A key-value pair mapping EX: _{ key1 = "value1", key2 = "value2" }_
  6. set(type):  A unique unordered collection of elements EX: _["a", "b", "c"]_
  7. object({...}): A structured object with named attributes
  8. tuple([types]): A fixed sequence of elements with different types

### Some examples:
1. list(string)
   ```
   variable 'instance_type' {
     type = list(string)
     default = ['t2.micro','t2.large','t2.medium']
   }
   ```
   for this we can output things like `length(list)` using a output block.
   ```
   output 'list_length'{
     value = length(var.instance_type)
   }
   ```
   **NOTE:**  
   1. `instance_type` is simply a variable name nothing else.
   2. To call a variable, we use `var.variable-name`.

2. Create 2 variables of list and output the combined list of both.
   ```
   #list-1
   variable 'inst-type' {
     type = list
     default = ['t2.micer','t2.large']
   }

   #list-2
   variable 'int-name' {
     type = list
     default - ['inst-1','inst-2']
   }


   #output block
   output 'combined list' {
     value = concat(var.inst-type, var.inst-name
   }
   ```

3.  Create a list and return only the first element of list.  
    ```   
    variable "fruits" {
      type    = list
      default = ["apple", "banana", "cherry"]
    }
    
    output "selected_element" {
      value = element(var.fruits, 1)
      ```
### Lets do a practical example,

```
vi main.tf
```


```
#provider block
provider "aws" {
  region = 'ap-south-1'
}


# variable blocks

variable 'inst-count' {
  description = 'for defining the count of instances'
  type = count
  default = 3
}

variable 'inst-ami' {
  description = 'defining the ami of the instance'
  type = string
  default = 'ami-0492447090ced6eb5'
}

variable 'inst-type' {
  description = 'tye of the instance'
  type = string
  default = 't2.micro'
}

variable "instance-name" {
  description = "defining a name for the instances"
  type        = string
  default     = "TF-Server"
}

#resources block
resource 'aws_instance' 'TrailInstances' {
  count = var.inst-count
  ami = var.inst-ami
  instance_type = var.inst-type
    tags = {
      Name = var.inst-name
    }
}

```

Use the following commnads one by one to execute the above.
```
terrafrom fmt
terraform init
terrafrom validate
terraform plan
terraform apply --auto-approve
```


Following the above way to define varaibles and using them becomes overhead when no. of variables inscreases. So  we follow/keep them in different configuration file called `variables.tf `.  

```
vi main.tf
```

```
provider "aws" {
  region = 'ap-south-1'
}

resource "aws_instance" "TrailInstance" {
  count = var.inst-count
  ami = var.inst-ami
  instance_type = var.inst-type
    tags = {
      Name = var.inst-name
    }
}
```



```
vi variables.tf
```

```
variable 'inst-count' {
  description = 'for defining the count of instances'
  type = count
  default = 3
}

variable 'inst-ami' {
  description = 'defining the ami of the instance'
  type = string
  default = 'ami-0492447090ced6eb5'
}

variable 'inst-type' {
  description = 'tye of the instance'
  type = string
  default = 't2.micro'
}

variable "instance-name" {
  description = "defining a name for the instances"
  type        = string
  default     = "TF-Server"
}
```
# Terraform  `.tfvars` file.
As of now, we have used `main.tf`, `variables.tf`.   
The terrafrom `.tfvars` file allows us to seprate variable defination from the main configuration, making it easier to manage sifferent enviromnets and keep your codebase clean and orginezed.  

We use `.tfvars` files when we have multiple configurations for different teams like ( prod, dev, test).  
Each configuration we can write on variable file and attach it while running.

THe default name that we use is `terraform.tfvars` for the `.tfvars` file. but,  
we can also create our custom named `.tfvars` files like `dev.tfvars`, `test.tfvars`, `prod.tfvars`.  

#### Lets do an example,  
`main.tf` will have no difference and `variables.tf` will have little diff @ `default` argument. 

```
vi main.tf
```

```
provider "aws" {
  region = 'ap-south-1'
}

resource "aws_instance" "TraulInstance" {
  count = var.inst-count
  ami = var.inst-ami
  instance_type = var.inst-type
  tags = {
    Name = var.inst-name
  }
}
```

```
vi variables.tf
```

```
variable 'inst-count' {
  description = "anything"
  type = number
}

variable "instance_ami" {

  description = "anything"
  type        = string
}

variable "instance_type" {

  description = "anyhting"
  type        = string
}
variable "instance_name" {

  description = "anything"
  type        = string
}
```
Now, we can create 3 different `.tfvars` files each for dev, prod, test.  

```
vi dev.tfvars
```
```
inst-count = 1
inst-ami = 'ami-0492447090ced6eb5'
inst-type = 't2.micro'
inst-name = 'Dev-Server'
```


```
vi test.tfvars
```
```
inst-count = 1
inst-ami = 'ami-0492447090ced6eb5'
inst-type = 't2.micro'
inst-name = 'Test-Server'
```
When there are more than 1 `.tfvars` files, then While running `terraform apply --auto-approve` command we will specify which `.tfvars` has to be used.  
like, 
```
terraform apply --auto-approve -var-file="dev.tfvars"
```

> [!NOTE]
> When we use `terraform apply --auto-approve -var-file="test.tfvars"`, it wont create new set of instances, rather redifines the old with changes form dev.tfvars.
> It is because that we are using the same **default workspace**.


#### _Another type Variable Usage : Command Line Flags: Terraform Command Line and Input Variable_,   

If you don't provide any values on configurations file, TF will ask for values on Command Line or provide inputs to Command Line

For Example: Remove all dev.tfvars, prod.tfvars and test.tfvars

First cat Variables.tf - No values defined there in variables.tf

##### Command Line Flags: Terraform Command Line


`terraform apply --auto-approve  **`  --> it will ask the values on Command Line.  

`terraform destroy --auto-approve  **`  --> it will ask the values on Command Line.  


##### Input Variable
```
terraform apply --auto-approve -var="inst-type=t2.micro" -var="inst-count=1" -var="inst-name=test-server" -var="inst-ami=ami-0492447090ced6eb5"
```

```
terraform destroy --auto-approve -var="inst-type=t2.micro" -var="inst-count=1" -var="inst-name=test-server" -var="inst-ami=ami-0492447090ced6eb5"
```

In above destroy command, remove one variable and destroy, TF will ask in Command Line but if you don't give also, it will take from statefile and destroy.  


# Terraform output variable 
These are used to return values from your Terraform configurations after they have been applied, often used for sharing data between different configurations or modules.  

Example, 
```
provider "aws" {
  region = 'ap-south-1'
}

resource "aws_instance" "MyInstance" {
  ami = ""
  instance_type = "t2.micro"
  tags = {
    Name = "Example-server"
  }
}

output "inst-info" {
  value = [aws_instance.MyInstance.public_ip, aws_instance.MyInstance.private_ip, aws_instance.MyInstance.public_dns]
```
If we need all the info of the ec2 then use `value = aws_instance.MyInstance`.    



And from now on, we will follow this file structure
```
├── main.tf
├── output.tf
├── provider.tf
├── terraform.tfvars
└── variables.tf
```


# Taint   
Taint in terraform is used to recreate a specific resource in infracture.  

Terraform fain command is used to manually mark a specific resource for recreation.  When we mark a resource as 'tainted', it indicates to terraform that the resource is in a bad or inconsisent condition stat and should be destroyed and recreated during the next terraform apply operation.  

_When to Use_ : Failed Deployments, Manual Changes and Resource Corruption.  

Example:  
```
vi main.tf
```
```
provider "aws" {
  region = 'ap-south-1'
}

resource "aws_instance" "MyInstance" {
  ami = "ami-"
  instance_type = "t2.micro"
  tags = {
    Name = "taint-server-example"
  }
}

resource "aws_s3_bucket" "MyS3Bucket" {
  bucket = "taint-server-exapmle-bkt"
}
```

Use the following commands one by one,  
```
terraform apply --auto-approve
terrform state list
terraform taint aws_s3_bucket.MyS3Bucket
terraform apply --auto-approve
# This will now delete only s3 bucket and recreate it not the EC2
# since only the s3 is marked as taint.
```

**TO untaint** :
```
terraform untaint aws_instance.MyS3Bucket
```

# Terraform locals  
In Terraform, locals are used to define and assign values to variables that are meant to be used within a module or a configuration block.

Unlike input variables, which allow values to be passed in from the outside, local values are set within the configuration itself and are used to simplify complex expressions, avoid repetition, and improve the readability of your Terraform code.

Example:
```
vi main.tf
```
~~~
provider "aws" {
  region = "ap-south-1"
}

locals {
env = "Prod"
}

resource "aws_vpc" "myvpc" {
  cidr_block = "192.168.0.0/16"
  tags = {
    Name = "${local.env}-VPC"
  }
}

resource "aws_subnet" "subnet1" {
  vpc_id            = aws_vpc.myvpc.id
  cidr_block        = "192.168.1.0/24"
  availability_zone = "ap-south-1a"
  tags = {
    Name = "${local.env}-Subnet"
  }
}
~~~
For the local block, it doesnt need any name, it only takes the arguments, and those will be addressed or reffered as `${local.arg_name}` as show in above example.


Another example, 
```
locals {
  project_name   = "My-Awesome-DevOps"
  environment    = "Students"
  instance_count = 2
  tags = {
    Name        = "${local.project_name}-${local.environment}"
    Environment = local.environment
  }
}
resource "aws_instance" "myinstance" {
  ami           = "ami-0492447090ced6eb5"
  instance_type = "t2.micro"
  count         = local.instance_count
  tags          = local.tags
}
```
  
  
# Terraform Workspace  

In terraform, a **workspace** is an isolated environment where a seprate state file is maintained.  

This feature allows us to manage different environments (like development, staging, production) within the same Terraform configuration.

Each workspace has its own state, enabling you to deploy the same infrastructure to multiple environments without needing to duplicate the configuration files.  

## Key concepts of Terraform workspace
### 1. Isolation
  Each workspace has its own state file. This means the resources managed by Terraform in one workspace are isolated from those in another workspace.

### 2. Use cases
Workspaces are typically used for managing multiple environments (e.g., dev, staging, prod) within a single Terraform configuration.

### 3. Default Workspace
When you first initialize a Terraform directory, it starts with a default workspace named default. You can switch to other workspaces or create new ones as needed.

> [!NOTE]
> We cannot delete a current workspace untill it has resources in it.
> We cannot delete **DEFAULT** workspace.

**All workspace statefiles are under directory `terraform.tfstate.d`.**  

COmmands related to workspace,  
```
terraform workspace list     #To show list of workspace
terraform workspace new dev  #To create and switch to workspace named as dev
terraform workspace show     #To show current workspace
terraform workspace select    #To switch between workspaces
terraform workspace delete    # To delete the workspcae
```

Lets use the locals, terraform workspace combinedly in an example,

```
terraform workspace list
terraform workspace new dev
terraform workspace select dev
```

```
vi main.tf
```

```
provider "aws" {
  region = "ap-south-1"
}

locals {
  instance_types = {
      dev = "t2.micro"
      test = "t2.small"
      prod = "t2.medium"
  }
}

resource "aws_instance" "workspace-example" {
  ami = "ami-08ee1453725d19cdb"
  instance_type = local.instance_type[terraform.workspace]
  tags = {
    Name = "${terraform.workspace}-server"
  }
}

output "active-workspace" {
  description = "current terraform workspace"
  value = terrafrom.workspace
}
output "selected_instance_type" {
  description = "Instance type selected for the current workspace"
  value       = local.instance_types[terraform.workspace]
}
```
> [!NOTE]
> When we refer the local directly (not with in a string), we use `local.arg-name`.  
> When we refer the local within a string we use `${local.arg-name}`.  
> We can abserve that in the above example.


Lets try playing with different workspace, 
```
terraform plan  #you should see t2.micro getting launched

terraform workspace new test  #This will create a new Workspace called test

terraform plan  #you should see t2.small getting launched

terraform workspace new prod  #This will create a new Workspace called prod

terraform plan  #you should see t2.medium getting launched

terraform workspace select dev

terraform apply --auto-approve

terraform workspace select test

terraform apply --auto-approve

cd terraform.tfstate.d

ls

cd .. #come back to main directory

terraform workspace list

terraform workspace delete test   #Workspace "test" is your active workspace, You cannot delete the currently active workspace. Please                       switch to another workspace and try again.

terraform workspace select dev

terraform workspace delete test   #[Error: Workspace is not empty, first delete the resources in workspace and then delete workspace]

terraform workspace select test   #[Again go back to test workspace, destory the infra]

terraform destroy --auto-approve

terraform workspace dev  #[Switch to another workspace to delete the test workspace]

terraform workspace delete test

terraform workspace select dev

terraform destroy --auto-approve

terraform workspace select default

terraform workspace delete dev

terraform workspace list
```

# Terraform backend setup  - Remote state.  
**Remote State**  

By default, Terraform stores state file locally in a file named `terraform.tfstate`. When working with Terraform in a team, use of a local file makes Terraform usage complicated because each user must make sure they always have the latest state data before running Terraform and make sure that nobody else runs Terraform at the same time.  

With remote state, Terraform writes the state data to a remote _data store_(S3), which can then be shared between all members of a team.  

Generally we have the statefile in local, if you lost the machine, statefile is also lost. So that reason we keep statefile in S3. And also, all DevOps Engineers can share the statefile if required.  

As we are using AWS cloud, we will be using S3 bucket for storing the state file remotly.  
So, Create a S3 bucket first with versioning.  

```
vu main.tf
```

```
provider "aws" {
  region = "ap-south-1"
}

terraform {
  backend "s3"  {
    bucket = "terraform-statefile-bkt"
    key = "prod/terraform.tfstate"
    region = "ap-south-1"
  }
}

resource "aws_instance" "MyInstance" {
  ami = ""
  instance_type = "t2.micro"
  tags = {
    Name = 'Backend-example"
  }
}

resource "aws_instance" "mysecondinstance" {
  ami           = "ami-0492447090ced6eb5"
  instance_type = "t2.micro"
  tags = {
    Name = "backend-example2"
  }
}

output "instance_ids" {
  description = "List of EC2 instance IDs"
  value       = [aws_instance.myfirstinstance.id, aws_instance.mysecondinstance.id]
}

output "instance_names" {
  description = "List of EC2 instance names"
  value       = [aws_instance.myfirstinstance.tags.Name, aws_instance.mysecondinstance.tags.Name]
}

```

```
terraform init
terraform validate
terraform plan
terraform apply --auto-approve
````

```
cat terraform.tfstate #[Currently no resources are there]
cat terraform.tfstate.backup #This is the backup of the previous state
```

We actually segrigate the remote backend block into another file, `backend.tf`. Hence the file system looks, 
```

├── main.tf      -- actual code
├── backend.tf   -- contains S3 statefile with statelock in dynamodb
├── provider.tf
├── output.tf    -- instance details as output
├── terraform.tfvars  -- variables
└── variables.tf   -- calling variables from tfvars

```

## Bring back the state file from s3 to local.
If you don't want to use S3 and want statefile to be in local again , modify main.tf and remove the backend code.  

```
terraform init -migrate-state
terraform init -reconfigure
terraform apply --auto-approve
terraform state list  #Now you have the statefile in local
```

## Untrack a terraform resource from statefile and statefile commands.

```
terraform state list
# terraform state rm resource-type.resource-name
terraform state rm aws_instance.MyInstance
terraform state list
cat terraform.tfstate   #it will not show the MyInstance but still EC2 will still be alive in AWS.
terrafrom destroy --auto-approve
```

If we want to import it back, 
```
terraform import aws_instance.MyInstance i-0b1c2d3e4f5g67891
```
Now Check the S3 bucket and contents of the bucket.  

  
  
## `import` in terraform
The terraform command import` is used to bring existing infrastructure resources under terraform management.  

This is practically useful when you have resources that were created manually or by another tool, and you now want to manage thenm using terraform without recreating them.  

EX:  
Lets say we have an untracked ( by terraform) resource say ec2 instance ( id = i-0ab2056f11dfa5a6e ) launched in AWS, and we want terraform to tracked it.

For that we need to manually create a resource block that will reflect the reources ( in our case its EC2 ) that we want to import.  
```
resource "aws_instance" "inst-1" {
}
```
**Note**: we dont need to specify any attributes or arguments.
```
terraform import aws_instance.inst-1 i-0ab2056f11dfa5a6e
```
**NOTE**: The name for the resource `inst-1` we used should match witht the resource name that we defined. and the `id` should match from instance that we want to import.   

Terraform does not support importing multiple resources in a single command or operation.  

Each resource must be imported individually using the terraform import command. However, you can streamline the process by scripting the import commands, especially if you have a large number of resources to import.  

Terraform's import command works one resource at a time, so multiple resources need to be imported individually.  

For Multiple resources import use another tool called **TERRAFORMER**.  
  

## Securing statefile in backend with State Lock option
**State Lock**

State locking is a mechanism that prevents multiple Terraform processes from simultaneously attempting to modify the same state file. Without state locking, concurrent Terraform operations could corrupt the state file, leading to unpredictable behavior and infrastructure issues.

State locking happens automatically on all operations that could write state. You won’t see any message that it is happening. If state locking fails, Terraform will not continue. You can disable state locking for most commands with the -lock flag but it is not recommended.  

Along with S3 bucket, create a Dynamodb table in AWS,   
**Table name** = dynamodb-terraform-state-lock  
**Column** = LockID  


So the backend.tf files takes, 
```
terraform {
  backend "s3" {

    bucket         = "terraform-statefile-reyaz"
    key            = "prod/terraform.tfstate"
    encrypt        = true
    dynamodb_table = "dynamodb-terraform-state-lock"
    region         = "ap-south-1"
  }
}
```


# Meta arguments in terraform 

In Terraform, meta-arguments are special arguments that you can use with resources, modules, and other blocks to control how they behave.  

The most commonly used meta-arguments in Terraform include, 
### 1. count
The `count` meta-argument allows us to specify the no. of instances of a resource or module to create.

EX:
```
provider "aws" {
  region = "ap-south-1"
}

resource "aws_instance" "myinstance" {
  count         = 2
  ami           = "ami-08ee1453725d19cdb"
  instance_type = "t2.micro"
  tags = {
    Name = "WebServer-${count.index}"
  }
}

output "instance_ids" {
  description = "List of EC2 instance IDs"
  value       = aws_instance.myinstance[*].id
}
output "instance_names" {
  description = "List of EC2 instance names"
  value       = aws_instance.myinstance[*].tags.Name
}
```
### 2. for_each
The `for_each` meta-argument allows you to create multiple instances of a resource or module based on the elements of a set.   
It provides more control and flexibility than `count`.   
  
count vs for_each : count will create identical resources, for_each will create different resources.

```
provider "aws" {
  region = "ap-south-1"
}

resource "aws_instance" "myinstance" {
  for_each      = toset(["dev-server", "test-server", "prod-server"])
  ami           = "ami-08ee1453725d19cdb"
  instance_type = "t2.micro"
  tags = {
    Name = "${each.key}"
  }
}

output "instance_ids" {
  description = "List of EC2 instance IDs"
  value       = { for k, v in aws_instance.myinstance : k => v.id }
}

output "instance_names" {
  description = "Instance names"
  value       = { for k, v in aws_instance.myinstance : k => v.tags.Name }
}
```

~~~
toset() is a function to create multiple EC2 instances from a list of names:

Terraform will generate a map of instances with keys as "dev-server", "test-server", and "prod-server".

The for expression iterates over aws_instance.myinstance
k represents the instance key (dev-server, test-server, etc.)
v.id retrieves the instance ID
The result is a map of key => instance_id

In for_each , we can play with key and value like .key and .value
~~~

### 3. depends_on
The depends_on meta-argument explicitly defines dependencies between resources. This ensures that one resource is created or updated only after another resource has been successfully created or updated.  

```
provider "aws" {
  region = "ap-south-1"
}

resource "aws_instance" "myinstance" {
  ami           = "ami-08ee1453725d19cdb"
  instance_type = "t2.micro"
tags = {
    Name = "DependsOn-Example"
  }
}

resource "aws_eip" "myinstance_eip" {
  instance   = aws_instance.myinstance.id
  depends_on = [aws_instance.myinstance]
}

output "elastic_ip" {
  description = "Elastic IP of the instance"
  value       = aws_eip.myinstance_eip.public_ip
}

output "instance_id" {
  description = "EC2 instance ID"
  value       = aws_instance.myinstance.id
}

```
### 4. provider
The provider meta-argument allows you to specify which provider configuration to use for a particular resource or module. This is useful when you have multiple configurations for the same provider, such as when managing resources in multiple regions.



### 5. lifecycle
The lifecycle meta-argument allows you to control the lifecycle of a resource. It provides options to prevent the destruction of resources, create resources before destroying existing ones, or ignore changes to specific attributes.  

#### 5.1. `create_before_destroy` 
If you change the instance type or instance name , security groups etc , It will change immediately ,
instance will not delete but if you want to change the image id of the EC2 instance , instance will delete first and then create a new instance with new ami-id.  

```
provider "aws" {
region = "ap-south-1"
}

resource "aws_instance" "one" {
ami = "ami-08ee1453725d19cdb"
instance_type = "t2.micro"
tags = {
Name = "reyaz-server"
}
lifecycle{
create_before_destroy = true
}
}
```
`terraform apply --auto-approve`      
  
Now change the image id to ami-022ce6f32988af5fa.  

`terraform apply --auto-approve`    #First instance will be created and then old instance will be deleted.

Note: if you remove the code in main.tf and terraform apply , resources will be deleted.  

Give a try,  
`vi  main.tf`  

keep only provider and remove all code and give destroy  

`terraform destory --auto-approve`  

#### 5.2. `prevent_destroy`  
resources will not delete if you give destroy command. 
```
provider "aws" {
region = "ap-south-1"
}

resource "aws_instance" "one" {
ami = "ami-08ee1453725d19cdb"
instance_type = "t2.micro"
tags = {
Name = "reyaz-server"
}
lifecycle{
prevent_destroy = true
}
}
```
  
```
terraform apply --auto-approve

terraform destroy --auto-approve
#It will not destroy as prevent_destroy is true , make it false and then destroy.
```


#### 5.3. `ignore_changes`  
If anyone modified the resources in AWS console which is created by TF, It will ignore that changes, it will not bring back to desired state. Actual State is AWS Console, Desired State is Statefile.  

EX: 
```
provider "aws" {
  region = "ap-south-1"
}

resource "aws_instance" "myinstance" {
  ami           = "ami-08ee1453725d19cdb"
  instance_type = "t2.micro"
  tags = {
    Name = "trail-server"
  }
  lifecycle {
    ignore_changes = all
  }
}

output "instance_id" {
  description = "EC2 instance ID"
  value       = aws_instance.myinstance.id
}
output "instance_name" {
  description = "Instance Name"
  value       = aws_instance.myinstance.tags.Name
}
```

Now, modify instance_type or tags or ami in configuration block , TF will ignore the changes while apply
example: modify instance_type = "t2.nano" and trail-server to hello-server.  

```
terraform apply --auto-approve
```
Note: No change, use `terraform state list` to verify.  



# Provider types in Terraform 
Terraform has 3 main providers  
1. Official : maintained by Terraform (AWS, Azure, GCP)  
2. Partner : Maintained by terraform and organizations (Oracle, Alibaba)  
3. Community : Maintained by individual  


EX: 1 Github   
Create a token first in GitHub --> Settings --> Developer Settings --> Personal access tokens (classic) --> Generate new token(classic)

```
provider "github" {
  token = "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"
}

resource "github_repository" "example" {
  name        = "tf-github-repo"
  description = "created repo from tf"

  visibility = "public"

}
```
EX: 2 Local provider    
```
provider "local" {
}

resource "local_file" "one" {
  filename        = "test.txt"
  content = "this is from test data from tf using local provider"
}
```
```
terraform apply --auto-approve
ls

#it will create a new file locally

terraform destroy --auto-approve
```

EX: 3 Docker  
```
yum install docker -y
systemctl start docker
```

```
terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 2.0"
    }
  }
}
provider "docker" {
  host = "unix:///var/run/docker.sock"  # For Linux/macOS
}

resource "docker_image" "nginx" {
  name         = "nginx:latest"
  keep_locally = false  # Removes the image when the container is deleted
}

resource "docker_container" "nginx" {
  name  = "nginx-container"
  image = docker_image.nginx.image_id

  ports {
    internal = 80  # Inside the container
    external = 8080  # Exposed on the host machine
  }
}

output "container_name" {
  value = docker_container.nginx.name
}

output "container_id" {
  value = docker_container.nginx.id
}

output "nginx_url" {
  value = "http://13.201.46.206:8080"
}
```

```
terraform init -upgrade
terraform plan
terraform apply --auto-approve
```

Access @ `http://13.201.46.206:8080`  

EX: 4 K8s  
Setup a minikubecluster first or even go with KOPS.  

```
terraform {
  required_providers {
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.0"
    }
  }
}

provider "kubernetes" {
  config_path = "~/.kube/config"  # Adjust if using a different kubeconfig
}
resource "kubernetes_deployment" "nginx" {
  metadata {
    name = "nginx-deployment"
    labels = {
      app = "nginx"
    }
  }

  spec {
    replicas = 2

    selector {
      match_labels = {
        app = "nginx"
      }
    }

    template {
      metadata {
        labels = {
          app = "nginx"
        }
      }

      spec {
        container {
          image = "nginx:latest"
          name  = "nginx"

          port {
            container_port = 80
          }
        }
      }
    }
  }
}

resource "kubernetes_service" "nginx" {
  metadata {
    name = "nginx-service"
  }

  spec {
    selector = {
      app = "nginx"
    }

    port {
      protocol    = "TCP"
      port        = 80
      target_port = 80
    }

    type = "LoadBalancer"
  }
}
```


# Modules in terraform  
Terraform modules are a fundamental featur that help in organization and reuse terraform configurations.  

A **Module**  is a container for multiple resources that are used together. 

Modules allow you to encapsulate and manage resources as a single unit, making your Terraform configurations more modular, readable, and maintainable.  

**Root Module:**  
* The root midule is the amin configuration where theeraform statrs it execution.
* It is usually defined in the main configuration directory where terraform init and terraform apply are run.
* The root module can call other modules, referred to as child modules.

**Child Modules:**
* Child modules are modules that are called from within other modules (including the root module).
* They help in organizing resources and reusing configurations.
* Each child module can be stored in a separate directory and can be called using a module block in the root module or another parent module.

Lets create a module directory with instance, bucket, and vpc.  

```
├── main.tf
├── modules
│   ├── ec2-instances
│   │   ├── main.tf
│   │   ├── outputs.tf
│   │   └── variables.tf
│   ├── s3-bucket
│   │   ├── main.tf
│   │   ├── outputs.tf
│   │   └── variables.tf
│   └── vpc
│       ├── main.tf
│       ├── outputs.tf
│       └── variables.tf
└── terraform.tfstate
```
Import `terr` for better visualization.
```
yum install tree -y
```

Check the {https://github.com/AreParameswarudu/}

# Dynamic Block, Terraform Provisiones 

**Provisioners**  
Terraform provisioners are used to perform actions on a local or remote machine after a resource is created or updated.  

They are typically used for tasks such as **configuring** or **installing software** on a machine, which Terraform itself does not handle directly.  

Type os provisioners
---------------------

### 1. l`ocal-exec`
Executes a command locally on the machine where Terraform is run.  
Useful for running scripts or commands that need to be executed locally.  

EX:   
In this example, the local-exec rovisioner writes the instance IN to a file instance_id.txt on the local machine after the ec2 instance is created.  

```
resource "aws_instance" "Example" {
  ami = "ami-08ee1453725d19cdb"
  instance_type = "t2.micro"

  Provisioner "local-exec" {
    command = "echo 'Insrcnce ID: ${self.id}' > instance_id.txt"
  }
}

output "instance_id" {
  value = aws_instance.example.id
}
```
self.id will be available after the instance is created.  
The provisioner runs on the local machine, saving the instance ID to instance_id.txt.  

use `terraform apply --auto-approved` to see the `instance_id.txt` file created automatically and respective resluts in the file as well.  


### 2. `remote-exec`  
Executes commands on a remote resource, such as an EC2 instance, after it has been created. It typically requires a connection configuration.  
Useful for configuring instances or applying configurations remotely.  


EX:  
In this example, from TF machine , we will connect remotely to another machine, for this we need to have pem file under `~/.ssh/id_rsa`  

```
vi ~/.ssh/id_rsa
```
copy past the pem file data.  

```
vi main.tf
```

```
resource "aws_instance" "example" {
  ami = "ami-08ee1453725d19cdb"
  instance_type = "t2.micro"
  key_name = "MyKey"
  tags = {
    Name = "ec2-instance"
  }

  Provisioner "remote-exec" {
    inline = [
      "sudo yum update -y", 
      "sudo yum install -y httpd",
      "cd /var/www/httpd/html",
      "echo 'Hey this is my first website onec2' ",
      "sudo systemctl start httpd"
      ]
      connection {
        type = "ssh"
        user = "ec2-user"
        private_key = file("~/.shh/id_rsa")
        host = self.public_ip
      }
    }
}
```
Use `terraform apply --auto-approve` and use the public ip of the instance to access the website.  

### 3. `file` provisioner
 The file provisioner uploads files from the local machine to the remote resource.  

 EX:  
 create a script file in a machine that we are at,  
 ```
cd /tmp
vi remote_script.sh
```

```
#!/bin/bash

# Example commands to run on the remote instance
echo "Running remote script"

# Update the system
sudo yum update -y

# Install Apache HTTP Server
sudo yum install -y httpd

# Start and enable the Apache service
sudo systemctl start httpd
sudo systemctl enable httpd

# Write content to /var/www/html/index.html with sudo
echo "<html><h1>This is AWS Infra created using Terraform in Mumbai Region!</h1></html>" | sudo tee /var/www/html/index.html > /dev/null
```
Now lets use that script for ec2 instance created using terraform.  

```
vi main.tf
```
```
resource "aws_instance" "apache-inst" {
  ami = "ami-08ee1453725d19cdb"
  instance_type = "t2.micro"
  key_name = "MyKey"
  tags = {
    Name = "ec2-apache-inst"
  }

  provisioner "file" {
    source = "remote_script.sh"
    destination = "/temp/remote_script.sh"

    connection {
      type = "ssh"
      user = "ec2-user"
      private_key = file("~/.ssh/id_rsa")
      host = self.public_ip
    }
  }

  provisioner "remote-exec" {
    inline = [
      "chmod +x /tmp/remote_script.sh",
      "/tmp/remote_script.sh"
    ]
    connection {
      type = "ssh"
      user = "ec2-user"
      private_key = file("~/.ssh/id_rsa")
      host = self.public_ip
      }
    }
}

output  "instance_ip" {
  value = aws_instance.apache.public_ip
}
```

## Dynamic Block  
It is used to reduce the length of the block.  

Example: Launch a new EC2 instance with security group allowed protocols 22 and 80, in this example we should create multiple ingress rules for multiple protocols.  

But instead writing multiple ingress rules, we can use dynamic block.  

```
provider "aws" {
  region = "ap-south-1"
}

locals {
  ingress_rules = [{
    port        = 443
    description = "Ingress rules for port 443"
    },
    {
      port        = 80
      description = "Ingress rules for port 80"
    },
    {
      port        = 8080
      description = "Ingress rules for port 8080"

  }]
}

resource "aws_instance" "ec2_example" {
  ami                    = "ami-08ee1453725d19cdb"
  instance_type          = "t2.micro"
  vpc_security_group_ids = [aws_security_group.main.id]
  tags = {
    Name = "Terraform EC2"
  }
}

resource "aws_security_group" "main" {

  egress = [
    {
      cidr_blocks      = ["0.0.0.0/0"]
      description      = "*"
      from_port        = 0
      ipv6_cidr_blocks = []
      prefix_list_ids  = []
      protocol         = "-1"
      security_groups  = []
      self             = false
      to_port          = 0
  }]

  dynamic "ingress" {
    for_each = local.ingress_rules

    content {
      description = "*"
      from_port   = ingress.value.port
      to_port     = ingress.value.port
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
  }

  tags = {
    Name = "terra sg"
  }
}
```

# Data source block in terraform  
In terraform, a data block or data source allows you to fetch information from existing resourecs or services that are external to your terraform configuration.  

_Fetch info about existing resources:_  
If you need to retrieve info about an existing reosurce that wasnot created by your terraform config (ex: existing VPC, or EC2 AMI etc).  

EX:  
To get the existing VPC and bicket details.  

```
vi main.tf
```
```
provider "aws" {
  region = "ap-south-1"
}

data "aws_vpc" "default {
  default = true
}

resource "aws_instance" "MyInstance" {
  ami = "ami-08ee1453725d19cdb"
  instance_type = "t2.micro"
  subnet_id = data.was_vpc.default.id
}

data "aws_s3_bucket" "example_bucket" {
  bucket = "test-bkt"
}

output "bucket_arn" {
  value = data.aws_s3_bucket.example_bucket.arn
}
```

```
terraform apply --auto-approve

terraform destroy --auto-approve
```

**Note**:  
Notice how we referred the resource from data block in the resource block.  


# Conditions

# Terraform vault  
HashiCorp Vault is a tool designed to securly store and manage sensitive info such as **secrets**, **passowrds**, **certificates** and **API keys**.  

Terraform can be integrated with Vault to dynamically retrieve and manage secrets as part of your infrastructure provisioning process.  


```
sudo yum install -y yum-utils

sudo yum-config-manager --add-repo https://rpm.releases.hashicorp.com/AmazonLinux/hashicorp.repo

sudo yum -y install vault

systemctl status vault

systemctl start vault

vault server -dev

vault secrets enable -path=secret kv

vault kv put secret/mysecret password="supersecretpassword"
```


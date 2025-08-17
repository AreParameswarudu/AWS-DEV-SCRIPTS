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

+    : Creating  
-    : Deleting  
~    : Update  

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


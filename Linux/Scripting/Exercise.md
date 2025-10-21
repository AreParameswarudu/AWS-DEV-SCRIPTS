## Q1
Write a one-liner to find the top 10 largest files under /home .

We can use `du -h` command  followed by path to dir to get the disk usage of the conents in that path and we can use the `sort` responce. 
so the whole command goes like `du -h /home | sort -h | tail 10`. But it will give the responce of only the folders in it not the files.

so, it needs a bit additoinal, like `find`, `type` flag to only include files. and the answer goes like, 
```
find /home -type f -exec du -h {} + 2> /dev/null | sort -h | tail-10
```
where `2> /dev/null` is to slience the errors.

## Q2
What is the difference between `kill`, `kill -9`, `pkill`? 

All these commands were used on process running on the OS. These processes can be inbuilt or installed (like nginx, apache, etc).  
TO list all processes, we use `ps aux`,

`kill process_name`  used to kill specific process by SLOWLY.  
`kill -9 process_name`  used to HARD kill or ABRUPTLY kill process.  
`pkill process_name`   used to kill all process by name specified.  


## Q3
Write a script to check that id a given service ( nginx) is running. If not, restart it.

This requires us to use the `if` conditional statements, 
```
#!/bin/bash

if [ systemctl status nginx | grep inactive]; then
    systemctl start nginx
else
    echo "nginx is active and running"
fi
```
This is not dynamic ( only usefull for testing nginx service) and can only be used when nginx is already installed.

To make it dynamic, we can use `read` command to give the users to provide the name of the service to check for, 
```
#!/bin/bash

echo "Enter the service name"
read service_name
if [ systemctl status $service_name | grep inactive ]; then
    systemctl start $service_name
else
    echo $service_name " is active and running"
fi
```

## Q4 
Schedule to a cron job to delete files older than 30 days in `/temp` dir.

`* 0 1 * * /bin/bash delete_30d.sh `


and the `delete_30d.sh` will be of, 
```
#!/bin/bash

#dir to clean
Target_dir="/temp"

#Log file path
Log_file="/var/log/delete_30d.log"

#Timepstamp 
TimeStamp=$(date '+%Y-%m-%d %H:%M:%S')

# start log
echo "[$TimeStamp] starting cleaning of $Target_dir " >> "$Log_file

#Check if directory exists
if [ ! -d $Target_dir ]; then
    echo "[$TimeStamp] Error: Directory $Target_dir does not exist." >> "$Log_file"
    exit 1
fi

#delete files older than 30 days
find "$Target_dir" -type f -mtime +30 -print -delete >> "$Log_file" 2>&1

#Completion log
echo "[$TimeStamp] cleaning completed." >> "$Log_file"
```


## Q5
Create a script that takes a list of IPs form a file and checks which ones are reachable ( ping ).

Create a text file and add IP addresses to it and name it as `file.txt`. add IP addresses like ( 8.8.8.8, 192.168.1.0, 8.8.8.4, 10.0.0.1)

[!NOTE]
> `8.8.8.8` is the IP of server maintained by google that can be reachable from any ip address, so we will get responce.  
> all other ips were either personal or not even reacheable form public, so no responce form then.

```
#!/bin/bash

while read -r ip;
do 
    if [ ping -cw -w2 $ip &> /dev/null ]; then
        echo " $ip is reacheable"
    else
        echo "$ip is not reacheabel"
    fi
done < file.txt
```

## Q6
Write a script that monitors `/var/log/auth.log` and prints all failed login attempts in real time.

```
#!/bin/bash

tail -F /var/log/auth.log | grep -line-buffered "Failed password"
```

`tail -F` --> Follows the file even if it is rotated ( better than -f ).

## Q7 
How do you check which ports are listening on your linux server! 

We can directly use a command that gives us the which ports are open,   
```
ss -tlunap
```  

`-t`  = tcp  
`-u` = udp  
`-l` = Listening scokets only  
`-p` = show process suing the ports  
`-n` = numeric address  
`-a` = show all scokets.  


## Q8
How do you print all environment variables in linux

1. Assigning ENV variables
    1.1 Temporary variable   
    `export my_var="Hello World"`  
    This temporary variable will be available to child processes but will expire when session ends.  

    1.2 Inline assignment  
    `my_var="Hello World" ./script1.sh`  
    This kinds of variables are available only during execution of `script1.sh`.  

    1.3 Permanent assignment (across sessions)  
    After assigning the variable, use `source ~/.bashrc` to add the variable to bashrc.  
    `export my_Var="Hello world"`, and folloed with `source ~/.bashrc`.  



2. Listing/printing env variables.

    use `printenv` or `env` to print all variables.  
    use `echo $my_Var` to print specific variable.  

    Use `set` to list all shell variables ( includes env + local )

3. Unset a variable

    use `unset my_Var` to unset the variable that was already set.  




## Q9
How do you pass arguments to a shell scripts

## Q10 
What does the `$0`, `$1`, `$#` and `$@` represent in a shell scripts.

These special variable are used to handle command-line arguments passed to the script.  
`$0` represents the name of the script itself.  
`$1`, `$2` ... represents the first, second, etc  command-line arguments passed to the script.  
`$#` represents the count of total no.of positional arguments passed to the script.  
`$@` repesents all the positional arguments as sperate words (preserving quoting).

EX:
```
./script.sh  Hyderabad Telangana India
```
Inside the `script.sh`, these variables would hold:
`$0` --> `./script.sh`  
`$1` --> `Hyderabad`  ( argument-1 passed to script)  
`$2` --> `Telangana`  ( argument-2 passed to script)  
`$3` --> `India`      ( argument-3 passed to script)  
`$#` --> 3            ( Total count of argument passed )  
`$@` --> `Hyderabad Telangana India`   ( List of arguments)  

## Q11 
Write a bash script to check if a file exists and readable.

```
#!/biin/bash

echo "enter the directory path"
read dir_path
echo -e "\n enter the file name"
read file_name
abs_path = $dir_path/$file_name
if [ -f $abs_path ]; then
    if [ -r $abs_path ]; then
        echo 'File exists and is readable"
    else
        echo "File exists and is not readable"
    fi
else
    echo "File does not exists"
fi
```

## Q12 
How do you handle errors in a shell script? Give example.

Different ways of handling the errors,  
To ways to appraoch this, 
### 1. To add the errors to the log files
In bash and most shells,  ( `1` and `2` represents the file descriptions)
--> `1` --> Standard output (stdout)   
--> `2` --> Standard Error (stderr)  

so when we say, `command >> output.log 2>&1`    
we mean to say, send stdout to `output.log` and also, send stderr to where stdout is going ( i.e. also to `output.log`). This ensures that both output and errors go to the same place.

| Synatx | Meaning|
|---|---|
| `>` | Redirect `stdout` to a file (overwrite) |
|  `>>` | Redirect `stdout` to a file (append) | 
| `2>` | Redirect the `stderr` to a file|
| `2>>`| Append `stderr` to a file |
| `2>&1` | Redirect `stderr` to where ever `stdout` is going |
| `&>` | Redirect bothe `stdout` and `stderr` to a file ( bash shorthand) |

EX: script.sh
```
#!/bin/bash
myscript.sh >> /var/log/myscript.log 2>&1
```


### 2. To use `set -x`, `set -e` commands to know at which command caused error.

 #### 2.1. Using `set -x` after the shebang to print which command of script is being executed and to interpert at which command the error was.

 #### 2.2. Using `set -e` after the shebang to exit the script execution after any error or script failure.

 #### 2.3. Using or checking the logs for the cron job  errors at the ath `/var/log/syslog`.

 #### 2.4. Check the exit status ( `$?` )  
  if `$? =0` refers to sucess, if not 0 or equal to any other integer ( 1,2,17,etc ) refers to not sucess or error.

Example script to check if a coping a file to `/backup/` was success or not.  
```
#!/bin/bash
cp file.txt /backup/
if [ $? -ne 0]; then    
    echo "Failed to copy the file"
    exit 1
fi
```

## Q13
Write a script to monitor disk usage and send an alert if it exceeds a threshold.
Create a file named `script.sh`  

```
#!/bin/bash

mount_path='/'
#Defining the threshold
Threshold=75  
usage=$( df -h "$mount_path" | awk 'NR==2 {gsub("%", "", $5); print $5}')

if [ "$usage" -ge "$Threshold" ]; then
    echo "Disk usage is at ${usage}% and is more than threshold"
else
    echo "Disk usage is fine and is below threshold"
fi
```
Here,   
`awk` is a pattern scanning and processing language. It reads input line by line, splits each line into fields (columns) and lets us to apply logic to extract, transform, or report data.  Its like a mini scripting language built for structured text.  

Core concepts of `awk`:  
1. Input is processed line by line, 
Each line is referred as record, and awk reads one record at a time.

2. Fields are auto-split:
By default, fields are split by whitespaces, we can change the delimeter suing `-F`,   
`$1` refers the firts column, `$2` refers 2nd column and so on.

3. Built in variables
| Variable | Meaning|
|---|---|
| `NR` | Current line number (record number) |
|  `NF` | Number of fields in the current line | 
| `$0` | Entire line |
| `$1`, `$2`| individual records |

4. Common functions
`print` --> output fileds.  
`gsub( regex, replacement, target)` --> global substitution (not inplace).  
`length($0)` --> length of line.  
`tolower($1)` --> lower case convertion.  
`substr($3,1, 5)` --> substring of field 3.  



## Q14 
Write a bash script to find and kill the processes that are using a given port.  


Create a script named `script.sh`  
```
#!/bin/bash
file_path="/var/log/myapp-log"
awk "{print $3}" "$file_path"
```

## Q15
How do you use `trap` in bash scripts and give an example for such usages.  


`trap` command is used to run/execute a custom defined command when the script exits or encounters errors.  
ex: `trap 'echo "Script failed at line $LINENO"; exit 1' ERR

## Q16
Write a bash script to perform a backup of a directory to another location.

Well the question is little ambiguous, so lets assume few aspects here, we will make the script dynamic by giving the users the ability to prompt which directory to be migrated, where ( server ip) to, and what is the destination.

```
#!/bin/bash

echo "started migrating...."

#inputing for users 
read -p "Enter the source directory path: " source_dir
read -p "Enter the backup server IP: " backup_server
read -p "Enter the distribution path on server: " dest_path

#check if source directory exists
if [ ! -d "$source_dir" ]; then
    echo "Source Directory doesnot eixst."
    exit 1
fi

#check if server is reacheable
ping -c 1 "$backup_server" > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "Cannot reach backup server at $backup_server"
    exit 2
fi

#create .tar.gz for the source_dir
source_dir_gz="target_dir.tar.gz"
tar -czf "$source_dir_gz" "$source_dir"

# perform backup using rsync
rsync -avz "$source_dir_gz" "$backup_server:$dest_path"

if  [$? -eq 0]; then
    echo "Migration complete"
else
    echo "Migration failed"
fi

echo "Script execution was complete."
```

## Q17

How do we securly store and use passwords in shell scripting!!

When do we use them, 
1. Connecting to remote server: via SSH, SFTP or rsync.  
2. Accessing databases: Mysql, PostgresSQL, etc.  
3. Interacting with APIs: that require authentication.  
4. Mounting network drives or encrypted volumes.  
5. Running backup scripts that push to cloud or remote storage.  

Secure strategies to  store and use passwords:
1. Using Env variables
```
export DB_PASSWORD="mySecret123"
```

With that we can just refer the env variable as, 
```
#!/bin/bash
echo "Using password: $DB_PASSWORD"
```
But was not more secured.

2. Use of `.netrc` or `.pgpass` files  
For tools like `culr`, `ftp`, or `psql`, we can use dedicated files:
*   `~/.netrc` for FTP or curl  
*   `~/.pgpass` for postgreSQL  
These files should be owned by user and also to set `chmod 600` for security.  

3. Use a password manager or secret vault.  
Foe enterprise-grade security, use tools like,   
* HashiCorp Vault
* AWS Secret manager
* Gnome Keyring / KWallet 
With them, the scripts can query the vault securely and retrive the password only when needed.  

4. Prompt the user at runtime  
```
read -s -p "Enter your passwword: " password
```
here, `-s` will hides the input and by this way, the password wiil be kept in memory for the duration of execution.   

5. Use of SSH keys intead of passwords  
For remote access ( eg. rsync, scp, ssh) use key-based authentication.

```
rsync -e 'ssh -i ~/.ssh/idrsa" /data user@server:/backup
```
No password needed, and more secure.  

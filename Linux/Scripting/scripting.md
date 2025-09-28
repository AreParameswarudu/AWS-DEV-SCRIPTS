# SCRIPTING:
1. Shell / bash
2. Python


## What is scripting:
	
A script is a file that contains a series of Linux commands that are to be executed in the same order line by line.
By saving these commands in a script, we can repeat the same sequence of steps multiple times and execute then by running the script.

	
By-default, scripting in Linux uses shell to run the scripts.
But, we can use Bash to run the same.

Shell and Bash in scripting are used interchangeably but yes they have subtle difference.
Shell script directly starts with series of commands, 
Bash script starts with #!/bin/bash (shebang) followed by series of commands.


To determine the type of shell that our system uses, 
```
ps
```

	
To know the bash shell path, we can use
```
 which bash
```
	
# Scripting
	
We basically uses the extension of .sh for scripts but without the extension is also fine.
 

Example script titled as `print.sh`
```
#!/bin/bash
echo "Today is " `data`

echo -e "\n enter the path to directory"
read the_path

echo -e "\n your path has following files and directories"
ls $the_path
```
		

## 1. Comments in scripting 

To enhance the readability.
  
This line starts with `#` so it is treated as comment

## 2. Variables  
Let us store data.

```
name=param
```
created a variable as name and assigned value to it.

To call the variable,
```
$name
```

### conventions for variable name:

* can start with letter or _  and not any other
* are case sensitive
* con not contain special characters
* not to use ( if, else, then, etc ) keywords.

## 3. Inputs and outputs  in scripting   
To give the user the ability to pass info.
	
### 3.1   read command

```
read
```
It will give the users the ability to pass the details/inputs to the script.
	
ex:
```
#!/bin/bash
echo "what is your name"
read entered_name
echo -e "\n welcome to the scripting " $entered_name
```

### 3.2. Reading formt the file
	
ex:
```
while read line
do
	echo line
done < input.txt
```

reads each line form the input.txt file and prints each line.

### 3.3  command line arguments.

In bash scripting, 
* `$1` represents 1st argument passed.  
* `$2` represents the 2nd argument passed and so on.


create script named greetings.sh
				
```
#!/bin/bash
echo "Hello" $1
```

while executing the script, give the argument as well.
`sh greetings.sh Param`  
Hello Param, will be printed.

### 3.4 Writing to file

```
echo "Add this line to text file" > output.txt
```

```
echo "Append this line to text file" >> output.txt
```

`>` ----- to rewrite the actual file.  
`>>` ----- append at the end of file.

### 3.5 Redirecting file

```
ls > file.txt
```

		
## 4. ( if/ else  )  Conditional statements :
		
Template:

```
if  ( condition );
then
	action/statement/work/print
elif ( condition ); 
then 
	action/statement/work/print
else
	do this by default
fi
```	
		

### 4.1 Logical operations  inside the condition.
	
`-a`   ===== and   
`-lt`  ===== less than  
`-gt` ===== greater than  
`-o`  =====	or   

ex: 
```
if  ($b -gt 60 -a $c -lt 20 );  then
			echo "Your on right track"
```

		
## 5. Looping and branching in Bash       
https://www.freecodecamp.org/news/bash-scripting-tutorial-linux-shell-script-and-command-line-for-beginners/
	
### 5.1 While loop

		
### 5.2 For loop
	
### 5.3 case statements


## 6. Scheduling scripts using cron jobs.

Cron is used to schedule a job/script / any executable or runnable file automatically/automated

	
Crontab utility is used to add and edit the cron jobs
`crontab -l`     ---> lists all the scheduled scripts for a particular user.
	
`crontab -e`    ---> to add or edit the cron jobs

	
	 
Cron job example
```
*  *  *  *   sh /path/to/the/script
```

	
## 7. debugging and trouble shooting.

### 7.1   `set -x`
	
If we want to script to show every command to print before it is executed, 
then we need to include this  command  at the very beginning of the script ( after the shebang)

ex:
```
#!/bin/bash
set  -x
#list of the scripts to execute
```
### 7.2  `set -e`
				
With use of this command after the shebang, 
the scripts exits immediately after any error or script fails 

ex:
```
#!/bin/bash
set -e
#list of commands to execute
```
### 7.3 Trouble shooting cron by  verifying the logs
```/var/log/syslog```
			
path to find the cron logs for ubuntu/Debian based Linux.

	
	
		
	

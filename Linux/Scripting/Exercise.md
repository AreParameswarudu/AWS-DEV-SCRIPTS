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



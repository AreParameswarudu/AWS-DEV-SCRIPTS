* Launch a server with node-exporter
* another server with prometheus
* connect them as usual

# Creating a custom metrics and exporting it to prometheus

For this we were using {textfile collector} that was present on the node-exporter machine.

The default path for the textfile exporter is, `/var/lib/node_exporter/textfile_collector/`.


1. But the file/directory wont exist unless created, so create the directory, 
```
sudo mkdir -p /var/lib/node_exporter/textfile_collector
sudo chown node_exporter:node_exporter /var/lib/node_exporter/textfile_collector
```

2. Update node exporter service
`vi /etc/systemd/system/node_exporter.service`  

update the `ExecStart` line as follows, 

```
ExecStart=/usr/local/bin/node_exporter \
  --collector.textfile.directory=/var/lib/node_exporter/textfile_collector
```

Restart the node-exporter
```
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl restart node_exporter
```

4. Custom script to export custom metrics.

Objective: To export the no. of ports exposed currently as custom metrics.  

lets create a custom bash/shell file, named as `custom_script.sh` .

```
#!/bin/bash

#count number of listning TCP ports
PORT_COUNT=$(ss -tlun | grep LISTEN | wc -l)

#output it in prometheus formate
echo "server_exposed_ports_gauge $PORT_COUNT" > /var/lib/node_exporter/textfile_collector/ports.prom

```

We need to schedule the script to be ran on defined intervals like for every 1 min and so. For that we are going to use cron job.  


5. Cron job to execute the `custom_script.sh` regularly

Cron tab may not present or exists in some cases,   
so install it, 

```
sudo dnf install cronie

sudo systemctl enable crond
sudo systemctl start crond
```
Create a cron job for our use case, 

```
crontab -e
```

Paste the below line

```
*/1 * * * * /home/custom_script.sh
```

save and exit.


Make the `custom_script.sh` executable, 

`chmod 755 /home/custom_script.sh` 

Once everything is fine, we can see the defined metric in the `node-exporter-IP:9100` or directly on the prometheus by explore or execute setion.



Q: The cron job was not running sucessfully, the `custom-script.sh` had to be ran manually to see the results. why!!
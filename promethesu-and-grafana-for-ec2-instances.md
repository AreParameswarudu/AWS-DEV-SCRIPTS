Monitoring EC2 instances with Promotheus and Grafana
=====================================================


Grafana: For visualizing metrics and logs.  
Loki: For aggregating and storing logs.  
Promtail: agent for logs  
Prometheus: For collecting metrics.  
Logstash: For log processing and forwarding.  


Launch 3 EC2 instance Amazon Linux 2023

Monitoring Server  
Worker-Node1  
Worker-Node2  


Prometheus = 9090  
graphana = 3000  
node exporter = 9100   
loki = 3100/metrics  




Install Prometheus and grafana in main monitoring server
=========================================

The below script will install Promo, Grafana and NodeExporter  

vi promo.sh  and sh promo.sh

```
#prometheus
wget https://github.com/prometheus/prometheus/releases/download/v2.43.0/prometheus-2.43.0.linux-amd64.tar.gz
tar -xf prometheus-2.43.0.linux-amd64.tar.gz
sudo mv prometheus-2.43.0.linux-amd64/prometheus prometheus-2.43.0.linux-amd64/promtool /usr/local/bin

#Now, We need to Create directories for configuration files and other prometheus data.

sudo mkdir /etc/prometheus /var/lib/prometheus
sudo mv prometheus-2.43.0.linux-amd64/console_libraries /etc/prometheus
ls /etc/prometheus
sudo rm -rvf prometheus-2.43.0.linux-amd64*

#sudo vim /etc/hosts
#3.101.56.72  worker-1
#54.193.223.22 worker-2

sudo cat <<EOF | sudo tee /etc/prometheus/prometheus.yml
global:
  scrape_interval: 10s

scrape_configs:
  - job_name: 'prometheus_metrics'
    scrape_interval: 5s
    static_configs:
      - targets: ['localhost:9090']
  - job_name: 'node_exporter_metrics'
    scrape_interval: 5s
    static_configs:
      - targets: ['localhost:9100','worker-1:9100','worker-2:9100']
EOF


sudo useradd -rs /bin/false prometheus
sudo chown -R prometheus: /etc/prometheus /var/lib/prometheus

sudo ls -l /etc/prometheus/
sudo cat <<EOF | tee /etc/systemd/system/prometheus.service
[Unit]
Description=Prometheus
After=network.target

[Service]
User=prometheus
Group=prometheus
Type=simple
ExecStart=/usr/local/bin/prometheus \
    --config.file /etc/prometheus/prometheus.yml \
    --storage.tsdb.path /var/lib/prometheus/ \
    --web.console.templates=/etc/prometheus/consoles \
    --web.console.libraries=/etc/prometheus/console_libraries

[Install]
WantedBy=multi-user.target
EOF

sudo ls -l /etc/systemd/system/prometheus.service
sudo systemctl daemon-reload && sudo systemctl enable prometheus
sudo systemctl start prometheus && sudo systemctl status prometheus --no-pager

#GRAFANA
wget -q -O gpg.key https://rpm.grafana.com/gpg.key
sudo rpm --import gpg.key
sudo cat <<EOF | tee /etc/yum.repos.d/grafana.repo
[grafana]
name=grafana
baseurl=https://rpm.grafana.com
repo_gpgcheck=1
enabled=1
gpgcheck=1
gpgkey=https://rpm.grafana.com/gpg.key
sslverify=1
sslcacert=/etc/pki/tls/certs/ca-bundle.crt
EOF

exclude=*beta*
yum install grafana -y
systemctl start grafana-server.service
systemctl status grafana-server.service
```

Install the node exporter   
-----------------
```
vi node-exporter.sh
```

```
#NODEEXPORTER
wget https://github.com/prometheus/node_exporter/releases/download/v1.5.0/node_exporter-1.5.0.linux-amd64.tar.gz
tar -xf node_exporter-1.5.0.linux-amd64.tar.gz
sudo mv node_exporter-1.5.0.linux-amd64/node_exporter  /usr/local/bin
rm -rv node_exporter-1.5.0.linux-amd64*
sudo useradd -rs /bin/false node_exporter

sudo cat <<EOF | sudo tee /etc/systemd/system/node_exporter.service
[Unit]
Description=Node Exporter
After=network.target

[Service]
User=node_exporter
Group=node_exporter
Type=simple
ExecStart=/usr/local/bin/node_exporter

[Install]
WantedBy=multi-user.target
EOF

sudo cat /etc/systemd/system/node_exporter.service
sudo systemctl daemon-reload  && sudo systemctl enable node_exporter
sudo systemctl start node_exporter.service && sudo systemctl status node_exporter.service --no-pager
```


```http://13.233.215.35:9100``` --> node exporter is working  
```http://13.233.215.35:9090``` --> Promo is working

```http://Ip:3000``` --> Grafana, username: admin, password: admin

Go to Grafana Dashboard --> Add the DataSource --> Select Prometheus and below URL, this URL is same in K8s for all  
`http://13.233.215.35:9090`--> monitoring server Ip, where promo is installed


Import Grafana dashboard --> New --> Import --> 1860 --> load --> select Prometheus --> import   


Add worker-nodes now
===================

Install node-exporter, this is like agent, to collect metrics

```
vi node.sh
```
```
#NODEEXPORTER
wget https://github.com/prometheus/node_exporter/releases/download/v1.5.0/node_exporter-1.5.0.linux-amd64.tar.gz
tar -xf node_exporter-1.5.0.linux-amd64.tar.gz
sudo mv node_exporter-1.5.0.linux-amd64/node_exporter  /usr/local/bin
rm -rv node_exporter-1.5.0.linux-amd64*
sudo useradd -rs /bin/false node_exporter

sudo cat <<EOF | sudo tee /etc/systemd/system/node_exporter.service
[Unit]
Description=Node Exporter
After=network.target

[Service]
User=node_exporter
Group=node_exporter
Type=simple
ExecStart=/usr/local/bin/node_exporter

[Install]
WantedBy=multi-user.target
EOF

sudo cat /etc/systemd/system/node_exporter.service
sudo systemctl daemon-reload  && sudo systemctl enable node_exporter
sudo systemctl start node_exporter.service && sudo systemctl status node_exporter.service --no-pager
```

Go to `http://13.233.215.35:9090/` --> prometheus ---> at top navibar --> Status --> Targets , worker nodes are down. 

go to monitoring server.

`cat /etc/prometheus/prometheus.yml`  --- this contains, workernode names, to add , go to `/etc/hosts` and add workernode IP's  

```
vi /etc/hosts
```

13.127.130.98 worker-1  
3.6.41.159 worker-2  

<img width="723" height="157" alt="image" src="https://github.com/user-attachments/assets/82ed605f-2627-4395-8f8c-41ab034a819c" />


Go to prometheus UI and to the target section, and refresh the page.  
`http://13.233.215.35:9090/targets?search=` ---> refresh and nodes are up

now monitor these through Grafana.    
`http://3.233.215.35:3000/`--> Make sure dashboard is there --> top --> Host --> DropDown -- see workernodes


LOG Monitoring with Loki and Promtail
=====================================

Setup Loki and Promtail on Docker to save money ;-)

Install docker and start
------------------------
yum install -y docker  
systemctl start docker


Create a directory for Grafana configs
----------------------------------
sudo mkdir grafana_configs  
cd grafana_configs


# Download Loki Config
-----------------------
sudo wget https://raw.githubusercontent.com/grafana/loki/v2.8.0/cmd/loki/loki-local-config.yaml -O loki-config.yaml

# Download Promtail Config
----------------------------
sudo wget https://raw.githubusercontent.com/grafana/loki/v2.8.0/clients/cmd/promtail/promtail-docker-config.yaml -O promtail-config.yaml


# Run Loki with Docker
-----------------------
docker run -d --name loki -v $(pwd):/mnt/config -p 3100:3100 grafana/loki:2.8.0 --config.file=/mnt/config/loki-config.yaml

Check the status using http://your-ec2-instance-ip:3100/metrics

Check the status using http://your-ec2-instance-ip:3100/ready


#RUN Run Promtail with docker
-----------------------------

docker run -d --name promtail -v $(pwd):/mnt/config -v /var/log:/var/log --link loki grafana/promtail:2.8.0 --config.file=/mnt/config/promtail-config.yaml


Link Loki to Grafana
----------------------
· In Grafana, navigate to Configuration > Data Sources.

· Add a new data source and select Loki.

· Enter the Loki URL (http://ec2-public:3100) and save the configuration.

Now, our datasource is connected.

Link Loki to Grafana

· In Grafana, navigate to Configuration > Data Sources.

· Add a new data source and select Loki.

· Enter the Loki URL (http://localhost:3100) and save the configuration.

Now, our datasource is connected



Step 9 — Explore and filter logs
--------------------------------

· Use the Explore tab in Grafana to view logs.

· Select the Loki data source , label filters = jobs, varlogs --> run query

Show Grafana logs
------------------

· Add the Grafana logs path (/var/logs/grafana) to the Promtail config file

vi promtail-config.yaml


```
  - targets:
      - localhost
    labels:
       job: grafanalogs
     __path__: /var/log/grafana/*log
```

-- docker ps  
-- sudo docker restart promtail-container-id

Go to Grafana --> Dashboard --> New Dashboard --> Add Visualization --> DataSOurce = Grafana --> click Query inspector --> Refresh
Select Loki as datasource --> 


ALERTS
=====

browser -- > my google account > security -- > two setp verification --> App passwords copy password


    vi /etc/grafana/grafana.ini line 892/1034
    [smtp]
    enabled = true
    host = smtp.gmail.com:587
    user = trainerreyaz@gmail.com
    # If the password contains #or; you have to wrap it with triple quotes. Ex """#pa 897 password=xhfa drlb zgwm ogey
    cert_file =
    ;key_file =
    skip_verify = true
    from_address = trainerreyaz@gmail.com 
    from_name = Grafana



systemctl restart grafana-server.service  
systemctl status grafana-server.service



Grafana --> Alert Rule --> contact point -- > Create --> name -- > email -- > test --> check gmail  

Alerting rules --> new -- > set -- > name: Grafana -- > Metric: node_cpu_seconds_total --> instace > localhost:9100-->  

Input: A & Function: Last & Mode: Stric   
Input: B & isabove: 0.7 (70%)  
Folder: cpu  
Evaluation group: cpu  
Pending period: 30s  


amazon-linux-extras install epel -y  
yum install -y stress  
run stress command  

# KUBERNETES:

K8S is an open-sourced  platform for automating the deployment, scaling and operation of containerized application.
K8S is a native docker orchestrating tool to work with multiple containers and managing multiple nodes.
With K8S, we can achieve auto scaling
			  we can associate a Load Balancer to expose the container services to customers using URLs.

| **Docker-Swarm**  | **K8S** |
| ------------- | ------------- |
| Cluster       |   Cluster  |
| Nodes  |   Nodes  |
| Containers  |   Pods  |
| Service/Application  |   Containers  |
|   |   Service?application  |
	
In K8S, the elemental level objects that K8S have control is PODS.
meaning, K8S don't really work on container level, they don't care/know about containers. All they work on is PODS.
we can treat PODS as containers for analogy.

	
Kubernetes Architecture:
--------------------------------
With a cluster in K8S, we have two kinds of nodes
  1. Master node/ control plane
  2. Worker node

___**Master node:**___   
  Its primary work is to,  
  * manage the worker nodes,   
  * assign them the work that we desire,   
  * keep the record of meta data ( in Json format).  


___**Slave node/Worker node /Minion:**___
  * PODS ( in which containers run) are present in the worker node.  
  * Does the actual work of running containers.  

A single cluster can have Multiple Worker nodes but mostly 1 Master node.  


<img width="1041" height="813" alt="image" src="https://github.com/user-attachments/assets/d56ab9d3-84c2-4d19-a574-246082037850" />


------------------
	
_**Kubectl**_ :  
DevOps Eng. connects to the K8S cluster using the tool. 
Used to write commands to work with K8S.  
Kubectl is the command line tool for Kubernetes

## MASTER Node:

  1. _**API server**_ : 
      The first line of interaction with k8S. (Entry point for all REST commands used to control cluster.)
             All the commands are reached to Kubeapi server.
      
  2. _**Schedular**_ : 
      This component work is to ASSIGN the no. of  pods to the node based on resource availability and other constrains.
      This will communicate with Nodes.

  3. _**ETCD**_ : 
      This component is like Database, to store the clusters data.
            Data is stored in JSON format ( Key : Value ).
      Data ---> Configuration data, Cluset data, state info, meta data.

  4. _**Controller Manager**_ : 
      This component runs various controllers that regulate the state of the cluster.
      Node controllers, Replication controller, and more.

  5. Cloud Controller manage:

## Worker Node:

  1. _**Kubelet**_ : 
      Agent that runs on every worker node.
      Ensures that containers are running in the PODS as defined.
      Worker nodes talk to master node(API server) through Kubelet and manages the lifecycle of containers on its node.

  2. _**PODS**_ : 
      Smallest and simplest K8S objects. 
      POD represents the single instance of running process in cluster.
      contains container ( one or many).

  3. _**Container runtime**_ :
      Software responsible for running containers.	
      Most common runtime is docker, but supports others like CONTAINERD, CRI-O.
    
      Pulls image from reg. , unpacks them, run as containers.
  
  4. _**Kube-Proxy**_ : 
      Is a network proxy that runs on each worker node.
      Maintains the network rules.
      It is responsible for assigning the Ports to the containers.


## Key Network Components:

  1. _**Cluster Ips**_ :  
      An internal Ip address that is assigned to  service within cluster.

  2. _**Node Ports**_ :
      Expose a service on a static port on each nodes Ip.

  3. _**Load balancer**_ :
      Provisions a load balancer in supported cloud env to expose service externally.


## Volumes:  
  Persistent storage to containers with in pods, allowing data to persist across pod restarts.  
  They can be backed by various storage backends, include local storage, cloud storages like AWS EBS etc.

## Name space:  
  Context: Even when having different ENVs like dev, pre-prod, prods, we only use 1 cluster for all of it.  
            maintaining different clusters cost much.  
  In such cases, Name space is the means to differentiate the resources, PODS, container for different ENVs.

	
## Cluster Types:
  1. _**Self managed**_  
  * minikube = single node cluster
  * kubeadm = multi node cluster (manual)
  * kops = multi-node cluster (automation)

  2. _**Cloud managed**_
  * AWS = EKS = ELASTIC KUBERNETES SERVICE
  * AZURE = AKS = AZURE KUBERENETS SERVICE
  * GOOGLE = GKS = GOOGLE KUBERENETS SERVICE



--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Minikube Setup

Requirement  
Launch an EC2 instance with Ubuntu and t2.small having min 10GB volume.

Install minikube and Kubectl

 ``` vi minikube.sh ```
```
sudo apt update -y
sudo apt upgrade -y
sudo apt install curl wget apt-transport-https -y
sudo curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo mv minikube-linux-amd64 /usr/local/bin/minikube
sudo chmod +x /usr/local/bin/minikube
sudo minikube version
sudo curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl&quot;
sudo curl -LO "https://dl.k8s.io/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl.sha256&quot;
sudo echo "$(cat kubectl.sha256) kubectl" | sha256sum --check
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
sudo minikube start --driver=docker --force
```


KUBECTL:
--------
kubectl is the CLI which is used to interact with a Kubernetes cluster.  

We can create, manage pods, services, deployments, and other resources.  

The configuration of kubectl is in the $HOME/.kube directory.  

`minikube status`  

`kubectl get nodes`  

`kubectl get pods`

## 1. PODS :
It is a smallest unit of deployment in K8's.  
It is a group of containers.  
Pods are ephemeral (short living objects)  
Mostly we can use single container inside a pod but if we required, we can create multiple containers inside a same pod.  
when we create a pod, containers inside pods can share the same network namespace, and can share the same storage volumes.  
While creating pod, we must specify the image, along with any necessary configuration and resource limits.  
K8's cannot communicate with containers, they can communicate with only pods.   

We can create this pod in two ways,  
	1. Imperative(command)  
	2. Declarative (Manifest file) - can be reuse - in real time we go with declarative
 
By default, one pod has one container, if required we can create, if you create multiple containers in a single pod, all containers inside the pods will share the same volume


### 1.1. Imperative(command)
  ``` kubectl run pod1 --image nginx ```   [Creating  pod with name pod1 with image nginx]

  ```kubectl get pods```          [To get the pods , can use pods/po/pods also]

  ```kubectl get pod -o wide```           [To get details about the pod]

  ```kubectl describe pod pod1```        [Describe is specific command so need to mention pod_name, to get more details about the pod]

  ```kubectl delete pod pod1```         [Delete is also specific, so need to mention podname as well, to delete the pod]

  ```kubectl logs pod1```              [Logs command only works on PODS (pods centric command), and need to mention pod_name as well.]

  ```kubectl exec -it pod1 -- /bin/bash```   [to connect to the pod1 inside]
  ```cd /usr/share/nginx/html```  
  ```cat index.html```    

```kubectl delete pod pod1```        [This will delete the pod named pod1]
   
The above approach is not advised, because don't create PODS manually , declarative approach is preffered all the time.

### 1.2. Declarative (Manifest file)
In manifest file we have these mandatory parameters  

```
apiVersion:
kind:
metadata:
spec:
```

  1.2.1. What is apiVersion?
  -------------------
  apiVersion: 
        * Specifies the API version used for the Deployment object. apps/v1 is the stable API version for managing deployments.
        * Depending on Kubernetes object we want to create, there is a corresponding  code library we want to use.
      apiVersion refers to Code Library
```
POD : v1
Service: v1
NameSpace: v1
Secrets: v1
Replicaset: apps/v1
Deployment: apps/v1
jobs: batch/v1
```

  ``` kubectl api-versions```   -->to get api versions


  1.2.2. What is kind ?
  --------------
  Refers to Kubernetes object which we want to create.
```
kind: Pod
kind: Deployment
kind: Service
kind: Ingress
kind: job
```
  1.2.3. What is metadata?
  ----------------
  Additional information about the Kubernetes object like name, labels etc  

  _name_ : The name of the Deployment.  
  _labels_ : Key-value pairs used for organizing and selecting objects


  1.2.4. What is spec?
  ------------
  Contains docker container related information like, image name, environment variables , port mapping etc

  How many number of pods (Replica)  
  About container and that should run on which image  
  On which port it should expose  
  Labeling the entire deployment etc  

### Sample manifest file template.
```
apiVersion: v1
kind: Pod  -- creating pod
metadata:
name: pod1 -- name of the pod
spec:  -- specifications
containers:
  - image: nginx  -- image  name
  name: cont1 -- container name
```
Create one using above template.
  ```vi pod.yml```
```
apiVersion: v1
kind: Pod
metadata:
name: pod1
spec:
containers:
  - image: nginx
  name: cont1
```

```kubectl create -f pod.yml```    [ To create a pod using manifest]
```kubectl get pods -o wide```     [ To get more details about pods]

```kubectl describe pod pod1```    [ To describe a specific pod ]

```kubectl delete pod pod1```      [ To delete the pod ]

DRAWBACK: once pod is deleted we can't retrieve the pod.
---------
If any pod deleted, it is deleted, no HA, for HA use ReplicaSET also called RS

(Additional/optionals)
		KUBECOLOR:
```
wget https://github.com/hidetatz/kubecolor/releases/download/v0.0.25/kubecolor_0.0.25_Linux_x86_64.tar.gz
tar -zxvf kubecolor_0.0.25_Linux_x86_64.tar.gz
./kubecolor
chmod +x kubecolor
mv kubecolor /usr/local/bin/
```

```kubecolor get po```

```kubectl create -f pod.yml```

```kubecolor get po```

------------------------------------------------------------------------------------
  
_Problem with using or defining only pods:_

  If any pod deleted, it is deleted, no HA, for HA use ReplicaSET also called RS  
  To achieve High availability ( Slef or auto healing ) we use REPLICASETs over PODS.  
  
-------------------------------------------------------------------------------------

## REPLICASET

This is used for managing multiple replicas of pod to perform activities like load balancing and autoscaling

Setup minikube with ubuntu 24 as per installation process

It will create replicas of same pod.

we can use same application with multiple pods.

Even if one pod is deleted automatically it will create another pod. It has self healing mechanism

Depends on requirement we can scale the pods.

We create rs --> rs wil create pods

LABELS:
-------

As we are creating multiple pods with same application, all these pods have different names but how to group all of them as we have 1 application with multiple pods. So we can give a label to group them  

Individual pods are difficult to manage because they have different names  
so we can give a common label to group them and work with them together

SELECTOR
--------

It is used to select pods with same labels  

For replicaset use apiversion as apps/v1  

how to find the apiresources to write in manifest file  


Template:  
```
apiVersion: apps/v1
kind: ReplicaSet
metadata:
name: ib-rs    ---------- Name of the Replicaset
labels:
	app: bank
spec:     ------------- this spec is for PODS
replicas: 3   --------- how many number of pods
selector:
	matchLabels:  -Ensures only pods with label app: bank are part of this Replicaset. if there is any pod with label bank, it will be a part of this replicaset
	app: bank
template:            ------------ Ensures the pods get labeled as app: bank
	metadata:
	labels:
		app: bank
	spec:  ----------------- this spec is for containers
	containers:
	- name: cont1
		image: trainerreyaz/ib-image:latest
```


```
apiVersion: apps/v1
kind: ReplicaSet
metadata:
name: ib-rs
labels:
	app: bank
spec:
replicas: 3
selector:
	matchLabels:
	app: bank
template:  
	metadata:
	labels:
		app: bank
	spec:  
	containers:
	- name: cont1
		image: trainerreyaz/ib-image:latest
```


```kubectl create -f replicaset.yml```		# to run the replicaset inorder to creats pods with desired replicas.

```kubectl get replicaset```				# to list the replicasets
		(or)
  ```kubectl get rs```

```kubectl get rs -o wide``` 				# [This command will get more details about ReplciaSets]

```kubectl describe rs ib-rs```  			# [This will describe about internetbanking-rs ]

```kubectl get pods```

```kubectl get pods --show-labels```   		# [This will list the pods with Labels]



If you delete any pod, automatically new pod will be created, if you want to watch live, open another terminate and give.

		> kubectl get pods --watch

		> kubectl get pods

		> kubectl delete pods pod-id      [First new pod create and the existing pod will be deleted]

		> kubectl get pods --show-labels  [New pod got created, this is called ReplicaSet, if one pod delete , another pod will get created automatically]

		> kubectl get pods -l app=bank  [This will list all the pods with label bank, l = label]

		> kubectl delete pods -l app=bank  [To delete all the pods wit label bank]

		Note: Replicaset will take image details from manifest file -- replicaset.yml
---------------------------

SCALE REPLICAS - Scale Out and Scale In
-----------

Scale Out
--------
First open anotherwindows live

> kubectl get pods --watch
> kubectl get rs   							#[To list the replicasets]
> kubectl scale rs/ib-rs --replicas=10  	#[Now see pods creating live]

Scale In
--------
	> kubectl scale rs/ib-rs --replicas=5  [Now see pods creating live]

	LIFO: LAST IN FIRST OUT.
	IF A POD IS CREATED LASTLY IT WILL DELETE FIRST WHEN SCALE IN

[!Note]: This Scale out and in is manual, later we learn how to automate.


Roll out concept:  (wont work with replicasets object kinds)
-----------------
	Now, all pods are running with ib-image:latest image , but if i want to change the image to mobilebanking and update the POD, not possible in ReplicaSet

	> kubectl describe pod -l app=bank | grep -i ID   [ALl pods are using ib-image:latest]

	Update the image in the replicaset, you cannot update in yml file, it will create a new replicaSet so there is a command to edit current replicaset

	> kubectl edit rs/ib-rs    [change internetbankingrepo to insurance]

	> kubectl describe pod -l app=bank | grep -i ID  [Still it shows internetbanking, image is not change , that's the problem with Replica SET, We cannot update the application]


	vi replicaset.yml  -- change to insurance

	> kubectl apply -f replicaset.yml    [This will give error that ib-rs already exits. So need to create a new RS again]

	> kubectl get pods --show-labels

	> kubectl describe pod -l app=bank | grep -i ID   [you still see old image internetbanking ]

	But if you scale out, new pods will contains insurance repo

	> kubectl scale rs/ib-rs --replicas=5
	> kubectl describe pod -l app=bank | grep -i ID  [you see mobilebanking . only new image are insurance.
													This is the drawback of replicaset]

	Using ReplicaSet we cannot roll out the application

	Advantage
		--> self healing
		--> scaling

	Drawbacks
		--> we cannot roll in and roll out, we cant update the applications using ReplicaSet, lets use DEPLOYMENT

	rs ---> pods

	> kubectl delete rs ib-rs

 
Initial version of ReplicaSET:
-----------------------------
	ReplicationController:
	=======================

		Same as ReplicaSet. It also used for handling multiple replicas of specific pod. But it doesn't contain selector and its child field matchField. matchField where it will search for pods based on a specific label name and adds them to Cluster
																									

		Kind : ReplicationController

	This below code doesn't contain matchLabels Field
	******************************************

		apiVersion: apps/v1
		kind: ReplicationController
		metadata:
		name: ib-rs
		labels:
			app: bank
		spec:
		replicas: 3
		template:  
			metadata:
			labels:
				app: bank
			spec:  
			containers:
			- name: cont1
				image: trainerreyaz/ib-image:latest


	Replication Controller
	---------------------

		The Replication Controller is the original form of replication in Kubernetes

		The Replication Controller uses equality-based selectors to manage the pods.

		The rolling-update command works with Replication Controllers

		Replica Controller is deprecated and replaced by ReplicaSets.

	Replica Set  
	------------

		ReplicaSets are a higher-level API that gives the ability to easily run multiple instances of a given pod

		ReplicaSets Controller uses set-based selectors to manage the pods.

		The rolling-update command won’t work with ReplicaSets.

		Deployments are recommended over ReplicaSets.

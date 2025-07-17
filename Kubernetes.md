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

# Single Node (Minikube) Setup

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

# 1. PODS :
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

 #### 1.2.1. What is apiVersion?
  
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


 #### 1.2.2. What is kind ?
  
  Refers to Kubernetes object which we want to create.
```
kind: Pod
kind: Deployment
kind: Service
kind: Ingress
kind: job
```
 #### 1.2.3. What is metadata?
  
  Additional information about the Kubernetes object like name, labels etc  

  _name_ : The name of the Deployment.  
  _labels_ : Key-value pairs used for organizing and selecting objects


 #### 1.2.4. What is spec?
  
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

# 2. REPLICASET :

This is used for managing multiple replicas of pod to perform activities like load balancing and autoscaling

Setup minikube with ubuntu 24 as per installation process

It will create replicas of same pod.

we can use same application with multiple pods.

Even if one pod is deleted automatically it will create another pod. It has self healing mechanism

Depends on requirement we can scale the pods.

_**Working flow:**_ :  
Create replica sets, replicasets will take care of the pods, pods will take care of the containers.  
i.e. Replicasets ----> Pods -----> Containers.

### 2.1 LABELS:


As we are creating multiple pods with same application, all these pods have different names but how to group all of them as we have 1 application with multiple pods. So we can give a label to group them  

Individual pods are difficult to manage because they have different names  
so we can give a common label to group them and work with them together

### 2.2 SELECTOR


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



If you delete any pod, automatically new pod will be created, if you want to watch live, open aother duplicat terminal 

```kubectl get pods --watch```  --> run this on duplicate terminal and watch this everytime you perform any operations/actions.

In the original terminal, 

```kubectl get pods```

```kubectl delete pods pod-id```      [First new pod create and the existing pod will be deleted]

```kubectl get pods --show-labels``` [New pod got created, this is called ReplicaSet, if one pod delete , another pod will get created automatically]

```kubectl get pods -l app=bank```  [This will list all the pods with label bank, l = label]

```kubectl delete pods -l app=bank```  [To delete all the pods wit label bank]

> [!NOTE]
> Replicaset will take image details from manifest file -- replicaset.yml.

----------------------------------

### 2.3 SCALE REPLICAS :

* Scale Out   
``` kubectl get pods --watch```   ---> Do this in another terminal for watch.  
```kubectl get rs```  				#[To list the replicasets]  
```kubectl scale rs/ib-rs --replicas=10```  	#[Now see pods creating live]  

* Scale In  
```kubectl scale rs/ib-rs --replicas=5```  [Now see pods creating live]  

_LIFO: LAST IN FIRST OUT.    
IF A POD IS CREATED LASTLY IT WILL DELETE FIRST WHEN SCALE IN_

> [!NOTE]
> This Scale out and in is manual, later we learn how to automate.


### 2.4 Roll out concept:  (wont work with replicasets object kinds)

Lets say that I have a _manifist.yml_ file that was defined to use nginx image.  
But now we need to update it to apache2 iamge.  
There are 2 ways we can think of doing this.  
	1. Edit the _manistfist.yml_ file directly, and re-run the file. This will throws and error saying the object already exist. (NOT RECOMMENDED).    
 	2. To edit the replica (not .yml file).    
  	```kubectl edit rs/ib-rs```  ---> command to edit the ib-rs replicaset (not .yml file).     
   	we can edit it as needed and save it. This is the **recommended way** as it wont give any errors.    

But the actual issue of image update will not reflected on the pods. Even if we scale out the replica set, the new pods will contain the same old image.  

So with REPLICA SETS,   
_**Advantage**_  
	* self healing  
	* scaling  
_**Drawbacks**_:  
	* we cannot roll in and roll out, we cant update the applications using ReplicaSet, lets use DEPLOYMENT  
_**Working flow:**_ :  
	Create replica sets, replicasets will take care of the pods, pods will take care of the containers.  
	i.e. Replicasets ----> Pods -----> Containers.

-------------------------------------------------------------------------------------------------------------------

### Optional / For knowledge:
2.5 Initial version of ReplicaSET  = ReplicationController :  
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


-----------------------------------------------------------------------------------------------------------------------------

# 3. Deployment

Kubernetes deployment is a high-level resource object by which you can manage the deployment and scaling of the applications while maintaining the desired state of the application. You can scale the containers with the help of Kubernetes deployment up and down depending on the incoming traffic.   
If you have performed any rolling updates with the help of deployment and after some time if you find any bugs in it then you can perform rollback also. Kubernetes deployments are deployed with the help of CLI like Kubectl it can be installed on any platform.  

Working strategy: Create deployments, deployments take care of replica sets, replica-sets take are of PODS and PODS  will take care of Containers.  
i.e. Deployments ----> Replica sets ----> PODS ----> Containers

So on the whole,   
	we mostly works on the deployment layer as it can take care of the layers under it

The manifest.yml file is as similar as for replicasets, the only major difference is that we mention kind as deployment rather than replicaset.  
Just change  "kind: Deployment" and "name: ib-deployment"

Create a manifist file with name deployment.yml
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ib-deployment
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

```kubectl create -f deployment.yml``` [To run the manifist file named as deployment.yml]

```kubectl get deploy```   or  ```kubectl get deployments```

```kubectl get deploy -o wide```

```kubectl get rs```  [As the deployment also creates replica sets, to list that replicasets].

```kubectl describe deploy ib-deployment```

```kubectl get pods```

Now lets scale out and Scale IN  

### Scale Out

```kubectl scale deploy/ib-deployment --replicas=10```  
```kubectl get pods```  [Check the no.of pods].


### Scale In

```kubectl scale deploy/ib-deployment --replicas=5```   
```kubectl get pods```  

What ever Replica set is doing Deployment is also doing the same thing

if you delete any pod, it will create immediately automatically
```kubectl get pods```  
```kubectl delete pod pod-id```  
```kubectl describe pod -l app=bank | grep -i ID```  
(or)  
```kubectl describe pods | grep -i image```   [It shows all internetbankingrepo image]  

***************** Now what Deployment do additional thing is to change the application ***************

First watch pods in another terminal  
```kubectl get po --watch```  

```kubectl edit deploy/ib-deployment```   [Edit the deployment object to use another image]    

watch pods in another terminal , first it will create a new pods and then terminate old ones
```kubectl describe pods | grep -i image``` [you can see now mobilebanking image]  

kubectl get events --sort-by=.metadata.creationTimestamp  



### 3.1 RollOut Few commands

```kubectl rollout history deploy/ib-deployment```

```kubectl rollout undo deploy/ib-deployment```   [It will go back to previous application / image ]

```kubectl get pods```  [Pods are terminating and creating new pods with new image, this was not possible in ReplicaSet]

```kubectl describe pods | grep -i image```

```kubectl rollout pause deploy/ib-deployment```  --- it is like lock, cannot undo, cannot rollout to previous

```kubectl rollout undo deploy/ib-deployment```  -- not possible

```kubectl rollout resume deploy/ib-deployment```

```kubectl rollout undo deploy/ib-deployment``` -- now possible

```kubectl rollout status deploy/ib-deployment```


### 3.2 Deployment has 2 Strategies:  

* _Rolling update_: This is **Default**, When you update the application, Rolling update will delete one pod and create . One by one
* _Recreate_: Delete all pods and create again- Downtime. Not recommended
* _Blue-Green Deployment_: 🟦 Blue = old version, 🟩 Green = new version, Switch traffic only when the new version is fully ready
* _Canary Deployment_:  Roll out new version to a small set of users, then gradually increase.

Out of these, Rolloing and Recreating were Kubernetes native, meaning that K8S will do that without manual intermention.  
While Blue-Green and Canary deployments require manual work.

Example: see strategy: Recreate

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ib-deployment
  labels:
    app: bank
spec:
  replicas: 3
  strategy:
    type: Recreate
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
If you want port to expose , use below code
```
spec:
containers:
- name: cont1
image: trainerreyaz/ib-image:latest
ports:
- containerPort: 8080   # Port inside the container
  hostPort: 8080        # Port on the host machine
```

🔹 Explanation of Changes
---------------------------
✅ containerPort: 8080 → The app runs inside the container on port 8080.  
✅ hostPort: 8080 → The container maps its 8080 port to the same port on the host machine.  

🔹 Important Notes on hostPort
----------------------------------
hostPort directly binds the container port to the host.  
It works only on worker nodes where the pod runs.  
If multiple pods run on the same node, you cannot use the same hostPort for all of them.  
Recommended alternative: Instead of hostPort, use a Kubernetes Service (NodePort or LoadBalancer) to expose the Deployment.  
------------------------

By default, a ReplicaSet (RS) only ensures that a specific number of Pods are running. However, it does not provide network access to those Pods externally.

✅ To access your application from the internet, you need a Kubernetes Service.

**Example files for exercise:**
---------------------------

*1.🚀 Kubernetes Manifest: 1 Pod with 2 Containers*  
In Kubernetes, a Pod can run multiple containers that share the same network and storage. Here’s how to create a single Pod with two containers inside it.

`vi pod-two-containers.yaml`
```
apiVersion: v1
kind: Pod
metadata:
  name: two-container-pod
  labels:
    app: multi-container
spec:
  containers:
  - name: nginx-container
    image: nginx
    ports:
    - containerPort: 80
  - name: busybox-container
    image: busybox
    command: ["sh", "-c", "while true; do echo 'Hello from BusyBox'; sleep 10; done"]
```


**-c:** Tells sh to execute the following string command

```kubectl apply -f pod-two-containers.yaml```

```kubectl get pods```    [we get single pod but 2/2 meaning, 2 containers]

```kubectl logs two-container-pod -c busybox-container```

```kubectl logs two-container-pod -c nginx-container```

```kubectl exec -it two-container-pod -c nginx-container -- sh```       [-c: container]

   `cd /usr/share/nginx/html`

```kubectl exec -it two-container-pod -c busybox-container -- sh```
   `ls`



# 4. Kubernetes JOBS:
   
Kubernetes Jobs are resources used to run batch tasks in a Kubernetes cluster.   
They ensure that a specified number of Pods successfully complete a task before marking the Job as done.   
Jobs are crucial for executing one-time or recurring tasks, such as data migrations, backups, or batch processing.  

### 4.1 Types of Kubernetes Jobs:

#### 4.1.1 Non-parallel Jobs:

These Jobs execute tasks sequentially /one by one, with only one Pod started unless it fails.   
The Job completes as soon as its Pod terminates successfully.   
It has completions parameter, Like _completions: 3_. The Job completes only when 3 Pods have successfully run

#### 4.1.2 Parallel Jobs with a Fixed Completion Count:

In these Jobs, multiple Pods run simultaneously to complete a task.  
The Job is considered complete when a specified number of Pods successfully complete their tasks.  
It has completions and Parallelism.
  _completions: 6
  parallelism: 3_

In the above example three pods are executing at a time, since we mentioned Parallelism = 3, so once the three pods are completed their tasks then next three will start execution.


#### 4.1.3 Parallel Jobs with a Work Queue:

These Jobs dynamically scale Pods based on workload.  
Pods coordinate with each other or external services to fetch and process tasks from a shared queue.

 **_Real-world Use Cases_**: 
	* _Non-parallel Jobs_: Running one-time administrative tasks, such as database migrations or system updates.
	* _Parallel Jobs with a Fixed Completion Count_: Processing large datasets, where data is split into chunks and processed concurrently by multiple Pods.
	* _Parallel Jobs with a Work Queue:_ Handling variable workloads, such as incoming requests in a web application, where Pods scale dynamically based on demand.

```
vi nonparallel.yml

apiVersion: batch/v1
kind: Job
metadata:
  name: non-parallel-job
spec:
  template:
    metadata:
      name: non-parallel-pod
    spec:
      containers:
      - name: non-parallel-container
        image: busybox
        command: ["echo", "Hello from the non-parallel job"]
      restartPolicy: Never
  completions: 3
```

_busybox:_ BusyBox is a single executable that bundles multiple Unix utilities (like sh, ls, cat, echo, wget, grep, etc.). It is widely used in minimal containers because of its small size (~1MB) and fast startup time.

_completions: 3_ → The Job completes only when 3 Pods have successfully run.

--> _restartPolicy_: Always, OnFailure, Never

| Header 1     	| Explanation    	|	Usage    |
| ------------ 	| ----------------------|----------------|
| Always 	|  Always restarts the container if it exits|Default for Deployments & ReplicaSets |
| OnFailure 	|Restarts the container only if it exits with an error (non-zero exit code).| Jobs & CronJobs |
|   Never       |Never restarts the container, even if it fails. | Jobs & CronJobs (One-time execution) |                                     

```kubectl apply -f nonparallel.yml```

```kubectl get pods```

```kubectl get jobs```

```kubectl logs -l job-name=non-parallel-job```

```kubectl logs podname```     Ex: kubectl logs non-parallel-job-2vvf9

```kubectl delete job jobname```

In above example the pods are executing one by one.


#### 4.1.4 Parallel Jobs with a Fixed Completion Count: 

Use the below simple manifest file for testing Parallel Jobs with a Fixed Completion Count jobs:

`vi parallelfixed.yml`
```
apiVersion: batch/v1
kind: Job
metadata:
  name: parallel-fixed-count-job
spec:
  template:
    metadata:
      name: parallel-fixed-count-pod
    spec:
      containers:
      - name: parallel-fixed-count-container
        image: busybox
        command: ["echo", "Hello from the parallel-fixed-count job"]
      restartPolicy: Never
  completions: 6
  parallelism: 3
```

_completions: 6 _→ The Job completes only when 6 Pods have successfully run.
_parallelism: 3_ → Runs 3 Pods at the same time.


```kubectl apply -f parallelfixed.yml```

```kubectl get pods```

```kubectl get jobs```

```kubectl logs -l job-name=<job-name>```

```kubectl logs parallel-job-2vvf9```	parallel-job-2vvf9 = Pod-name of one of my pods.

```kubectl delete job jobname```

In the above example three pods are executing at a time, since we mentioned Parallelism = 3, so once the three pods are completed their tasks then next three will start execution.

#### 4.1.5 Parallel Jobs with a Work Queue 

Use the below simple manifest file for testing Parallel Jobs with a Work Queue jobs:

`vi parallel-work-queue-job.yaml`
```
apiVersion: batch/v1
kind: Job
metadata:
  name: parallel-work-queue-job
spec:
  template:
    metadata:
      name: parallel-work-queue-pod
    spec:
      containers:
      - name: parallel-work-queue-container
        image: busybox
        command: ["echo", "Hello from the parallel-work-queue job"]
      restartPolicy: Never
  parallelism: 3
```

```kubectl apply -f parallel-work-queue-job.yaml```

```kubectl get pods```

In the above example 3 pods are started executing at a time since we mentioned Parallelism = 3 and we didn’t mention any specified number of Completions.
                           

# 5. 🚀 Kubernetes CronJob Example

A Kubernetes CronJob is used to schedule jobs to run at specific times, just like a Linux cron job. It is useful for tasks such as backups, periodic data processing, or sending scheduled reports.

This CronJob prints "Hello from Kubernetes!" every minute.

`vi cron.yml`
```
apiVersion: batch/v1
kind: CronJob
metadata:
  name: hello-cronjob
spec:
  schedule: "*/1 * * * *"  # Runs every minute
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: hello-container
            image: busybox
            command: ["sh", "-c", "echo Hello from Kubernetes!"]
          restartPolicy: Never  # Ensure job runs only once per schedule
```

```kubectl apply -f cron.yaml```

```kubectl get cronjobs```

```kubectl describe cronjob cron```


🔹 View Logs of Last Run
---------------------------

```kubectl get pods```  # Get the latest pod name

```kubectl logs <POD_NAME>```

```kubectl get cronjob```

```kubectl delete cronjob```

#  Lets setup a multi node cluster 
> [!NOTE]
> This multi node cluster setup using AWS instances will cost.


For single node cluster ==> MiniKube.    
For multi node cluster ==> KOPS.  

We have several options for mutinode cluster, lets go with KOPS.

Go to AWS ec2 console,   
	* Choose a t2.micro instance with Amazon Linux OS.  
 	* Attach an IAM role with trusted entity = EC2, and Permissions = Administrative permissions.
create instance.

--------------
> [!NOTE]
> Use of IAM role:  
> As this EC2 instance is going to create a cluster of a Master node and desired no. of worker nodes, and need to talk to the nodes in the cluster. so unless we have an IAM role with required permission, we cannot do that.  
> The permission for IAM role can be fined tuned.  
> The resources that this role going to create were, _Ec2 instances_, _dedicated VPC_, _ig = Instance group_, _CIDER block_.
>
> As Amazon Linux machine inherently contains Amazon CLI, we no need to install it additionaly.
--------------

Login to the instance, now settup the KOPS and Kubectl in this machine.

`sudo -s`   --> To elivate the permission to root user.    
`hostnamectl set-hostname kops`   --> set hostname for machine.    
`sudo -i`     --> Reflect the changes.  

`vi .bashrc`    --> to edit the .bachrc file and add a path.  
`export PATH=$PATH:/usr/local/bin/`  --> add this pathe in the file.  

`source .bashrc`    ---> to reflect changes /compile the edit.  

Now lets add a kops.sh file and run it to install kops, kubectl.

`vi kops.sh`     --> create a shell script.  

```
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl&quot;
wget https://github.com/kubernetes/kops/releases/download/v1.32.0/kops-linux-amd64
chmod +x kops-linux-amd64 kubectl
mv kubectl /usr/local/bin/kubectl
mv kops-linux-amd64 /usr/local/bin/kops
aws s3api create-bucket --bucket param-kops-testbkt143.k8s.local --region ap-south-1 --create-bucket-configuration LocationConstraint=ap-south-1
aws s3api put-bucket-versioning --bucket param-kops-testbkt143.k8s.local --region ap-south-1 --versioning-configuration Status=Enabled
export KOPS_STATE_STORE=s3://param-kops-testbkt143.k8s.local
kops create cluster --name param.k8s.local --zones ap-south-1a --image ami-0f918f7e67a3323f0  --control-plane-count=1 --control-plane-size t2.medium --node-count=2 --node-size t2.micro
kops update cluster --name param.k8s.local --yes --admin
```

------------
> [!NOTE]
> 1. param-kops-testbkt143.k8s.local = is the bucket name, change it according to your needs and choose your region as needed.
> 2. param.k8s.local = is the cluster name.
> 3. In order to setup the main and worker nodes, iam using AMI machine image, **ami-0f918f7e67a3323f0** which is UBUNTU machine's AMI.
> 4. For this setup we are uisng t2.medium for main node ( control plane) and t2.micro for worker node.
------------------

Save and run the script.

It may take a while to setup as it need to configure multiple things.  
You can see the setup configuring in the your AWS account.  

It is advised to run the following command again ( even though it was mentioned in the above script).  
`export KOPS_STATE_STORE=s3://param-kops-testbkt143.k8s.local`  

To verify the setup of cluster, use the following command  
`kops validate cluster --wait 10m`  
This command will return the status of cluster for a period of 10 mints.  
The setup may take more than 10 mints. So Wait for untill setup was configured and you can see all 3 nodes up and healthy.  

After sucessfull setup,  
`kops get cluster`       --> to get the cluster details.  
`kops get cluster -o wide`    --> to get more details of cluster.

-------------------
> [!NOTE]
> kops edit cluster cluster_name   ---> to edit cluster (like replicas count etc).  
> kops edit ig --name=cluster_name nodes-ap-south-1a ---> to edit worker nodes instance group.
> kops edit ig --name=cluster_name control-plane-ap-south-1a    --> to edit control-plane (master) node instance group.  
-------------------

Lets try to create some nodes using deployment.

`vi deployment.yml`

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ib-deployment
  labels:
    app: bank
spec:
  replicas: 4
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
        image: nginx
```

`kubectl create -f deployment.yml`    --> to run the deployment.

lets see the nodes of the deployments.  
`kubectl get pods`  	--> to get the pods of deployment.  
`kubectl get pods -o wide`  
`kubectl get nodes`    --> to get the nodes of the cluster.  
`kubectl get nodes -o wide`  


##### Lets look how scaling works for multi node cluster

**_Scale out_** :  
`kubectl scale deployment/ib-deployment --replicas=10`    --> this will replicate the pods to 10.

lets check the pods count,  
`kubectl get pods -o wide`  

**_Scale in_** :  
`kubectl scale deployment/ib-deployment --replicas=4`

check again the pods count and the nodes that pods belongs to.  

> [!NOTE]
> Remember, not to exit the cluster without deleting it, if not you will be charged on a HUGE amount from AWS for using AWS resources as we are using AWS servers for setting up multinode cluster.

### **To delete the cluster**:  
`kubectl delete cluster --name param.k8s.local`		--> param.k8s.local is the name that have used for the cluster.

-----------------------------------------------------------------------------------

# 6. NAMESPACES.

> [!NOTE]
> If you are very new to using multi node cluster and are not fine to go with multi node cluster, then go with minikube (single node cluster) than KOPs.
Name space is the means by which we segregate to differenciate different enviroments/teams.

If we have multiple teams, say _Development team_, _Testing team_, _Prepod team_ and _prod team_. and all of these teams want to work with kuberetes, then instead of going with multiple clusters of kubernetes, we just create different **namespaces** for each team in a single cluster.


Good thing about namespaces is that budefault, they cannot talk with each others. so complete isolation from each other.  

In kubernetes, if we are using a cluster, there are few default namespaces already present. they are:  
| Types  	|  Purpose or work |
| ---------- | -----------------|
| default 	|  This is default namespace. If no namespace is mentioned, all objects are created here |
| kube-node-release |	It will store the object which is taken from one namespace to another |
| kube-public	|All Public objects are stored here, generally namespace are private, if you want common public namespace |
|kube-system	| By default K8S will create some object, those are stored here |

> [!NOTE]
> 1. Objects here refers to deployments, replica sets, pods, services. Every thing in K8S are treated as objects.  
> 2. Default objects that K8S will createa are apiserver, controller manager, schedular, etcd, kubelet, kubeproxy or simply, every component of kubernetes cluster is going to create in the form of POD, All these PODS are stored in Kube-System Namespace.


`kubectl get namespace`		--> to get the list of namespaces.  
`kubectl get ns`		--> same as above.  

Bydefault, pods will be created in default name space if no namespace is mentioned.  
`kubectl describe pod`		--> can see the namespace details.  
`kubectl get pods -A`		--> to get pods of all namespaces.  
`kubectl get pods -n namespace_name` --> to get the pods of specific namespace, use default, kube-public as namespace.


##### Lets create name spaces.
`kubectl create ns dev`		--> creating a namespace named dev.  
`kubectl get ns`		--> look for the created namespace in results.  

How to check in which namespace you are currently are  
`kubectl config view`  
Bydefault we will be in default namespace and hence all pods are created here in the default namespace.

Lets switch to dev namespace.  
`kubectl config set-context --current --namespace=dev`  

conform the switch was sucess.  
`kubectl config view`  

lets create pods in pod namespace.  
`kubectl run dev1 --image nginx` 	--> creating nginx pod with pod name as dev1.
`kubectl run dev2 --image nginx`	--> creating nginx pod with pod name as dev2.

As we have pods in the default namespace and dev namespace, lets use _get pods_ command and see which pods will be listed  
`kubectl get pods`  
only the pods belongs to dev namespace are listed.  


As I have mentioned that use of namespaces will have complete isolation from ine another, but with use of `kubectl get pods -A` we can get all pods of all namespaces.  
Also, we can shift from one namespcae to another namespace, then how come its a complete isolation!!.  

In this case, anyone can access/delete/create pods in any namespace. Which is not good. for this we need restrict users to access namespaces using RBAC ( Role based Access Control ).

# 7. RBAC.

# 8. SERVICES.

The very use of services is to enable the communication.  
When I say communication I mean two aspects,   
* _**Communication in between cluster**_  
	When two pods need to work depending on another ( say i have UI in one pod that connects to database in 		another POD) then the two pods need to connect or communicate and this is internal aommunication.  
 * _**Communicatio to the outside world.**_  
	I also need ot make the UI presented to my users to use it, to interact with it. This is outside the cluster communication.


So services allow you to expose your application running on pods to other components within cluster or to the external users.  

Services porvide a stable IP address and DNS name for the set of PODS, which might chnage over time due to scaling or updates.

#### Key concepts of SERVICES in Kubernetes:
1. **_Cluster IP_** :  
   This is default type of service. It exposes the Service on a cluster-internal IP. Other services within the same Kubernetes cluster can access the Service, but it is not accessible from outside the cluster.  
   This creates a connection using an internal Cluster IP address and a Port.

2. **_NodePort_** :  
   This type of Service exposes the Service on each Node’s IP at a static port. A NodePort Service is accessible from outside the cluster by hitting NOdeIP:NOdePort  
   when node port is created, kube-proxy exposes a port in the range 30,000-32,767.  
   We can explicitly mention the port no. else k8s takes are of assigning the port no. but anyhow, the port no. should be in same rangee.

3. **_TargetPort_** :  
   Pod Container port. Pod's container listens on applicationn port Ex: 80 or 8080, if you dont use this line, K8s will assign default 80 port.  

4. **_LoadBalancer_** :  
   This Service type exposes the Service externally using a cloud provider’s load balancer. It is typically used in cloud environments like AWS, GCP, or Azure.  
   A LoadBalancer is a Kubernetes service that:  
	* Creates a service like cluster IP,  
	* Opens a port in every node like nodeport,  
	* Uses a load balancer implementation from your cloud provider.

> [!NOTE]
> We dont need to explicitly mention the loadbalancer's url or to create a load balancer in aws account and copy paste the url. k8s will take care of this as it creates its own VPC and respective needed resources in this VPC.
   

Services in k8s are created on top of deployment. so we cannot a standalone service without any deployments.  
Services are defined with _manifist.yml_ file.


Lets creat a deployment and then create service on top of it.  
We can define both deployment and service in a single manifist.yml file.  

#### 8.1 For clusterIP exercise.    
`vi nginxapp.yml`  

```
appVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginxapp
spec:
  replicas: 3
  selector:
     matchLabels:
        app: nginxapp
  template:
    metadata:
      labels:
        app: nginxapp
    spec:
      containers:
        - name: cont1
          image: nginx
---
apiVersion: v1
kind: Service
metadata:
  name: nginxapp-service
spec:
  type: ClusterIP
  selector:
    app: nginxapp
  ports:
    - port: 80
      targetPort: 80
```

In the file, -port: 80  = expose the service on port 80.   
targetPort: 80  = Pod's container listens on 80, if you dont use this line, k8s will assign defalut 80 port.


How Traffic Flows  
	_Client connects to my-service:80  
	Service forwards request to the Pod’s container at 8080 if 80 (because targetPort: 8080 / 80)  
	The container in the Pod listens on 8080 / 80 and processes the request._  


Run the nginxapp.yml file.  
`kubectl create -f nginxapp.yml`  

get list of services.  
`kubectl get svc`  

get list of pods.  
`kubectl get pods -o wide`  

describe the nginxapp-service that we have created.  
`kubectl describe svc/nginxapp-service`   --> nginxapp-service is the name of the service that we have created.  

As of now we have created clusterIP but with this we can anly estlabish internal communication but not outside world communication.  
`kubectl delete -f nginxapp.yml`   --> to delete the created deployment and service.


#### 8.2 For NodePort service.  
`vi nginxapp.yml`  
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginxapp-deployment
  labels:
    app: nginxapp
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginxapp
  template:
    metadata:
      labels:
        app: nginxapp
    spec:
      containers:
      - name: cont1
        image: nginx
---
apiVersion: v1
kind: Service
metadata:
  name: nginxapp-service
spec:
  type: NodePort   # Type Nodeport, but if you dont mention port number under ports section, K8s will assign random port
  selector:
    app: nginxapp
  ports:
    - port: 80
      targetPort: 80  # Ensure this matches the container's port, if you dont use this line, K8s will assign default 80 port
```

create or run the file.  
`kubectl create -f nginxapp.yml`  

lets describe service that we have created.  
`kubectl get svc`  
 `kubectl describe svc/nginxapp-service`  

 Lets connect to the nginxapp  
 use `http://ip:portnumber`  
 it may not woork as the cluster created new VPC and new SG for cluster, we need to allow the inblound rules for the port.  So go to respective Security Group, allown alltraffic for all IPs. 

 If we want to explicitly mention the Nodeport, then edit the above file and add `nodePort: 3122` at the end of ports section.  
 Remember the nodeports range should be between 30,000 to 32767.  

How traffic flows: 
	_Client accesses http://<NodeIP>:31234  
	Traffic reaches Kubernetes Node on nodePort: 31234  
	The service forwards it to port: 80 (internal Service port)  
	Then it forwards the request to targetPort: 80 (inside the Pod’s container)._

`kubectl delete -f nginxapp.yml` 	--> to delete the deployment and services from file.  

As we cannot provide the Ips to users, we need to use load balancers.  
Along with load balancer, use Route53 to give the url a domani name.  


 #### 8.3 For LoadBalancer  
 `vi nginxapp.yml`

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginxapp-deployment
  labels:
    app: nginxapp
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginxapp
  template:
    metadata:
      labels:
        app: nginxapp
    spec:
      containers:
      - name: cont1
        image: nginx
---
apiVersion: v1
kind: Service
metadata:
  name: nginxapp-service
spec:
  type: LoadBalancer
  selector:
    app: nginxapp
  ports:
    - port: 80
      targetPort: 80  # Ensure this matches the container's port, if you dont use this line, K8s will assign default 80 port
      nodePort: 31433 # If you dont mention target and nodeports, K8s will generate random nodeport and target port 80
```

Create the deployment and service.  
`kubectl create -f nginxapp.yml`  

describe the service.  
`kubectl describe svc/nginxapp-service`  

```
kubectl get svc		  
```
note the loadbalancer url.   
use the url and access the application.  

# 9. Auto scaling with Kubernetes METRIC SERVER
So far we hvae been doing scaling of pods, replicas, deployments manually.  
```
kubectl scale object --replicas=10
```

But we need auto scaling. This can be acheived by monitoring metrics like CPU, Memory etc.

_**Kubernetes Metric Server**_, is a scalable efficient source for monitoring the overall health and performance of a kubernetes cluster, providing the data need for kubernetes features like **HORIZONTAL POD AUTOSCALING** **( HAP )** and Kubernetes Dashboard.  

**Key features**:  
#### 10.1 Resource Metrics:
Collects CPU and memory usage metrics from kubelets and provides aggregated metrics at the node and pod level.  

#### 9.2 Autoscaling:  
Enables features like the Horizontal Pod Autoscaling (HPA), which automatically adjusts the no. of pods in a deplooyment based on the observed CPU or memory utilization.

#### 9.3 Kubernetes Dashboard:  
The metrics server provides the resources usage data dislayes in the kubernetes Dashboard.

#### 9.4 Kubelets:  
Each nodes in a kubernetes cluster runs a kubelet that periodically clooects resources usage statics from the node and the containers running on it.

#### 9.5 Metrics server: 
Metrics server collects these metrics from the kubelets and stores them in memory, aggregating them to be accessed by other components like HPA.

_So in short:_  
	Info like CPU, Memory from each PODS, Nodes -------> collected by Metrics Server in K8S.  
	This will be done on every 15 sec.  ( we can say near real time.)  

Well, the Metrics server is not default in K8S, its like a addon plugin.  
We need to install in the master server.  

Install the Metrics Server from github official repo's .yml file.    
```
kubectl create -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/high-availability-1.21+.yaml
```


Lets check the metrics of resources.  
```
kubectl top pods
```

```
kubectl get nodes
```


With this lets acheive Autoscaling.

**Auto-Scaling**:

HPA - to scale no. of pods based on metrics usage.  The metric can be CPU, Memory or even custom metrics.  
Remember that its PODS that we scale not NODES here.  

Before scale In, process will wait for few mins to scale-in to complete the traffic requests this is called COOLING PERIOD   

In Kubernetes, the cooling period for the Horizontal Pod Autoscaler (HPA) is the amount of time the HPA waits after a scale event before triggering another scale event.  

Scaling can only be done on/for scalable objects like Deployments, Replicasets, Pods, Replication Controller.  

_Replication controller is the older version of Replicasets._


So lets create a deployment object and run it.
```
vi nginxapp.yml
```

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginxapp-deployemnt
  labels:
    app: nginxapp
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginxapp
  template:
    metadata:
      labels:
        app: nginxapp
    spec:
      containers:
       - name: cont1
         image: nginx
```

Create the deployment.  
```
kubectl create -f nginxapp.yml
```

Get the pods list.  
```
kubectl get pods
```

Get the Metrics of pods.  
```
kubectl top pods
```

Now lets auto scale the pods,  
```
kubectl autoscale deployment nginxapp-deployment --cpu-percent=20 --min=1 --max=10
```
The commad says, if the cpu percentage goes up more than 20 then use auto scaling to scale up to 10 pods.  

```
kubectl het hpa
```
This wil show cpu: 1% / 20% , now cpu percent is 1%, it will take time.  

You can stress the pods by installing stress inside the pods.  
First connect to a pod interactive mode.  
```
kubectl exec -it nginxapp-deployment-XXXXXX-XXXX -- /bin/bash
```
Install _STRESS_, inside the pod.  
```
apt update
apt install stress
stress --cpu 8 --io --vm 2 --vm-bytes 128M --timeout 60s
exit
```

Meanwhile duplicate the present tab and watch the pods creation lively.

Delete the stress or completely delete the deployment object's yml file.


Lets do the same autoscaling but now with Manifist file ( declaretive mode) most used way.  
---------------

Create deployment.  
```
vi auto.yml
```

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginxapp
spec:
  replicas: 2
  selector:
    matchLabels:
      app: nginxapp
  template:
    metadata:
      labels:
        app: nginxapp
    spec:
      containers:
      - name: cont1
        image: nginx
```

```
kubectl create -f auto.yml
```

```
vi hpa.yml
```

```
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: nginxapp-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: nginx-deployment
  minReplicas: 2
  maxReplicas: 10
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 20
```

NOTE: we can use a single yaml file to define the deployment and autoscaling as well.  

In the scaleTargetRef section, the details of the target deployment file are to be mentioned.


```
kubectl apply -f hpa.yml
```

In the similar way as we did above, go to interactive mode into any pod, install stress and run the stress execution command.  
and look for actoscaling working.  


To delete the Metrics Server, 
```
kubectl delete -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/high-availability-1.21+.yaml
```

 	

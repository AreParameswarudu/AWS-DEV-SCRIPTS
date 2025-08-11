For installing or settuping up the **PROMETHEUS** and **GRAFANA** in EKS cluster have a slight chnages.

They both require PVC Persistent Volume Claims,  
* In K8S cluster, Volume is avaible from the ec2 instance itself so no need to explicitly mention or assign. but,   
* In EKS cluster, EBS volumes has to be assigned or Claimed, and it makes an issue if tried to assign like `--set alertmanager.persistence.storageClass="gp2"`.


So rather than mentioning, we can have an alternative, 

1. Set up the EKS cluster.

2. Add Helm, Helm charts for prometheus and grafana.


3. Settingup prometheus and grafana

   3.1. Create a single name space for both prometheus and grafana.
   ```
   kubectl create ns monitoring
   ```
  3.2. Install prometheus into the namespace.
  ```
   helm install prometheus prometheus-community/kube-prometheus-stack --namespace monitoring
   ```
  3.3. External access of prometheus.
  We will be getting like this, 
  ```
NAME: prometheus
LAST DEPLOYED: Mon Aug 11 19:41:55 2025
NAMESPACE: monitoring
STATUS: deployed
REVISION: 1
NOTES: kube-prometheus-stack has been installed.
Check its status by running: kubectl --namespace monitoring get pods -l "release=prometheus"
Get Grafana 'admin' user password by running: kubectl --namespace monitoring get secrets prometheus-grafana -o jsonpath="{.data.admin-password}"  base64 -d ; echo
Access Grafana local instance:
export POD_NAME=$(kubectl --namespace monitoring get pod -l "app.kubernetes.io/name=grafana,app.kubernetes.io/instance=prometheus" -oname) kubectl --namespace monitoring port-forward $POD_NAME 3000
Visit https://github.com/prometheus-operator/kube-prometheus for instructions on how to create & configure Alertmanager and Prometheus instances using the Operator.
```
It says that the prometheus is listning at 3000,   
lets create a service object for that so that we can access it by using EKS cluster node ( from ec2 console) public ip.

`vi prom-service.yml`  

```
apiVersion: v1
kind: Service
metadata:
  name: grafana-nodeport
  namespace: monitoring
spec:
  type: NodePort
  selector:
    app.kubernetes.io/name: grafana
    app.kubernetes.io/instance: prometheus
  ports:
    - port: 3000
      targetPort: 3000
      nodePort: 30090
```

then, use `kubectl apply prom-service.yml -n monitoring`

in the browser, `http://public-ip:30090`
Note public ip sholud be the ec2 instance created from EKS cluster.

### Similarly for grafana

3.4. install grafana
```
helm install grafana grafana/grafana --namespace monitoring
```

you will be getting like this, 
```
NAME: grafana
LAST DEPLOYED: Mon Aug 11 20:04:02 2025
NAMESPACE: monitoring
STATUS: deployed
REVISION: 1 NOTES:
- Get your 'admin' user password by running:
- kubectl get secret --namespace monitoring grafana -o jsonpath="{.data.admin-password}"  base64 --decode ; echo
- The Grafana server can be accessed via port 80 on the following DNS name from within your cluster:
- grafana.monitoring.svc.cluster.local
- Get the Grafana URL to visit by running these commands in the same shell: export POD_NAME=$(kubectl get pods --namespace monitoring -l "app.kubernetes.io/name=grafana,app.kubernetes.io/instance=grafana" -o jsonpath="{.items[0].metadata.name}") kubectl --namespace monitoring port-forward $POD_NAME 3000
- Login with the password from step 1 and the username: admin
```

3.5. We can simply go like this as well
```
kubectl patch svc grafana \
  -n monitoring \
  -p '{"spec": {"type": "NodePort"}}'
```

```
kubectl get svc grafana -n monitoring
```
the last command sill give us the node port ranging between 30000 - 32767.

use, `http://public-ip:port-no`

to access the grafana.

and its password can be found at, 
```
kubectl get secret --namespace monitoring grafana \
  -o jsonpath="{.data.admin-password}" | base64 --decode
```

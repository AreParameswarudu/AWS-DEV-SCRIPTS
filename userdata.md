
# For apache2 web server on a AL2023 machine
```
!#/bin/bash
//install apache in AL2 machines
yum install httpd -y

// run the apache service
service httpd start

chkconfig httpd on
mkdir /var/www/html
echo 'Hey this is my first website onec2' > /var/www/html/index.html
```


# For nginx web server on a AL2023 machine
```
!#/bin/bash
//install nginx
yum install nginx -y

//run or start the service
systemctl start nginx
```

## Repos, links, 
1. Veerababu sir
   ```
   https://github.com/CloudTechDevOps
   ```

2. Raham sir
  ```
  https://github.com/rahamshaik007
  ```

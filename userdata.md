```
!#/bin/bash
//install apache in ubuntu or AL2 machines
yum install httpd -y
// run the apache service
service httpd start
chkconfig httpd on
mkdir /var/www/html
echo 'Hey this is my first website onec2' > /var/www/html/index.html
```



https://docs.google.com/document/d/1WAS6QbHIqt5Vup6fKo7hAsmBMit6D87tySaS0-uwhXg/edit?tab=t.0

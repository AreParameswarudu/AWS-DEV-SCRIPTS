# If the ec2 has key with it to login ( .pem key),   

1. login to bastion  
2. go to  `/home/ec2-user/.shh/`
```
cd /home/ec2-user/.shh/
```
3. Add the .pem key with same name as in the ec2 details section
   ```
   vi key-name.pem
   ```

4. change the permissions to the key create.
```
chmod 400 /home/ec2-user/.shh/key-name.pem
```

5. use ssh to login to ec2 in private subnet.
```
shh -i ~/home/ec2-user/.shh/key-name.pem ec2-user@private-ip
```
Replace the private ip with the actual private ip of the ec2 that we are trying to login into.


# If no key is mentioned in the ec2 details of the ec2 that we are trying to shh into.

```
shh ec2-user@private-ip
```


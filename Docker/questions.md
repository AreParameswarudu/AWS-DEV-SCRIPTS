# Q1. How do we reduce the size of a docker image!!
There are different ways we can adopt to reduce the size of a docker image they are,   
### 1. Reduce the layers of docker file.
Each instruction in a `Dockerfile`  that modifies the filesystem creates a new layer. Combine multiple `RUN` commands into a single `RUN` instruction suing `&&` to reduce the number of layers.
### 2. Use of low resolution base image.
### 3. Use of multi stage for build.

Example for each appraoch and for more other approches, refer [https://medium.com/@ksaquib/how-i-cut-docker-image-size-by-90-best-practices-for-lean-containers-1f705cead02b]

<img width="579" height="119" alt="image" src="https://github.com/user-attachments/assets/3b78b79b-5bf1-4a3e-8bf5-483ef9ca3e02" />  
`Dockerfile`s for,    

```
#image1
FROM ubuntu:22.04

RUN apt update -y
RUN apt install -y python3 python3-pip  git
RUN mkdir /app
RUN echo "print('Hello world')" > /app/app.py
RUN chmod +x /app/app.py
CMD ["python3", "/app/app.py"]

#image2
FROM ubuntu:22.04

RUN apt update -y && \
    apt install -y python3 python3-pip git && \
    mkdir /app && \
    echo "print('Hello world')" > /app/app.py && \
    chmod +x /app/app.py

CMD ["python3", "/app/app.py"]



#image3
FROM ubuntu:latest
RUN apt-get update
RUN apt-get install -y curl
RUN apt-get clean

#image4
FROM ubuntulatest 
RUN apt-get update && apt-get install -y curl && apt-get clean



#image5
FROM python:latest
RUN pip install flask numpy pandas
RUN mkdir /app
RUN echo "print('Hello from Flask')" > /app/app.py
CMD ["python", "/app/app.py"]

# image6
FROM python:3.11-slim

RUN pip install flask numpy pandas && \
    mkdir /app && \
    echo "print('Hello from Flask')" > /app/app.py

CMD ["python", "/app/app.py"]
```

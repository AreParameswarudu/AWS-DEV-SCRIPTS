# Q1. How do we reduce the size of a docker image!!
There are different ways we can adopt to reduce the size of a docker image they are,   
### 1. Reduce the layers of docker file.
Each instruction in a `Dockerfile`  that modifies the filesystem creates a new layer. Combine multiple `RUN` commands into a single `RUN` instruction suing `&&` to reduce the number of layers.
### 2. Use of low resolution base image.
### 3. Use of multi stage for build.

Example for each appraoch and for more other approches, refer [https://medium.com/@ksaquib/how-i-cut-docker-image-size-by-90-best-practices-for-lean-containers-1f705cead02b]

  
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

 <img width="579" height="119" alt="image" src="https://github.com/user-attachments/assets/3b78b79b-5bf1-4a3e-8bf5-483ef9ca3e02" />  



2. What happens if you use `CMD ["python", "app.py"]` in you docker file!!

Lets say that we ahve a docker file that uses a python docker image ( or ubuntu and you installed ptyhon in it),  
and you defined a python script to be run. 

The responce/working of the `CMD ["python", "app.py"]` will actually depends.  
    A. If the docker file(more specifically in the python script) says that the script runs and be exposed to some port number then it will still be in running state untill stoped explicitly.  
    Example:
    ```
    #Dockerfile
    FROM python:3.9
    WORKDIR /app
    COPY requirements.txt .
    RUN pip install -r requirements.txt
    COPY . .
    EXPOSE 5000
    CMD ["python", "app.py"]


    #app.py
    from flask import Flask
    app = Flask(__name__)
    @app.route('/')
    def hello():
        return "Hello, World!"

    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)


    #requirements.txt
    flask==2.3.2
    ```
    We can use ip:5000 in browser and can get the output.

    
    B. If the docker file(more specifically in the python script) simply defined to run a script then it runs the script and the container get exited as there are no working processes present.

    Example:
    ```
    #app.py
    print("hello world")

    #requirements.txt 
    flask==2.3.2

    #Dockerfile
    FROM python:latest
    WORKDIR /app
    COPY requirements.txt
    RUN pip install -r requirements.txt
    COPY . . 
    CMD ["python","app.py"]

    ```

# Q1. How do we reduce the size of a docker image!!
There are different ways we can adopt to reduce the size of a docker image they are,   
### 1. Reduce the layers of docker file.
Each instruction in a `Dockerfile`  that modifies the filesystem creates a new layer. Combine multiple `RUN` commands into a single `RUN` instruction suing `&&` to reduce the number of layers.
### 2. Use of low resolution base image.
### 3. Use of multi stage for build.

Example for each appraoch and for more other approches, refer [https://medium.com/@ksaquib/how-i-cut-docker-image-size-by-90-best-practices-for-lean-containers-1f705cead02b]

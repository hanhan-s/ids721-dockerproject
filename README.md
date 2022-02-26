# ids721-microservice
Working environment for ids721

# Docker Project

This project build a fastapi which is deployed on ECR and ECS.
The project is also deployed on Kubernates.


## Reference

Source code: [noahgift/container-from-scratch-python](https://github.com/noahgift/container-from-scratch-python).  
Source code: [noahgift/container-revolution-devops-microservices](https://github.com/noahgift/container-revolution-devops-microservices).  


## How to use

To build a docker image and push it to registry, you can follow these steps:

### Set up a project

Launch AWS Cloud9, choose or create an environment.  
Create ssh-keys and upload it to Github.  ``ssh-keygen -t rsa``  
Create a new repo on github, git clone it to your AWS local and cd into it.  
Create all related files, including **Dockerfile, Makefile, requirements.txt, app.py**.  


### Run this app locally

Create a virtual environment and activate it. (To deactivate it, run "deactivate") 

```
python3 -m venv ~/.fastapi
source ~/.fastapi/bin/activate
```

Install the required packages. ```make install```  
Run this app. ```python main.py```  

### Build an image and run a container

We will pull down an official base image, package up our own software and runtime on top of it.  
Build an image accoridng to the setup in Dockerfile, name it "app", tag it "v1".  

```
docker build -t app:v1 .
```

```
docker run -it app:v1 bash 
```

```
python main.py
exit
```

### Push to Docker Hub

Create a new repository "dockerproj" on DockerHub.  
Login to DockerHub in your AWS local.  

```
docker login
```

Tag your image with hostname and self defined ```tag-name```.  

```
docker tag app:v1 hanhan-s/fastapi:[tag-name]
```

Push it to Docker Hub.

```
docker push hanhan-s/fastapi:[tag-name]
```

### Pull from Docker Hub

```
docker pull hanhan-s/[repo-name]:[tag-name]
```

### Push to Amazon ECR

Open Amazon ECR console.  
Create a repository, call it "dockerproj" and enable "Scan on push".  
Click on the newly created repo, and click on **"view push commands"**. It will show commands like below:  
First authenticate.  
Then build docker image.  
Then tag the image.  
Finally push this image to AWS repository.  
The command will be like:  

### Deploy to Amazon ECS fargate

Make sure you have pushed your image to Amazon ECR.  
Open ECS and "get started".  
"Container definition", choose to configure your custom container image. (You can get the image from Amazon ECR)  
 "Define your service", check load balancer for your service.  
 "Configure your cluster", name your cluster.  

And you can see the service is running and access the public IP.

### Kubernetes deployment

```
kubectl apply -f api.yaml
```

If working locally, e.g. using `minikube`, use port forwarding to expose the service:

```
kubectl port-forward service/fastapi-svc 8000
```

To scale the deployment, apply a HorizontalPodAutoscaler. Either:

```
kubectl apply -f autoscale.yaml
```

or:

```
kubectl autoscale deployment dockerproj --cpu-percent=50 --min=1 --max=10
```

[![Python application test with Github Actions](https://github.com/hanhan-s/ids721-microservice/actions/workflows/main.yml/badge.svg)](https://github.com/hanhan-s/ids721-microservice/actions/workflows/main.yml)

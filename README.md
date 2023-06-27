# Project Summary
python-Flask-Docker-kubernetes

This project shows how to build docker image using Dockerfile for a python-Flask application ,the docker image is push  and stored in dockerhub.This image is then pulled and deployed into kubernetes clusters.As the kubenrnete files grow bigger i then used helm charts to manage my kubernetes manuscripts files .This demonstrates the deployment of a python-Flask based application project. I created a virtual environment for this project called venv buit since t i dont need this in my Github when i push the code i saved the venv
 in .gitignore

# Project Requirements/Perequisite
 1. Install an IDE preferably Vscode
 2. install Git
 3. create project in Git and clone into your Vscode terminal
 4. cd into that project folder and create a virtual environment $pip -m venv
 5.  install python
 6. Install Flask    $pip install Flask
 7. Set up kubernetes cluster (Either of this two)
  i. Set up minikube cluster
  ii. Set up Aws Elastic Container Service(AWs ECS) using AWS management console or terraform tool
 8. Install Docker Desktop locally on your machine and have a Dockerhub account
 9. Install kubernetes command line interface(kubectl CLI)
 10. Write kubernetes manuscripts files for the application
 11. Install Helm Charts to manage your k8s files


# Create a requirements.txt file to name all the dependables for this project
 $touch requirements.txt

# To freeze all the dependnecies used for this project into requirements.txt,i ran command

 $pip freeze requirements.txt

# To free all the dependables in the docker image to be build, i ran inside the Dockerfile
 $pip install -r requirements.txt

# Dockerfile contents
FROM python:3.10.0-alpine3.15
ADD . /app
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src src
EXPOSE 5002
HEALTHCHECK --interval=30s --timeout=30s --start-period=30s --retries=5 \
     CMD curl -f http://localhost:5002/food || exit 1
ENTRYPOINT [ "python","./src/main.py" ]

# Check if you have docker installed locally
 $docker --version

# To check if theere are no docker images already i ran
  $docker images
# To check if there are no docker container running or not already i ran
 $docker ps -a

# To build the docker image called flaskapp1 i ran
 $docker build -t <dockerusername/flaskapp1> .

# To run the application locally,i run the container using the docker image built with the #container namespace called pythonweb i ran

 $docker run -p -d 80:5004 --name pythonweb <dockerusername/flaskapp1>

 # Check for any new images
 $ docker images

  # To remove docker images
   $ docker rmi <imagename>
 # To remove docker conatiner forcefully

 $ docker rm -f <container_ID>

 # Now push the images into dockerhub to store
 $ docker login
 $docker push <dockerusername/imagename>:latest

# I created another directory called kubernetes  in my root directory to house all the k8s # manuscripts files
 $mkdir kubernetes 
$touch deployments.yml
$touch service.yml

# Check the k8s cluster information
 $kubectl cluster-info
 # To get more information about your cluster
 $kubectl cluster-infor dump

# Check for any existing node pods in the cluster
 $kubectl get pods --all

 # Check for anyfor details of a particular pod in the cluster
  $kubectl describe pod <nameofpod>

# I created the deployments file with this command using kubectl cli
 $kubectl apply -f deployment.yml 
 # to view the application externally using loadbalancer as type, run the command to create service
 $kubectl  apply -f service.yml
 # to get all the service created
 $kubectl get svc

# to get get a particular service 
   $kubectl service <servicename>

   # to get get a particular service 
   $minikube service <servicename>

   # Now we need to now mamange the k8s files so we need to install helm but firstbdelete all the kubenrnetes object #in the kubernets directory,first chanage directory to kubernetes
   $cd kubernetes && kubectl delete -f .

   # install helm
  # install helm charts locally on your machine
   $From Script
   Helm now has an installer script that will automatically grab the latest version of Helm and install it locally.

    You can fetch that script, and then execute it locally. It's well documented so that you can read through it and understand what it is doing before you run it.

  $ curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
  $ chmod 700 get_helm.sh
   $ ./get_helm.sh
   # now install k8s helm
   $ pip3 install helm-charts

   # check for the installed helm on your ma
   chine
    $helm version 
   # now create helm 
   $ helm create flaskapp

   # After changing values in helm chart i will now render the it, using the command below
    $helm template flaskapp

   # Now release the helm by running this command below
    $ helm install web flaskapp
 NAME: web
LAST DEPLOYED: Tue Feb 27 17:50:37 2023
NAMESPACE: default
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
 Get the application URL by running these commands:
  export NODE_PORT=$(kubectl get --namespace default -o jsonpath="{.spec.ports[0].nodePort}" services web-flaskapp)
  export NODE_IP=$(kubectl get nodes --namespace default -o jsonpath="{.items[0].status.addresses[0].address}")
  echo http://$NODE_IP:$NODE_PORT


# check helm list

$helm list









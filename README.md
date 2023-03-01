# ml_deploy

It is a repository for deploying ML models and testing poetry, nox, tensorflow, flask, and swagger.

Model is trained using MNIST dataset and recognizes digits **[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]**.

There are two different models:
- model_1
- model_2

Scripts for generating models and test samples are jupyter notebooks: 
- model_1.ipynb
- model_2.ipynb


## **Prerequisites:**

Install Docker Desktop

In Docker Desktop - Settings - Kubernetes - check "Enable Kubernetes"

Move files to **ml_deploy** parent directory:

- Dockerfile
- deployment.yaml

Test the code - in Anaconda Prompt (anaconda3) in **ml_deploy** directory run:

nox --verbose


## **User Guide:**

- start Docker Desktop.exe

- open cmd as admin

- go to **ml_deploy** parent directory and run:

docker build -t model-deploy .

- verify the image was created:

docker image ls

- run the application in a container and map it to port 5000:

docker run -p 5000:5000 model-deploy

- send the YAML file to Kubernetes:

kubectl apply -f deployment.yaml

- see the pods are running:

kubectl get pods

- tag docker image

docker image tag model-deploy USER_NAME/model-deploy:latest

- push image to docker hub

docker image push USER_NAME/model-deploy:latest


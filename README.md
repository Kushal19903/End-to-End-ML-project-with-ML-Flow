# End-to-End-ML-project-with-ML-Flow
# End-to-end-Machine-Learning-Project-with-MLflow


## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml            (used for model ttraining)
4. Update the entity                        (config entity)
5. Update the configuration manager in src config        (configuration.py)
6. Update the components             (create component)
7. Update the pipeline               (create pipeline)
8. Update the main.py                 (add in main.py)    delete artiflex for each process
9. Update the app.py



# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/Kushal19903/End-to-End-ML-project-with-ML-Flow
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n mlproj python=3.8 -y
```

```bash
conda activate mlproj
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```



## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/Kushal19903/End-to-End-ML-project-with-ML-Flow.mlflow \
MLFLOW_TRACKING_USERNAME=Kushal19903 \
MLFLOW_TRACKING_PASSWORD=68a140eff3be1be76627b033e2aac7487d069bf2 \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/Kushal19903/End-to-End-ML-project-with-ML-Flow.mlflow

export MLFLOW_TRACKING_USERNAME=Kushal19903 

export MLFLOW_TRACKING_PASSWORD=68a140eff3be1be76627b033e2aac7487d069bf2

```
prediction.py
app.py
css js html result setup
run app.py
/train  - values --- output

write code in docker also to make code as image format
create main.yaml in github 


# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment   ---- user ----create ----attach 3 option---policy
##----security----access key generate----CLI----CREATE ACCESS KEY----DOWNLOAD CSV FILE ---open

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

#-----ecr ---- create repository  ---- copy URI
## 3. Create ECR repo to store/save docker image
    - Save the URI: 528757828449.dkr.ecr.eu-north-1.amazonaws.com/mlproj

#---dashboard EC2 ----mlproj-machine  -----ubantu---select instance provioder	----t2/t3large 8gb
#---key pair login---create mlproj(RPS) ----downloaded---allow http and https traffic---configuration size atleast 32gb---launch instance ----view launch instance---running---click instance id---connect
---install
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	installlllllllllllllllllll
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker

-- success - docker --version
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one

--github in new tab ---settings ----run all command ---connecting github with (aws)
--when we push to github for updates it will automatically deploy for automated code by self host runner----> configure command give ----enter ----"self-host"---enter--github connected yo aws success

# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app


---settings ---secrate variables---actions---secrate repository---"aws secrate id downloaded file in excel paste it"

## About MLflow 
MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & tagging your model



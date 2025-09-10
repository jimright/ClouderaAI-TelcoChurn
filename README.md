# Churn Prediction Prototype
This project is a Cloudera Machine Learning 
([CML](https://www.cloudera.com/products/machine-learning.html)) **Applied Machine Learning 
Project Prototype**. It has all the code and data needed to deploy an end-to-end machine 
learning project in a running CML instance.

## Project Overview
This project builds the telco churn with model interpretability project discussed in more 
detail [this blog post](https://blog.cloudera.com/visual-model-interpretability-for-telco-churn-in-cloudera-data-science-workbench/). 
The initial idea and code comes from the FFL Interpretability report which is now freely 
available and you can read the full report [here](https://ff06-2020.fastforwardlabs.com/)

![table_view](images/table_view.png)

The goal is to build a classifier model using Logistic Regression to predict the churn 
probability for a group of customers from a telecoms company. 
The Logistic Regression model is deployed using CML's real-time model deployment 
capability. We use this model  as a rest endpoint to allow enrichment of a DataViz dashboard using ML trained models. 



### Initialize the Project
There are a couple of steps needed at the start to configure the Project and Workspace 
settings so each step will run successfully. You **must** set the `DATABASE` env variable under the Project Settings.  
You **must** run the project bootstrap before running other steps. 


### 0 Bootstrap
Just to reiterate that you have run the bootstrap for this project before anything else. 
So make sure you run step 0 first.   

Open the file `0_bootstrap.py` in a normal workbench PBJ python3 session. You only need a 
2 vCPU / 4 GB instance. Then **Run > Run All Lines**


### 1 Model Training


Open the file `1_trainStrategy_job.py` in a normal workbench PBJ python3 session. You only need a
2 vCPU / 4 GB instance. Then **Run > Run All Lines**



### 3 Deploy Models
Open the file `2_deploy_models.py` in a normal workbench PBJ python3 session. You only need a
2 vCPU / 4 GB instance. Then **Run > Run All Lines**


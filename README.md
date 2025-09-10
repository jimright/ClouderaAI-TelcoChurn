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
probability for a group of customers from a telecoms company. On top that, the model 
can then be interpreted using [LIME](https://github.com/marcotcr/lime). Both the Logistic 
Regression and LIME models are then deployed using CML's real-time model deployment 
capability and finally a basic flask based web application is deployed that will let 
you interact with the real-time model to see which factors in the data have the most 
influence on the churn probability.

By following the notebooks in this project, you will understand how to perform similar 
classification tasks on CML as well as how to use the platform's major features to your 
advantage. These features include **streamlined model experimentation**, 
**point-and-click model deployment**, and **ML app hosting**.

We will focus our attention on working within CML, using all it has to offer, while
glossing over the details that are simply standard data science.
We trust that you are familiar with typical data science workflows
and do not need detailed explanations of the code.
Notes that are *specific to CML* will be emphasized in **block quotes**.

### Initialize the Project
There are a couple of steps needed at the start to configure the Project and Workspace 
settings so each step will run sucessfully. You **must** run the project bootstrap 
before running other steps. If you just want to launch the model interpretability 
application without going through each step manually, then you can also deploy the 
complete project. 

***Project bootstrap***

Open the file `0_bootstrap.py` in a normal workbench python3 session. You only need a 
1 vCPU / 2 GiB instance. Once the session is loaded, click **Run > Run All Lines**. 
This will file will create an Environment Variable for the project called **STORAGE**, 
which is the root of default file storage location for the Hive Metastore in the 
DataLake (e.g. `s3a://my-default-bucket`). It will also upload the data used in the 
project to `$STORAGE/datalake/data/churn/`. The original file comes as part of this 
git repo in the `raw` folder.
  
will end up with a running application.

### 0 Bootstrap
Just to reiterate that you have run the bootstrap for this project before anything else. 
So make sure you run step 0 first. 

Open the file `0_bootstrap.py` in a normal workbench PBJ python3 session. You only need a 
2 vCPU / 4 GB instance. Then **Run > Run All Lines**


### 1 Model Training


Open the file `1_trainStrategy_job.py` in a normal workbench PBJ python3 session. You only need a
2 vCPU / 4 GB instance. Then **Run > Run All Lines**



### 3 Deploy Models
The **[Models](https://docs.cloudera.com/machine-learning/cloud/models/topics/ml-creating-and-deploying-a-model.html)** 
is used top deploy a machine learning model into production for real-time prediction.  
In the lab we will run a script to leveraging cml api to deploy  
Open the file `1_trainStrategy_job.py` in a normal workbench PBJ python3 session. You only need a
2 vCPU / 4 GB instance. Then **Run > Run All Lines**
To 
deploy the model trailed in the previous step, from  to the Project page, click **Models > New
Model** and create a new model with the following details:

* **Name**: Explainer
* **Description**: Explain customer churn prediction
* **File**: 5_model_serve_explainer.py
* **Function**: explain
* **Input**: 
```
{
	"StreamingTV": "No",
	"MonthlyCharges": 70.35,
	"PhoneService": "No",
	"PaperlessBilling": "No",
	"Partner": "No",
	"OnlineBackup": "No",
	"gender": "Female",
	"Contract": "Month-to-month",
	"TotalCharges": 1397.475,
	"StreamingMovies": "No",
	"DeviceProtection": "No",
	"PaymentMethod": "Bank transfer (automatic)",
	"tenure": 29,
	"Dependents": "No",
	"OnlineSecurity": "No",
	"MultipleLines": "No",
	"InternetService": "DSL",
	"SeniorCitizen": "No",
	"TechSupport": "No"
}
```
* **Kernel**: Python 3
* **Engine Profile**: 1vCPU / 2 GiB Memory

Leave the rest unchanged. Click **Deploy Model** and the model will go through the build 
process and deploy a REST endpoint. Once the model is deployed, you can test it is working 
from the model Model Overview page.

_**Note: This is important**_

Once the model is deployed, you must disable the additional model authentication feature. In the model settings page, untick **Enable Authentication**.

![disable_auth](images/disable_auth.png)

* **Subdomain**: churn-app _(note: this needs to be unique, so if you've done this before, 
pick a more random subdomain name)_
* **Script**: 6_application.py
* **Kernel**: Python 3
* **Engine Profile**: 1vCPU / 2 GiB Memory


After the Application deploys, click on the blue-arrow next to the name. The initial view is a 
table of randomly selected from the dataset. This shows a global view of which features are 
most important for the predictor model. The reds show incresed importance for preditcting a 
cusomter that will churn and the blues for for customers that will not.

![table_view](images/table_view.png)

Clicking on any single row will show a "local" interpreted model for that particular data point 
instance. Here you can see how adjusting any one of the features will change the instance's 
churn prediction.


![single_view_1](images/single_view_1.png)

Changing the InternetService to DSL lowers the probablity of churn. *Note: this does not mean 
that changing the Internet Service to DSL cause the probability to go down, this is just what 
the model would predict for a customer with those data points*


![single_view_2](images/single_view_2.png)


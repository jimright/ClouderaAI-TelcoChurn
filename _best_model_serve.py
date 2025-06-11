from collections import ChainMap
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from churnexplainer import ExplainedModel
import pickle
from churnexplainer import CategoricalEncoder
import cml.metrics_v1 as metrics
import cml.models_v1 as models

filename="./models/champion/champion.pkl"
#Load the model save earlier.
loaded_model = pickle.load(open(filename, 'rb'))
filename="./models/champion/ce.pkl"
#Load the model save earlier.
ce = pickle.load(open(filename, 'rb'))

# *Note:* If you want to test this in a session, comment out the line 
#`@cdsw.model_metrics` below. Don't forget to uncomment when you
# deploy, or it won't write the metrics to the database 
cols = (('gender', True),
        ('seniorcitizen', True),
        ('partner', True),
        ('dependents', True),
        ('tenure', False),
        ('phoneservice', True),
        ('multiplelines', True),
        ('internetservice', True),
        ('onlinesecurity', True),
        ('onlinebackup', True),
        ('deviceprotection', True),
        ('techsupport', True),
        ('streamingtv', True),
        ('streamingmovies', True),
        ('contract', True),
        ('paperlessbilling', True),
        ('paymentmethod', True),
        ('monthlycharges', False),
        ('totalcharges', False))

@models.cml_model(metrics=True)
# This is the main function used for serving the model. It will take in the JSON formatted arguments , calculate the probablity of 
# churn and create a LIME explainer explained instance and return that as JSON.
def explain(args):
    data = pd.json_normalize(args)
    # This is Mike's lovely short hand syntax for looping through data and doing useful things. I think if we started to pay him by the ASCII char, we'd get more readable code.
    data = data[[c for c, _ in cols]]
    catcols = (c for c, iscat in cols if iscat)
    for col in catcols:
      data[col] = pd.Categorical(data[col])
    

    X = ce.fit_transform(data)
    probability = loaded_model.predict(X)
      
    
    return {
        'probability': probability[0]
        }
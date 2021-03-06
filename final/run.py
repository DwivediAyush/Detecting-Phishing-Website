#!/usr/bin/env python
# coding: utf-8

# In[5]:


from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import GridSearchCV
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv("phishcoop.csv")
dataset = dataset.drop('id', 1) #removing unwanted column

x = dataset.iloc[ : , :-1].values
y = dataset.iloc[:, -1:].values

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.25, random_state =0 )
parameters = [{'n_estimators': [100, 700],
    'max_features': ['sqrt', 'log2'],
    'criterion' :['gini', 'entropy']}]

grid_search = GridSearchCV(RandomForestClassifier(),  parameters,cv =5, n_jobs= -1)
grid_search.fit(x_train, y_train)
#printing best parameters
print("Best Accurancy =" +str( grid_search.best_score_))
print("best parameters =" + str(grid_search.best_params_))
classifier = RandomForestClassifier(n_estimators = 100, criterion = "gini", max_features = 'log2',  random_state = 0)
classifier.fit(x_train, y_train)

#predicting the tests set result
y_pred = classifier.predict(x_test)

# In[7]:


import Datasetgen as data


# In[8]:



def run(url):

    try:
        #checking and predicting
        checkprediction = data.main(url)
        #checkprediction=[[0, -1, -1, -1, 1, 1, -1, 1, 0, 0, -1, -1, 1, 1, 0, 0, -1, 0, -1, -1, -1, -1, 1, 0, 0, 1, 1, 1, -1, -1]]
        prediction = classifier.predict(checkprediction)
        if prediction==1:
            return "Warning The website is harmfull for you"
        else:
            return "COOL! You can excess the website" +"\n"+ url

    except:
        return "The website you entered does not exist"
# In[9]:





# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix


# In[2]:


dataset = pd.read_csv("phishcoop.csv")
dataset = dataset.drop('id', 1) #removing unwanted column

x = dataset.iloc[ : , :-1].values
y = dataset.iloc[:, -1:].values


# In[4]:


x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.25, random_state =0 )

#fitting logistic regression 
classifier = LogisticRegression(random_state = 0)
classifier.fit(x_train, y_train)

#predicting the tests set result
y_pred = classifier.predict(x_test)


# In[6]:



cm = confusion_matrix(y_test, y_pred)
print(cm)
score = classifier.score(x_test, y_test)
print(score*100,"%")


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





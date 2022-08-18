#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import MultinomialNB

import sys
sys.path.append('..')
from src.data import load_data
from src.metric import classificationSummary, confusion_matrix

# If you prefer a different style, pick from this list
# plt.style.available
pd.set_option('display.precision',4)
plt.style.use('fivethirtyeight')
plt.rcParams["figure.figsize"] = (20, 10)


# # Automobile Accidents <a id='auto-accidents'></a>
# 
# The file, [accidentsFull.csv](../data/accidentsFull.csv), contains information on 42k actual accidents in the US in 2001.  There are three levels of injury provided NO INJURY, INJURY, FATALITY.  Your job, if you choose to accept it, is to use the predictors available to develop a model that can determine whether there was an injury at an accident (INJURY or FATALITY).

# In[ ]:


accidents_df = load_data('accidentsFull')
accidents_df.head(10)


# In[ ]:


# Create dummy variable for the target
accidents_df.loc[accidents_df.MAX_SEV_IR>0, "INJURY"]='yes'
accidents_df.loc[accidents_df.MAX_SEV_IR==0, "INJURY"]='no'
accidents_df.INJURY


# In[ ]:


# Determine naive rule
accidents_df.INJURY.value_counts()/len(accidents_df)


# In[ ]:


# predictors and outcome
predictors = ['HOUR_I_R', 'ALIGN_I', 'WRK_ZONE', 'WKDY_I_R', 'INT_HWY', 'LGTCON_I_R', 'PROFIL_I_R', 'SPD_LIM',
              'SUR_COND', 'TRAF_CON_R', 'TRAF_WAY', 'WEATHER_R']
outcome = 'INJURY'
# get dummies
X = pd.get_dummies(accidents_df[predictors])
y = accidents_df['INJURY'].astype('category')
classes = list(y.cat.categories)
# partition the data
X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.40, random_state=1)
# fit the model
accidents_nb = MultinomialNB(alpha=0.01)
accidents_nb.fit(X_train, y_train)

# predict probabilities for training and validation sets
predProb_train = accidents_nb.predict_proba(X_train)
predProb_valid = accidents_nb.predict_proba(X_valid)
# predict class memberships for validation data
y_train_pred = accidents_nb.predict(X_train)
y_valid_pred = accidents_nb.predict(X_valid)

# confusion matrix
# training
print('training data\n')
classificationSummary(y_train, y_train_pred, class_names=classes)
# validation 
print('\nvalidation data\n')
classificationSummary(y_valid, y_valid_pred, class_names=classes)


# In[ ]:


# Overall error and improvement
naive_error = 1-accidents_df.INJURY[accidents_df.INJURY=='yes'].count()/len(accidents_df)
validation_error = (1-accuracy_score(y_valid,y_valid_pred))
print(f'Overall misclassification for naive rule set {naive_error:.4f}')
print(f'Overall misclassification for validation set {validation_error:.4f}')
print(f'Model improvement: {100*(naive_error-validation_error)/naive_error:.2f}%')


# <div align='center'/>
# 
# [Back to TOC](./00-Introduction.ipynb)&emsp;&emsp;[<- Back: Classification](./30-Classification.ipynb)&emsp;&emsp;[Next: Estimation and Prediction ->](./40-EstimationPrediction.ipynb)

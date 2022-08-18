#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append('..')
from src.data import load_data
from src.metric import classificationSummary
from sklearn.model_selection import (
    GridSearchCV,
    train_test_split, 
)
from sklearn.preprocessing import StandardScaler

pd.set_option('display.precision',4)
plt.style.use('fivethirtyeight')
pd.set_option('display.max_rows', 200)
pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 1000)
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"


# # Ensembling
# Ensembling refers to learning in which multiple models are used to produce a single outcome.  Often these models are considered "weak learners" because they intentionally try to underfit so that the final model is not overfit when the models are combined.
# 
# There are generally two different types of ensembling:
# *   __Averaging__ - in these approaches multiple models are created and the outcomes are aggregated into a final result.  The aggregation made be via voting or by averaging the responses.
#     *  _Examples include_: Bagging methods, and Randomized Trees
# *   __Boosting__ - alternatively boosting methods take weaker models and run them in series.  This means that the output of each model provides a factor for subsequent models to use in the learning task.  
#     *  _Examples include_: AdaBoost, Gradient Tree Boosting

# In[ ]:


# German Credit
# Assume all columns are categorical
credit_df = load_data('GermanCredit', index_col="OBS#",dtype='category')
credit_df.rename(columns={"RADIO/TV":"RADIO_TV","CO-APPLICANT":"CO-APPLICANT"}, inplace=True)

credit_df = credit_df.astype({'DURATION':float,'AMOUNT':float, 'INSTALL_RATE':float, 'AGE':float,'NUM_CREDITS':float,'NUM_DEPENDENTS':float})
credit_num_columns = credit_df.select_dtypes(include='number').columns
credit_cat_columns = ['NEW_CAR', 'USED_CAR', 'FURNITURE', 'RADIO_TV', 'EDUCATION', 'RETRAINING', 'MALE_DIV', 'MALE_SINGLE', 'MALE_MAR_or_WID', 'CO-APPLICANT', 'GUARANTOR',  'REAL_ESTATE', 'PROP_UNKN_NONE', 'OTHER_INSTALL', 'RENT', 'OWN_RES', 'TELEPHONE', 'FOREIGN']
credit_ord_columns = ['CHK_ACCT','HISTORY','SAV_ACCT','EMPLOYMENT','PRESENT_RESIDENT','JOB']
credit_df.head()


# Good for us we have a couple of ways to use Ensembling to make this work.  We can use the built in essemble methods like [BaggingClassifier](https://scikit-learn.org/stable/modules/ensemble.html#bagging).  These classifiers do all the heavy lifting for us, we specify the algorithm for the weak learner and let the BaggingClassifier manage the splitting and aggregation.

# In[ ]:


from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier

X_credit = credit_df.drop(columns='RESPONSE')
y_credit = credit_df.RESPONSE

X_credit_train, X_credit_valid, y_credit_train, y_credit_valid = train_test_split(X_credit, y_credit, test_size=.40, random_state=123)


# In[ ]:


# Bagging with DecisionTrees
clf_tree = DecisionTreeClassifier()
clf_bag = BaggingClassifier(DecisionTreeClassifier(),n_estimators=10)

clf_tree.fit(X_credit_train,y_credit_train)
clf_bag.fit(X_credit_train,y_credit_train)

y_credit_pred_valid_tree = clf_tree.predict(X_credit_valid)
y_credit_pred_valid_bag = clf_bag.predict(X_credit_valid)

print(f'Decision Tree Results')
classificationSummary(y_credit_valid,y_credit_pred_valid_tree)
print(f'Bag Results')
classificationSummary(y_credit_valid,y_credit_pred_valid_bag)


# Alternatively we can use some of the Boosting methods like [AdaBoost](https://scikit-learn.org/stable/modules/ensemble.html#adaboost) or [GradientTreeBoosting](https://scikit-learn.org/stable/modules/ensemble.html#gradient-boosting).  While both are good in their results, one of more popular alternatives which is usually at the top of many Kaggle competitions is [XGBoost](https://xgboost.readthedocs.io/en/stable/install.html#python).  There are a few things to keep in mind when using XGBoost though:
# - Categorical fields must be encoded
# - Numeric features need to be standardized

# In[ ]:


import xgboost as xgb
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

pre_processor = ColumnTransformer(transformers=[
    ('numeric',StandardScaler(),credit_num_columns),
    ('categories',OneHotEncoder(),credit_cat_columns),
    ('ordinals',OneHotEncoder(),credit_ord_columns)])

X_credit_processed = pre_processor.fit_transform(X_credit)
y_credit_processed = LabelEncoder().fit_transform(y_credit)

X_credit_xgb_train, X_credit_xgb_valid, y_credit_xgb_train, y_credit_xgb_valid = train_test_split(X_credit_processed, y_credit_processed, train_size=.40, random_state=123)


# In[ ]:


clf_xgb = xgb.XGBClassifier(use_label_encoder=False,eval_metric='auc',objective='binary:logistic',verbosity=0)
clf_xgb.fit(X_credit_xgb_train,y_credit_xgb_train)
y_credit_pred_valid_xgb = clf_xgb.predict(X_credit_xgb_valid)

print(f'XGBoost Results')
classificationSummary(y_credit_xgb_valid,y_credit_pred_valid_xgb)


# In[ ]:


# This is going to take a long time to run, so pick your parameters wisely!
num_splits = 5
param_grid = {
    "max_depth": [3, 4, 5, 7],
    "learning_rate": [0.1, 0.01, 0.05],
    #"gamma": [0, 0.25, 1],
    # "reg_lambda": [0, 1, 10],
    # "scale_pos_weight": [1, 3, 5],
    "subsample": [0.5],
    # "colsample_bytree": [0.5],
}
# Go through an exhaustive search by combining all the variables specified in the
clf_xgb_2 = xgb.XGBClassifier(use_label_encoder=False,eval_metric='auc',objective='binary:logistic',verbosity=0)
clf_xgb_grid = GridSearchCV(clf_xgb_2, cv=num_splits, param_grid=param_grid, n_jobs=-1)
clf_xgb_grid.fit(X_credit_xgb_train,y_credit_xgb_train)
y_credit_pred_valid_xgb_grid = clf_xgb.predict(X_credit_xgb_valid)

print(f'XGBoost Results')
classificationSummary(y_credit_xgb_valid,y_credit_pred_valid_xgb_grid)


# In[ ]:


xgb_best_estimator = clf_xgb_grid.best_estimator_
best_max_depth = xgb_best_estimator.get_params()["max_depth"]
best_learning_rate = xgb_best_estimator.get_params()["learning_rate"]
print(f'{best_max_depth=}, {best_learning_rate=}')

# We could also then use the best_estimator to deploy
xgb_best_estimator.predict(X_credit_xgb_valid)


# <div align='center'/>
# 
# [Back to TOC](./00-Introduction.ipynb)

#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.neighbors import KNeighborsClassifier


import sys
sys.path.append('..')
from src.data import load_data, load_excel, TRUE_VALUES, FALSE_VALUES

pd.set_option('display.precision',4)
pd.set_option('display.max_rows', 200)
pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 1000)
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"


# # Pipelines
# Pipeline can be used to chain multiple estimators into one. This is useful as there is often a fixed sequence of steps in processing the data, for example feature selection, normalization and classification. Pipeline serves multiple purposes here:
# 
# __Convenience and encapsulation__
#     <br/>You only have to call fit and predict once on your data to fit a whole sequence of estimators.
# 
# __Joint parameter selection__
#     <br/>You can grid search over parameters of all estimators in the pipeline at once.
# 
# __Safety__
#     <br/>Pipelines help avoid leaking statistics from your test data into the trained model in cross-validation, by ensuring that the same samples are used to train the transformers and predictors.
# 
# All estimators in a pipeline, except the last one, must be transformers (i.e. must have a transform method). The last estimator may be any type (transformer, classifier, etc.).
# 
# *(source: [sklearn documentation](https://scikit-learn.org/stable/modules/compose.html#pipeline))*
# 
# We can use a pipeline for instance to standardize our data prior to running the Nearest Neighbors classifier.

# In[ ]:


# Import and clean-up the heart disease dataset
heart_df = load_excel('HeartDisease_Cleveland',
                    dtype={'FBS': bool, 'EXANG': bool}, true_values=TRUE_VALUES,
                    false_values=FALSE_VALUES, na_values=['?'])
heart_df.dropna(inplace=True)
heart_df['DIAG'] = (heart_df.NUM > 0)
heart_df.drop(columns=['NUM'], inplace=True)


# In[ ]:


MAX_NEIGHBORS = 25
X = heart_df.drop(columns='DIAG')
y = heart_df['DIAG']
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.4, random_state=1)
clf = KNeighborsClassifier(n_neighbors=MAX_NEIGHBORS, weights='uniform', algorithm='auto', n_jobs=-1)

pipe = make_pipeline(StandardScaler(),clf)
pipe.fit(X_train,y_train)
pipe.score(X_test,y_test)


# In[ ]:


# We can also name the steps in the pipeline. 
# This is useful if we need to send parameters to different steps in the pipeline
# Accessing parameters of the pipeline by name takes the following form:
#  pipeline_step_name + '__' + parameter name
pipe = Pipeline([('scaler', StandardScaler()), 
                ('classifer', clf)])
params = {'classifer__n_neighbors':25}
pipe.set_params(**params)
pipe.fit(X_train,y_train)
pipe.score(X_test,y_test)


# Pipelines can get complicated, fortunately when we are working in Jupyter notebooks we can see an HTML representation of the final pipeline

# In[ ]:


from sklearn import set_config
set_config(display='diagram')
pipe


# In[ ]:


numeric_features = ['AGE','TRESTBPS','THALACH','CA','OLDPEAK']
numeric_transformer = Pipeline(
    steps=[("imputer", SimpleImputer(strategy="median")), ("scaler", StandardScaler())]
)

categorical_features = ['SEX','CP','FBS','RESTECG','EXANG','SLOPE','THAL']
categorical_transformer = OneHotEncoder(handle_unknown="ignore")

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features)]
)
pipe2 = Pipeline([("preprocessor",preprocessor),("classifier",clf)])


# In[ ]:


X2 = heart_df.drop(columns='DIAG')
y2 = heart_df['DIAG']
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, train_size=0.4, random_state=1,stratify=y2)
pipe2.fit(X2_train,y2_train)
pipe2.score(X2_test, y2_test)

# Note our score improves likely because we stratified the split in this effort


# <div align='center'/>
# 
# [Back to TOC](./00-Introduction.ipynb)

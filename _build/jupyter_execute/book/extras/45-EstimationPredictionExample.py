#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler
from sklearn import set_config
import seaborn as sns
import matplotlib.pyplot as plt
import sys
sys.path.append('..')
from src.data import load_data, convert_to_bool, convert_to_ordinal
from src.feature_selection import FeatureImportance

pd.set_option('display.precision',4)
plt.rcParams["figure.figsize"] = (20, 10)
plt.style.use('fivethirtyeight')
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"


# # Predicting the price of used cars
# In the data file [ToyotaCorrolla](../data/ToyotaCorolla.csv) we have data on used Toyotas from late 2004 in the Netherlands.  The goal is to predict the price based on it's specifications.
# 
# Note there has been some significant EDA done ahead of time to reduce the number of columns and find interesting data.
# - Cylinders: dropped because all the values are 4

# In[3]:


#
# Let's start by checking out the data
cars_df = load_data('ToyotaCorolla',index_col='Id')
cars_df = cars_df.drop(columns=['Cylinders','Model'])
cars_df.shape


# _NOTE:_ Maybe it's worth noting (many notebooks leave these steps out because they are cumbersome and more complex to explain than to just do).  In a different notebook, I took a good look at the data to determine how to ensure that the data types were correct for each column.  You could do this in Excel (if your data is small enough) or you might use another tool where you can get a quick sample and try to understand the data.  For me, I took a look at the the types of data `cars_df.dtypes` then since I saw that many of the columns had just a 1 or a 0, I figured these were `boolean`.  Then looking at the names of the columns, like `Mfg_Year` and `Mfg_Month`, even though they are numbers, I felt it would be best to convert them what they are _ordinal_ values.  The other reason that this doesn't get much description is because the process is usually a bit non-linear and repeatitive.  For instance, once I determined the booleans, I converted them and then started looking for categoricals.  This would have taken 4 notebook cells (1. find bools, 2. convert columns to bool, 3. find non-bool number columns, 4. convert to ordinal).  As a reader you are really only interested in seeing the conversion of columns in a single cell instead of all the work behind it.
# 
# Another example of the non-linear workflow, I discovered `Cylinders` as a unary value (all cars here have 4 cylinders).  If this column was dropped later in the notebook, then an update to the categorical columns as well.  Instead, I'll just let you know that I found this in a later step.  To be more clear, it was dropped immediately at the start before creating the categorical columns.  Additionally, I found later in the model that there are 300+ different car models in a dataset (within just 1400 rows), so this isn't going to be helpful later on either.

# In[4]:


cars_df.dtypes


# In[5]:


cars_df = convert_to_bool(cars_df,['Met_Color', 'Automatic', 'Mfr_Guarantee', 'BOVAG_Guarantee', 'ABS',
       'Airbag_1', 'Airbag_2', 'Airco', 'Automatic_airco', 'Boardcomputer',
       'CD_Player', 'Central_Lock', 'Powered_Windows', 'Power_Steering',
       'Radio', 'Mistlamps', 'Sport_Model', 'Backseat_Divider', 'Metallic_Rim',
       'Radio_cassette', 'Parking_Assistant', 'Tow_Bar'])

ord_columns = ['Model','Mfg_Month', 'Mfg_Year','Doors', 'Gears','Fuel_Type',"Color"]

cars_df = convert_to_ordinal(cars_df,ord_columns)

# Take out the target column before determining the number columns
num_columns = cars_df.drop(columns='Price').select_dtypes(include='number').columns
bool_columns = cars_df.select_dtypes(include='bool').columns
cat_columns = cars_df.select_dtypes(include=['object','category']).columns

print(num_columns)
print(bool_columns)
print(cat_columns)

def remove_column(df, column_collection):
       '''
       Drop a column from the dataframe, as well as from the list associated with the column
       '''
       pass


# ## More EDA
# Next, I'm going to do a few more steps to see if I can determine anything interesting about the data.  I'll start with a cumulative density plot of the price.  This helps me to see what the range of prices is and I've also plotted to the IQR's, this can be helpful to see how spread out the prices are.

# In[6]:


iq1,iq2,iq3 = cars_df.Price.describe()[4:7]
sns.kdeplot(cars_df.Price, cumulative=True);
y=np.full(len(cars_df.Price.cumsum()),0.5)
plt.axhline(y=0.5,color='red',linestyle='--');
plt.axhline(y=0.75,color='green',linestyle='--');
plt.axhline(y=0.25,color='green',linestyle='--');
plt.text(x=0.1*max(cars_df.Price),y=0.51,s=f'Median: {iq2}');
plt.text(x=0.1*max(cars_df.Price),y=0.76,s=f'IQ3: {iq3}');
plt.text(x=0.1*max(cars_df.Price),y=0.26,s=f'IQ1: {iq1}');
plt.show();

cars_df.Price.describe()


# In[8]:


# Next, I want to see if  there are cases where there are too many of one class (bool or categorical)
bool_df = cars_df[bool_columns].apply(pd.value_counts).T
bool_df.columns = ['F','T']
bool_df['% True'] = bool_df['T']/bool_df.sum(axis=1)
bool_df.sort_values(by='% True')
cars_df[cat_columns].nunique()


# Looking at the values above, it seems like `Parking_Assist` is pretty much useless in terms of determining the price since there are only 4 cars with this feature - I'll remove it from the categoricals.

# In[9]:


# Now let's see how these categoricals relate to price
fig, axs = plt.subplots(nrows=3, ncols=2,figsize=(20,25));
for ax, c in zip(axs.flat,cat_columns[1:]):
    sns.boxplot(data=cars_df, x=c,y='Price',ax=ax);


# In[8]:


# We see above that it looks like these values may have some interest (certainly the newer the car the more valuable)
# There seems to be a small number of 2-doors let's see
cars_df['Doors'].value_counts()


# In[9]:


# With only 2 samples of 2-door cars, we can safely drop these
cars_df = cars_df.query('Doors>2')


# In[10]:


# Next I noticed that the price seems to differ for each color pretty significantly
colors_df = cars_df.groupby('Color')['Price'].mean().sort_values(ascending=False)
colors_df.columns = ['Color','MeanPrice']
colors_df


# ## Feature importance
# Many of the notebooks you see or some of the examples, skip the step where show how they determined that they only want to use 6-8 of the features that are provided.  I'm going to start by looking at which features are best using a DT regressor, a LinearModel with ForwardSelection and Backward elimination, once we've done this - we can start again by dropping out the features that don't seem to have any value

# In[15]:


from sklearn.tree import DecisionTreeRegressor
from sklearn import set_config
set_config(display='diagram')

X = cars_df.drop(columns='Price')
y= cars_df['Price']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size =0.2)
cat_cols = ['Mfg_Month','Fuel_Type','Color']
ord_cols = ['Mfg_Year','Doors', 'Gears']
bool_cols = X_train.select_dtypes(include='bool').columns
num_cols = X_train.select_dtypes(include=np.number).columns

# We're going to setup our column transformer as pre-processing step for the follow-on steps.
pre_processing = ColumnTransformer([
    ('cat_encoder', OneHotEncoder(), cat_cols),
    ('ord_encoder', OrdinalEncoder(handle_unknown='use_encoded_value',unknown_value=99), ord_cols),
    ('num_encoder', StandardScaler(),num_cols)])


# In[12]:


pipe = Pipeline([("pp",pre_processing), ("dtr",DecisionTreeRegressor(random_state=123))])

pipe.fit(X_train,y_train)
fi= FeatureImportance(pipe)
fn = fi.get_feature_names()
top_10_tree = fi.get_feature_importance().sort_values(ascending=False)[:10]
top_10_tree.name='top_10_tree'
top_10_tree


# Seems like the `Age`, `KM`, `HP` and `Weight` seem to be the most important variables.  Let's take a look using a different method and see which features float to to the top.  Here we'll try a forest of trees, this ought to give us an even better idea of which parameters are of the most value.

# In[13]:


# And now one last try using GridSearch to find the best transformer
param_grid = {'regressor__max_depth': [3,4,5]}

pipe = Pipeline([("pp",pre_processing), ("regressor",DecisionTreeRegressor(random_state=123))])
reg = GridSearchCV(pipe,param_grid=param_grid)
reg.fit(X_train, y_train)
best= reg.best_estimator_

fi= FeatureImportance(best)
top_10_grid = fi.get_feature_importance().sort_values(ascending=False)[:10]
top_10_grid.name='top_10_grid'
top_10_grid


# In[19]:


# Now that we have both using a standard regressor and using GridSearch, let's compare
pd.concat([top_10_grid,top_10_tree],axis=1)


# Knowing what the top ten differentiating factors are help us to narrow the focus of our predictive models going forward.  Since we know for instance that a multiple linear regression model will continually improve as we add more variables (maybe insignificantly) and if we want to be able to explain our model, keeping to the most impactful variables most helpful.
# 
# At this point, we could just decide to keep a managable number of factors and restart our entire process from scratch.  (Frankly this is what happens when alot of the samples are explained.  All the work that we've done here so far, is left out so that the learner is not subjected to the steps which simply eliminate useless information.)  Since all the work has been done, we are just going to move on keeping in all the features and letting the algorithm reduce the featureset as appropriate.

# ## Making predictions
# At this point we have done a thorough job of exploring the data, finding possible outliers, eliminating features and  coming up with a candidate list of good features.  We'll try a couple of different approaches finding a good predictive fit for the price.

# In[60]:


X_cars = cars_df.drop(columns='Price')
y_cars = cars_df['Price']

c_cols = ['Mfg_Month','Fuel_Type','Color']
o_cols = ['Mfg_Year','Doors', 'Gears']
b_cols = X_train.select_dtypes(include='bool').columns
n_cols = X_train.select_dtypes(include=np.number).columns

X_train, X_test, y_train, y_test = train_test_split(X_cars,y_cars,test_size =0.2)

# We're going to setup our column transformer as pre-processing step for the follow-on steps.
pre_processing_transform = ColumnTransformer([
    ('cat_encoder', OneHotEncoder(), c_cols),
    ('ord_encoder', OrdinalEncoder(handle_unknown='use_encoded_value',unknown_value=99), o_cols),
    ('num_encoder', StandardScaler(),n_cols)])

X_train.columns.sort_values()


# In[66]:


ohe = OneHotEncoder()
ohe.fit_transform(X_train[c_cols])

ode = OrdinalEncoder()
ode.fit_transform(X_train[o_cols])


# In[59]:


param_grid2 = {'reg__max_depth': [3,4,5]}
dtr = DecisionTreeRegressor(random_state=234)
pipe2 = Pipeline([('pre',pre_processing_transform), ("reg",dtr)])
dt_reg = GridSearchCV(pipe2,param_grid=param_grid2)
dt_reg.fit(X_train, y_train)
best= dt_reg.best_estimator_
best


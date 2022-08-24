#!/usr/bin/env python
# coding: utf-8

# # Exploratory Data Analysis
# Telling the future is the exciting part of data mining.  Everyone wants to build the best model that can be the most accurate prediction of future results or have the best explanation for why the past occurred the way it has.  But in order to have a valuable model, it is important to understand the data, determine the shape, understand the predictors and the target variables (if any).  Understanding the scale of these values and their relationship to each other can save hours of testing different modelling techniques and parameter tuning.
# 
# The next cell is one that will appear in some configuration as the first in nearly every notebook.  It imports the key libraries we are going to use in our analysis and model building.  In the first case, we will depend on pandas and numpy for our data manipulation and we'll leverage matplotlib as our graphical library.  We'll also use the seaborn library to show off a few plots and visuals that are not quite as readily accessible with the matplotlib library.

# In[1]:


# Import relevant libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns
import sys
sys.path.append('..')
from src.data import load_data

# If you are using a 'light' them
# comment out or remove this line
pd.set_option('display.precision',4)
plt.style.use('dark_background')


# ## Boston Housing Dataset
# Let's take a look at some basic data manipulation with pandas and understand how to get some data to work with.  In all of our examples, we'll use a pretty standard text format called (CSV) or comma-separated-values files.  This format is readable by nearly every statistical software package and by humans.  The first row is typically the name of the columns and each line of the file is a row of data with the values separated by commas.  The pandas library supports many different ways to load up a dataframe, which we will use as the primary mechanism for manipulating data in these notebooks.
# 
# ### Business Context
# Each record in the database describes a Boston suburb or town. The data was drawn from the Boston Standard Metropolitan Statistical Area (SMSA) in 1970. The attributes are deﬁned as follows (taken from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/machine-learning-databases/housing/)):
# 
# - **CRIM**: per capita crime rate by town
# - **ZN**: proportion of residential land zoned for lots over 25,000 sq.ft.
# - **INDUS**: proportion of non-retail business acres per town
# - **CHAS**: Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)
# - **NOX**: nitric oxides concentration (parts per 10 million)
# - **RM**: average number of rooms per dwelling
# - **AGE**: proportion of owner-occupied units built prior to 1940
# - **DIS**: weighted distances to ﬁve Boston employment centers
# - **RAD**: index of accessibility to radial highways
# - **TAX**: full-value property-tax rate per 10,000
# - **PTRATIO**: pupil-teacher ratio by town
# - **B**: 1000(Bk−0.63)2 where Bk is the proportion of blacks by town
# - **LSTAT**: % lower status of the population
# - **MEDV**: Median value of owner-occupied homes in 1000s
# - **CAT.MEDV**: Is median value of owner-occupied home in tract above $30k (CAT.MEDV = 1) or not (CAT.MEDV = 0)
# 
# We can see that the input attributes have a mixture of units.

# In[2]:


# Load up the housing dataset
housing_df = load_data('BostonHousing')
housing_df


# ### Exploratory Data Analysis (EDA)
# Once we understand the business content, then we want to take a look at our data and see what else we can discover about the relationships between our target variable and the other independent factors.  
# 
# We'll end up doing quite a bit of EDA, usually we'll start with some EDA, clean up the data and munge it into an appropriate format for modeling and then we'll want to check out the results.  It pays to have a good grasp of a plotting library and some techniques to make this process go a bit faster.  There are a few libraries which are pretty common place in the data science with python world, including seaborn and matplotlib.  Many new libraries have been introduced recently as well that add much more interactive opportunities with less coding.
# 

# In[3]:


# Change the column to be more convenient (notice the space between . MEDV)
housing_df.rename(columns={'CAT. MEDV':'CAT_MEDV'},inplace=True)
# Take a look at the first few rows of data
housing_df.head()


# In[4]:


# check the rows and columns
housing_df.shape


# We see from the ouput about that we have 506 rows and 14 columns, but we can't see all the columns - let's check out the column names and get an idea of the some descriptive statistics for each numerical column)

# In[5]:


housing_df.describe()


# In[6]:


housing_df.dtypes


# Now that we have an idea of the numerical fields.  We should check out the distribution of the CAT_MEDV field to see how these are laid out.

# In[7]:


print (housing_df.value_counts(['CAT_MEDV']))
# and also the percentages
housing_df.value_counts(['CAT_MEDV'])/len(housing_df)


# We can now take a look at a couple of values as they relate to our target variable (CAT_MEDV).

# In[8]:


housing_df.plot.scatter(x='LSTAT', y='MEDV', legend=False)


# In[9]:


ax=housing_df.groupby('CHAS').mean().MEDV.plot(kind='bar')
ax.set_ylabel('Avg. MEDV')


# In[10]:


dataForPlot= housing_df.groupby('CHAS').mean()['CAT_MEDV']*100
ax=dataForPlot.plot(kind='bar', figsize=[5,3])
ax.set_ylabel('% of CAT.MEDV')


# ### Determining the interaction between a set of variables
# Sometimes it is helpful to see many more dimensions of the data at once.  We can use color, size, shape and axises to show several dimensions, and one more commonly overlooked approach is to use faceting as yet another dimension.  Let's take a look at how the age of the houses vary by the relativeness to the Charles river.  
# 
# From here we can see that, as previously, there are many more homes not on the Charles River and also that the age of the homes is skewed heavily toward the older home ages.
# 
# (Check out the extra notebook [Visualization Samples](visualizationSamples.ipynb) to see another library and possible visualizations.) 

# In[11]:


g = sns.FacetGrid(housing_df, col='CHAS')
g.map_dataframe(sns.histplot,x='AGE')


# We may also be interested in the relationship between a set of the variables so that we can identify which ones may prove to be over-influencing a regression model.  For this we can use two approaches, first we'll look at a set of charts that are related in a pair-wise chart or a correlation map.  First a pairwise graph.  A pairwise graph shows the relationship between these 4 different variables to each other in one simple clean chart.

# In[12]:


# setup a small subset of data
df = housing_df[['CRIM','INDUS','LSTAT',"RM","MEDV"]]
sns.pairplot(df)


# Looking at the pair plots, it seems that we have a very clear relationship between RM and MEDV, an inverse linear relationship between LSAT and RM and also a slightly or maybe non-linear relationship between LSTAT and MEDV.
# 
# Let's take a look and see if we can find any correlations

# In[13]:


print(housing_df.corr())
sns.heatmap(df.corr(),  fmt='.2f',
    annot=True,
    annot_kws={'size': 15},
    cmap='YlGnBu')


# In[14]:


correlationMatrix = df.corr()
# Convert our correlationMatrix to a one-dimensional array
correlationMatrix = correlationMatrix.unstack()
correlationMatrix[abs(correlationMatrix) > 0.7]


# ## Other datasets that are of interest for EDA
# * [Amtrack](../data/Amtrak.csv) - includes data for timeseries analysis
# * [Bankruptcy](../data/Bankruptcy.csv) - lots of factors to consider
# * [Motor Vehicle Collisions](../data/NYPD_Motor_Vehicle_Collisions_1000.csv) - includes lat/long, useful for mapping visuals
# 
# ## Other tools for EDA
# You may find the notebook [Other Tools for EDA](311-OtherToolsForEDA.ipynb) an interesting tour as well.

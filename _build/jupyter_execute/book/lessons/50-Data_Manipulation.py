#!/usr/bin/env python
# coding: utf-8

# # Introduction
# The purpose of this lesson is to expose students to libraries for preparing and manipulating "rectangular" data files (that is data which has both rows and columns, where each row has the same number of columns).

# The next cell is one that will appear in some configuration as the first in nearly every notebook.  It imports the key libraries we are going to use in our analysis and model building.  In the first case, we will depend on pandas and numpy for our data manipulation and we'll leverage matplotlib as our graphical library.  We'll also use the seaborn library to show off a few plots and visuals that are not quite as readily accessible with the matplotlib library.

# In[ ]:


# Setup code
# Import relevant libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns
import sys
sys.path.append('..')
from src.data import load_data, convert_to_bool

# Limit the precision to 4 significant digits
pd.set_option('display.precision',4)


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
# - **CAT. MEDV**: Is median value of owner-occupied home in tract above $30k (CAT.MEDV = 1) or not (CAT.MEDV = 0)
# 
# We can see that the input attributes have a mixture of units.

# In[ ]:


# Load up the housing dataset
housing_df = load_data('BostonHousing')
# Change the column to be more convenient (notice the space between . MEDV)
housing_df.rename(columns={'CAT. MEDV':'CAT_MEDV'},inplace=True)
convert_to_bool(housing_df, 'CAT_MEDV',inplace=True)
housing_df


# # Inspect data
# One of the first things we want to do in our process is to take a look at the data we have and see what kinds of issues we might be dealing with.  For simple datasets, this can be a quick glance at a table of data, for move complex datasets or issues it will be helpful to use some kind of graphical analysis.
# 
# In the example above we see just 10 rows of the data (the first 5 and the last 5).  We can also inspect a few more from the front and a few more in the back using `head()` and `tail()`.
# 

# In[ ]:


housing_df.head(10)


# In[ ]:


housing_df.tail(10)


# We can clearly see that the dataset has 505 rows ( the number on the side is the index and shows us such) and we have already been told how many columns we have.  But we can also use a few handy features to get this information from our dataset.  

# In[ ]:


# Shape tells us the number of rows and columns
housing_df.shape


# We see from the ouput about that we have 506 rows and 14 columns, but we can't see all the columns - let's check out the column names and get an idea of the some descriptive statistics for each numerical column)

# In[ ]:


housing_df.describe()


# We can see from our data dictionary, provided above, that `CAT_MEDV` is meant to be a categorical value (boolean)- not a numeric value.  So the descriptive statistics for it don't make much sense.  We can see however that there are 2 unique values (good, True/False) that False is the most common and it occurs 422 out of of 506 times.

# ## Quick plots and charts
# We've got some interesting data here and we can get some quick plots to see how the data is distributed.  For instance, we might be interested in how old the houses are are or what the crime stats are like.  With this we can use the built-in dataframe functions for plotting.

# In[ ]:


# It's always safe to use the `index` method to get a particular column
housing_df['AGE'].hist()


# In[ ]:


housing_df['CRIM'].hist()


# We can also use the handy [seaborn](https://seaborn.pydata.org/) library which gives us a bit more control over the output.  There is lots and lots of examples of using the seaborn library on the website with a great tutorial.

# In[ ]:


sns.histplot(data=housing_df,x='INDUS',color='yellow').set_title('proportion of non-retail business acres per town')


# ### Determining the interaction between a set of variables
# Sometimes it is helpful to see many more dimensions of the data at once.  We can use color, size, shape and axises to show several dimensions, and one more commonly overlooked approach is to use faceting as yet another dimension.  Let's take a look at how the age of the houses vary by the relativeness to the Charles river.  
# 
# From here we can see that, as previously, there are many more homes not on the Charles River and also that the age of the homes is skewed heavily toward the older home ages.
# 
# (Check out the extra notebook [Visualization Samples](../extras/visualizationSamples.ipynb) to see another library and possible visualizations.) 

# In[ ]:


# Show a scatterplot relating LSTAT to MEDV
housing_df.plot.scatter(x='LSTAT', y='MEDV', legend=False)


# In[ ]:


sns.boxplot(data=housing_df,x='CHAS',y='LSTAT')


# We may also be interested in the relationship between a set of the variables so that we can identify which ones may prove to be over-influencing a regression model.  For this we can use two approaches, first we'll look at a set of charts that are related in a pair-wise chart or a correlation map.  First a pairwise graph.  A pairwise graph shows the relationship between these 4 different variables to each other in one simple clean chart.

# In[ ]:


df = housing_df[['CRIM','INDUS','LSTAT',"RM","MEDV"]]
sns.pairplot(df)


# # Data manipulation
# Visualization is helpful and can be really useful in Python in lots of situations, especially if you need something super specific that can't be done other tools - or if you just need a quick visual of what's happening.  The real power unleashed by coding is to manipulate the data in a series of steps that can be repeated over and over again.  This is where `pandas` and Python shine.
# 
# ## Where to get more help
# * The [pandas documentation](https://pandas.pydata.org/pandas-docs/stable/index.html) is very good
# * The [10 minute guide to pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html) is a great place to start
# * Pandas comparison to [spreadsheets](https://pandas.pydata.org/pandas-docs/stable/getting_started/comparison/comparison_with_spreadsheets.html?highlight=filtering)
# * There are alot of examples in the [pandas cookbook](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html), but if you can't find it there - try [stackoverflow](https://stackoverflow.com/)
# 
# First thing we need to know about dataframes is how they are accessed.  In other words, how do we get at specific rows/columns in the data.  Below are a few indexing techniques.

# ## Data Understanding 
# The following dataset represents individuals and their health insurances charges from a US company.  Some of the key indicators that influence the cost of the insurance are in this dataset.
# ### Insurance
# * __age__: age of primary beneficiary
# * __sex__: insurance contractor gender, female, male
# * __bmi__: Body mass index, providing an understanding of body, weights that are relatively high or low relative to height,
# objective index of body weight (kg / m ^ 2) using the ratio of height to weight, ideally 18.5 to 24.9
# * __children__: Number of children covered by health insurance / Number of dependents
# * __smoker__: Smoking
# * __region__: the beneficiary's residential area in the US, northeast, southeast, southwest, northwest.
# * __charges__: Individual medical costs billed by health insurance

# In[ ]:


# First get the data and take a quick look at the set
insurance_df = load_data('insurance')
insurance_df


# In[ ]:


# Gather the first row
insurance_df.iloc[0]


# In[ ]:


# The rows between 10-20
insurance_df.iloc[10:20]


# ## Pandas Series
# With dataframes, the columns of data are represented as a collection of [series](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html?highlight=series#pandas.Series).

# In[ ]:


insurance_df.columns


# We can look at the data in single series

# In[ ]:


# All the ages
insurance_df['age']


# In[ ]:


# but if we want more than one column (series) we need to specify a list
list_of_columns = ['age','sex']
insurance_df[list_of_columns]


# In[ ]:


# More commonly we just use the list directly
insurance_df[['age','sex']]


# We can use this for lots of great stuff like aggregating values in a column.

# In[ ]:


# What is the maximum charges
insurance_df['charges'].max()


# ### Filtering
# Filtering is a bit more complex.  What we need is a boolean array of values to `index` our dataframe by.  I'll leave the [explanation to the experts](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html), but show a few examples.

# In[ ]:


# All the smokers
insurance_df[insurance_df['smoker']=='yes']


# In[ ]:


# Or using the query syntax
insurance_df.query('smoker=="yes"')


# In[ ]:


# and now, just the male smokers
insurance_df.query('sex=="male" & smoker=="yes"')


# In[ ]:


# We can also group our queries and then apply aggregates
# In this example, we are grouping by 'sex' and then using only the 'bmi' series, getting the mean()
insurance_df.groupby('sex')['bmi'].mean()


# In[ ]:


# Or by two categories
# Here we group by two columns and still just looking at bmi
insurance_df.groupby(['sex','smoker'])['bmi'].mean()


# ## Working on data in a series
# The library is incredibly powerful, but just a few things we want to do.  Let's take a few examples.  
# 
# A few things to note
# - all operations apply to all the items in the series by default, so no need to loop
# - while we can change values in a series, more commonly we'll just create a new series and replace the old one (in one fellswoop)
# - notice that what we are really doing is creating a new series anyway (below, we are rounding the numbers, but this creates a new series - unconnected to our dataframe)

# In[ ]:


# Create a new column that just says whether someone has children
# If the number of children is > 0 then True else False
insurance_df['has_children'] = insurance_df['children'] > 0
insurance_df


# In[ ]:


# Now, let's round the amount of the charges to 2 decimals
insurance_df['charges'] = round(insurance_df['charges'],2)
insurance_df['charges']


# In[ ]:


# assuming these charges are an annual rate, let's create a column of the monthly rate
insurance_df['monthly_charges']=round(insurance_df['charges']/12,2)
insurance_df


# ### Working with strings in the series
# Working with strings in a series [are a little different](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.html), but they look alot like the python string functions.  We need to tell `pandas` what the type of data we want to work with is

# In[ ]:


# Working with a string, ensure all the male and female strings are UPPERCASED
insurance_df['gender']=insurance_df['sex'].str.upper()
insurance_df


# In[ ]:


# or we could uppercase just the first letter of the region for instance
insurance_df['region'] = insurance_df['region'].str.title()
insurance_df


#!/usr/bin/env python
# coding: utf-8

# ## Data Preparation Tasks
# After we have seen how our data looks, next we need to spend some time preparing our data for use.  This means we need to ensure that the data types are correct, that we have dealt with "dirty" data (missing fields, outliers, unary values), and possibly creating new factors which can enhance predictive models or better explain the data we have. 

# In[ ]:


# Import relevant libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
sys.path.append('..')
from src.data import load_data

# If you prefer a different style, pick from this list
# plt.style.available
pd.set_option('display.precision',4)
plt.style.use('fivethirtyeight')
plt.rcParams["figure.figsize"] = (20, 10)


# Before we jump in, we'll use the [cereal](DataDictionary.ipynb#cereal) dataset for some of this example.

# In[ ]:


dirty_cereal_df = load_data('Cereals_dirty')
dirty_cereal_df


# In[ ]:


# This will give us some information, but a more exhaustive rendention maybe in order
dirty_cereal_df.info()

# TODO: Explore the dirty cereal data, dataframe


# ### Missing data
# 
# Missing data can be fields that are represented as NULL, Na, NaN (not a number), blanks or it could even just plain wrong (like a number where you expect a string or a string where you expect a number).  All of these situations can be handled similarly.  Fortunately, the `pandas` library gives us some tools to deal with them.

# In[ ]:


dirty_cereal_df.head(10)


# Right away we can see in the first line that there is a missing value.  Let's see if we find any more

# In[ ]:


# This statement counts up the number of null/na values in every column
dirty_cereal_df.isnull().sum()


# In[ ]:


# And since we know a bit about visualization, 
dirty_cereal_df.isnull().sum().plot(kind='bar')


# In[ ]:


# So it seems we have some null or NaN fields, how should we proceed
# We could replace the values
# new_cereal_df = dirty_cereal_df.copy(deep=True)
# Find all the fields with an na or null and replace with 0
# Notice .loc allows us to access a set of rows/columns by label or boolean
dirty_cereal_df.loc[dirty_cereal_df.carbo.isna(), 'carbo'] = 0
# We could also replace with the mean/median
dirty_cereal_df.loc[dirty_cereal_df.carbo.isna(), 'carbo'] = dirty_cereal_df['carbo'].mean()
dirty_cereal_df.isnull().sum().plot(kind='bar')


# ## Fixing inappropriate values
# Let's check out our data and see if we can find any outliers or maybe inappropriate values.  We'll start by checking the datatype of each column

# In[ ]:


dirty_cereal_df.dtypes


# In[ ]:


# Let's get a box plot for a numerical column

fig = plt.figure(figsize=(10,7))
plt.boxplot(dirty_cereal_df['calories'], labels=['calories'])
#plt.boxplot(dirty_cereal_df[['calories','sugars']], labels='calories'])
plt.title('calories')
plt.show()


# Seaborn allows us to do a similar chart

# In[ ]:


# Also we can do this with seaborn
# Notice the [[]] indexing method, this says return the result as a dataframe rather than a series
g = sns.boxplot(data=dirty_cereal_df[['sugars','mfr']],x='mfr',y='sugars');
g.set_title('sugars by manufacturer')


# From the first box plot, we can see that that have an issue with calories (there is a negative value).  You might want to check the other columns or maybe just do a visual scan of the columns to see what else might be a problem.
# 
# Also we can see that we have Post and Kellogg as manufacturers.  I'm guessing this is a mistake since all the others only have a single letter representing the brand.  We may want to address this as well
# 
# The next step is to figure out what to do with this data.  Usually we don't want to eliminate it from the source data and it might be helpful in our actual dataset - so we can simply filter out the bad rows or we can replace them.

# In[ ]:


# TODO: Replace the calories that are negative with the positive value
dirty_cereal_df['calories'] = dirty_cereal_df['calories'].abs()


# In[ ]:


# Let's check to see if any of the other numeric fields are suspect
dirty_cereal_df.describe()


# In[ ]:


# let's take a look at the non-numeric columns
dirty_cereal_df.select_dtypes(exclude='number').columns


# In[ ]:


[dirty_cereal_df[c].value_counts() for c in dirty_cereal_df.select_dtypes(exclude='number').columns]


# In[ ]:


# And maybe most interesting is to look at these in a bar chart
fig, axs = plt.subplots(ncols=3)

sns.countplot(x='mfr', data=dirty_cereal_df, ax=axs[0])
sns.countplot(x='foodtype', data=dirty_cereal_df, ax=axs[1])
sns.countplot(x='type', data=dirty_cereal_df, ax=axs[2])


# In[ ]:


# Since we realize that `foodtype` is just the same value we can drop the column from our dataset
dirty_cereal_df = dirty_cereal_df.drop(columns=['foodtype'])
dirty_cereal_df


# #### Fixing inappropriate values - Your turn
# ---------
# There are several other issues in this dataset like 
# - Sugars and potass also have 0/null values
# - there is a calorie number < 0
# - the manufacturer codes include K, G, P etc, but also Post and Kellogg how to deal?
# - some rows have weight = 0 or na, should we drop them? or replace them with mean values?

# In[ ]:


# TODO: What about sugars and potass these have 0/null values
# TODO: Decide what to do about calorie number <= 0
# TODO: Deal with Post, Kellogg
dirty_cereal_df.loc[dirty_cereal_df['mfr']=='Post','mfr']='P'
dirty_cereal_df.loc[dirty_cereal_df['mfr']=='Kellogg','mfr']='K'
dirty_cereal_df['mfr']=dirty_cereal_df.mfr.str.upper()
# TODO: Deal with missing weight


# ## Data Preparation
# Occassionally we find it helpful to adjust our data to make it easier to work with or make it more suitable for different machine learning models.  While we will look at a few more methods as we deal with specific algorithms, here are some of the most common steps we may want to take as we continue our EDA

# ### Normalization & Standardization
# Often when we are dealing with data, the units are not on the same scale.  For instance in this case, `calories` is a range from 50 to 160 whereas `weight` ranges from 0.5 to 1.5.  Most of our mathematical algorithms used in machine learning would give `calories` an inappropriately large influence on the outcome.  So we need to adjust for both of these to be on a similar scale.  This is where standardization and normalization comes in.  We can use a min/max normalization which will make each category on a scale from 0-1
# 
# We do this with the following formula
# $$x_{scaled} = \frac{x-min(x)}{max(x)-min(x)}$$
# 
# _The terms normalization and standardization are sometimes used interchangeably, but they usually refer to different things. Normalization usually means to scale a variable to have a values between a desired range (like [-1,1] or [0,1]) while standardization transforms data to have a mean of zero and a standard deviation of 1. Advantage of Normalization over Standardization is that we are not bound to any specific distribution. In addition to that Normalization also suppresses the effect of outliers to some extent._
# 
# Normalization is a good technique to use when you do not know the distribution of your data or when you know the distribution is not Gaussian (a bell curve). Normalization is useful when your data has varying scales and the algorithm you are using does not make assumptions about the distribution of your data, such as k-nearest neighbors and artificial neural networks

# In[ ]:


dirty_cereal_df[['calories','weight']].describe()


# In[ ]:


def normalize(data, column):
    new_column_name = f'{column}_NORM'
    data[new_column_name]=(data[column]-data[column].min())/(data[column].max()-data[column].min())
    return data

# Apply a normalization to our dataset
normalize(dirty_cereal_df,'calories')
normalize(dirty_cereal_df,'weight')
fig, axs = plt.subplots(ncols=2)

axs[0].set_title('Original')
axs[1].set_title('Scaled')
sns.scatterplot(data=dirty_cereal_df, x='calories', y='weight', ax=axs[0])
sns.scatterplot(data=dirty_cereal_df, x='calories_NORM', y='weight_NORM', ax=axs[1])


# In statistics, standardization is the process of putting different variables on the same scale. This process allows you to compare scores between different types of variables. Typically, to standardize variables, you calculate the mean and standard deviation for a variable. Then, for each observed value of the variable, you subtract the mean and divide by the standard deviation.
# 
# This process produces standard scores that represent the number of standard deviations above or below the mean that a specific observation falls. For instance, a standardized value of 2 indicates that the observation falls 2 standard deviations above the mean. This interpretation is true regardless of the type of variable that you standardize.
# We use the following formula to Standardize a Variable value
# 
# $$z=\frac{(X-\mu)}{\sigma}$$
# 
# Standardization works best when the variable follows a Normal distribution due to the fact that in a Normal Distribution 68% of data lies within 1 standard deviation from the mean, 95% within 2 standard deviation and 99.7% within 3 standard devations from the mean. So it is highly unlikely that a variable value is greater than ±3
# 
# Standardization assumes that your data has a Gaussian (bell curve) distribution. This does not strictly have to be true, but the technique is more effective if your attribute distribution is Gaussian. Standardization is useful when your data has varying scales and the algorithm you are using does make assumptions about your data having a Gaussian distribution, such as linear regression, logistic regression, and linear discriminant analysis.

# In[ ]:


from scipy import stats
def standardize(data, column):
    new_column_name = f'{column}_STD'
    data[new_column_name] = stats.zscore(data[column])
    # data[new_column_name]=(data[column]-data[column].mean())/data[column].std()
    return data

# Apply a standardization to our dataset
standardize(dirty_cereal_df,'calories')
fig, axs = plt.subplots(ncols=2)

axs[0].set_title('Original')
axs[1].set_title('Normalized')
sns.histplot(data=dirty_cereal_df, x='calories', ax=axs[0])
sns.histplot(data=dirty_cereal_df, x='calories_STD', ax=axs[1])


# ### Discretizing / Binning
# Sometimes, it might be helpful to have categories for the ranges of values rather than just the value themselves.  For instance, if we are looking at the cereal example, it might be helpful to determine that cereal with a low calorie count vs a high calorie count

# In[ ]:


# How about we create a category for these fields instead
dirty_cereal_df['calorie_groups'] = pd.qcut(dirty_cereal_df.calories,q=3,duplicates='drop',labels=['low cal','normal','high cal'])
print(dirty_cereal_df.calorie_groups.value_counts())
sns.countplot(x='calorie_groups', data=dirty_cereal_df)


# ## Dealing with categorical variables
# Machine learning models deal in numeric data and don't handle string data or categorical data very well, so often times we are left to deal with categorical data and turning it into numerical.
# 
# In the cereal dataset we have `mfr`, `type`, and `calorie_groups` which are not numeric, but we also have `shelf` which is numeric, but really is a categorical field.  So we need to be careful about this as well.
# 
# We have a couple of options depending on which kind of data we are encoding.  If we are dealing with data and the order matters, for instance using a Likert scale (`disagree`,`somewhat agree`, `agree` etc), then we have ordinal dta and the data should be encoded with values 0 to n-1 (where n is the number of categories).  Otherwise, we should put our features in a OneHotEncoding whereby their is a feature created for each category and a 1 is placed in the proper column that matches the feature.

# In[ ]:


dirty_cereal_df.dtypes


# In[ ]:


# Start with ensuring pandas knows what we are dealing with
print(dirty_cereal_df.mfr.value_counts())
dirty_cereal_df['mfr'] = pd.Categorical(dirty_cereal_df['mfr'])
dirty_cereal_df.mfr.describe()


# In[ ]:



# We could use this to just get the dummy columns and join ourselves
#   dirty_cereal_df = pd.concat([dirty_cereal_df, pd.get_dummies(dirty_cereal_df['mfr'],prefix="mfr",prefix_sep="_")], axis=1)
#   dirty_cereal_df.drop(columns='mfr')

# Or we can let pandas handle this all for us
dirty_cereal_df = pd.get_dummies(dirty_cereal_df,prefix=['mfr','type'],columns=['mfr','type'])
dirty_cereal_df


# ### Advanced data preparation
# While preparing the data for machine learning, we often find that we either don't have enough features or we have way too many features to be valuable.  In both cases, we need to consider which features help us to describe the outcomes we are searching for.  We can often times do both tasks, creating new features [Feature Engineering](#feature-engineering) or reducing features through [Feature Selection](#feature-selection).  A brief overview is here, though we'll see more examples as we work through a few examples.
# 
# #### Feature Engineering
# Sometimes a set of predictors just doesn't provide enough variability on it's own and we would find value in breaking apart or finding new features in exisiting features.  One of the most obvious is time/date fields, these types of fields are filled with amazing data all locked up in what look like a single value.  Consider a date field for instance, with a date we can tell a whole lot of interesting things:
# - What day of the week is it?  (Mon, Tue, Wed..)
# - Which day of the month?  (1st, 10th, 21st ...)
# - Which month of the year? 
# - Which season? (Spring, Summer ...)
# - What's the closest holiday, payday, birthday, significant event?
# - Is it a leap year? 
# - Which week of the fiscal year?
# 
# By exploring the dates on these dimensions we may find a better set of predictors or develop new insights into the quality/variability of our data.  The same thing works with time (hour of the day, night/day, morning/afternoon/evening).  These are easy and very common ways to create new insights into the data from a seemingly small set of predictors.  Check your data to see if there are hidden aspects as well!There are many, many different transformations and to add features to a dataset which has just a few features.  For instance, it may be necessary to consider the interaction between variables.  Consider, 2 categorical variables like movie genres.  While it would be helpful to look at each genre separately, it's possible that considering a movie of multiple genres is of interest.  Sci-Fi/Action movies or Romance/Comedy movies for instance.  We can see this combination by looking at dummy variables of course, but it might also be helpful to have a column for common 2 genre combinations or 3 genre combos.
# 
# Other methods to consider: 
# = combining continuous variables with simple math (addition, subtraction, multiplication, division), 
# - polynomial fits : instead of $y=\beta_0x_0 + \epsilon$ a more appropriate fit might be $y=\beta_0x_0^2 +\beta_1x_0  + \epsilon$
# - Ensembling: first clustering records and then using this outcome as predictor in a different model.
# 
# Aside from using the pandas library to add new series, the patsy library has also been built to provide a consise language syntax for generating statisical matricies.  This is covered in the [AdvancedTechniques](./41-AdvancedTechniques.ipynb) notebook.

# 
# #### Feature Selection
# We can also face what we call the "curse of dimensionality" where our data has way too much data.  For instance, if we are to create an image classifier, each pixel carries with it at least 3 pieces of information (red, green and blue values) or even more!  We can be overwhelmed with the number of dummy variables or simply the shear amount of data that is provided.  In these cases, we need to decide which are the most relevant pieces of data and which we can safely ignore.  Take for instance, the image classifier, the first row of pixels may be a black border on all the pictures - this doesn't help us there is no variability if all the images have the same black border.  We should therefore leave them out of the equation.  Or in the case of our movie generes, what if there is only 1 movie that is a Sci-Fi/Romance/Horror film?  This doesn't help us to find others like it.  In these cases, we need to reduce our set of features.
# 
# A few algorithms handle this pretty well, Decision Trees in particular are good at ignoring variables have limited 'split' value and regression models [use a more brute force approach](https://towardsdatascience.com/feature-selection-techniques-in-regression-model-26878fe0e24e) (forward selection, backward elimination, stepwise selection).  For the ones that don't we can drop unary columns (those that don't change at all in all of our records), or use something like PCA ([principal components analysis](./41-AdvancedTechniques.ipynb#principal-components)) which is meant to capture as much of the variability as possible in just a few orthagonal vectors.
# 
# Finally, knowing your data is one of the most important aspects of getting the right set of features.  Analysts that spend hours letting the computer chug away on too many features (or too far) are far less efficient than those that take time to understand the data and capture the essense prior to trying to tune any models on an inefficient dataset.

# # Next Steps
# Now that we have an idea of how to deal with outliers, manage null values, filter rows and columns of our data and fix other issues our data may be ready to start the modelling process.  We'll look at a number of other different transforms as we work through the actual machine learning tasks ahead.  Operations such as determining interactiongs been variables and decomposing variables into new factors.  But first, in the next notebook [Classification](./30-Classification.ipynb), we'll start to see how to apply the techniques of prediction.
# <div align='center'/>
# 
# [Back to TOC](./00-Introduction.ipynb)&emsp;&emsp;[<- Back: 02-Exploratory Data Analysis](./10-ExploratoryDataAnalysis.ipynb)&emsp;&emsp;[Next: Classification ->](./30-Classification.ipynb)

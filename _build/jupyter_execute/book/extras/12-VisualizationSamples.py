#!/usr/bin/env python
# coding: utf-8

# # Visualization Examples
# This notebook demonstrates a few visualization techniques just to show what is possible.  It starts with an overview of a complex visualization which uses the oft used, diamonds dataset.  Here it shows how subplots can be used to show different kinds of charts all in one go.
# 
# Following this the `mtcars` dataset is used to demonstrate how to visualize up to seven different dimensions in a single unified visual.  Each step adding one more piece of information to the overall picture.

# In[ ]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from plotnine import *
from plotnine.data import mtcars
from plotnine.data import diamonds as d
from plotnine.data import msleep
from plotnine.themes import theme_538
from pandas.api.types import CategoricalDtype
theme_set(theme_538())


# # Diamonds
# We'll start with a side-step and show how to think about a dataset with diamands (cut, color, clarity and size).  We start here only to show a few techniques that might be useful later in the notebook

# In[ ]:


f, axarr= plt.subplots(2,2, sharex=False, sharey=False, figsize=(18, 16))
f.tight_layout()
clarity_cat = CategoricalDtype(categories=['I1','SI1','SI2','VS1','VS2','VVS1', 'VVS2','IF'], ordered=True)
d['clarity'] = d.clarity.astype(clarity_cat)
sns.scatterplot(x=d.carat,y=d.price, ax=axarr[0,0])
sns.scatterplot(x=d.table,y=d.price, ax=axarr[0,1])
sns.barplot(x=d.color,y=d.price, ax=axarr[1,0])
sns.barplot(x=d.clarity, y=d.price, ax=axarr[1,1])
plt.setp(axarr[1,0].xaxis.get_majorticklabels(), rotation=45)
plt.setp(axarr[1,1].xaxis.get_majorticklabels(), rotation=45);


# ## mtcars
# This next set of visuals shows how we can disect a dataset along 1 to 7 dimensions.  At each stage we'll understand the relationship among the observations on one more factor.
# 
# We begin by fixing up some of the factors and getting a sense of what the dataframe looks like.  (31 cars, 14 factors)

# In[ ]:


df = mtcars
df['cyl'] = df.cyl.astype('category')
df['am'] = df.am.astype('category')
df['gear'] = df.gear.astype('category')
df['trans'] = df.am.apply(lambda x: 'auto' if x else 'man')
df['engine'] = df.vs.apply(lambda x: 'V-shaped' if x else 'straight')
df


# ## Viewing 1 dimension (factor)
# It is often helpful to view a single dimension of data to understand it's distribution.  We can use multiple different kinds of visuals here (histogram, pie-chart and kernel density plot come to mind).  But I'm not a huge fan of pie charts as they often are difficult to read, so a histogram works well.  We could also use a kernel density plot, which removes the issue with choosing a bin size.

# In[ ]:


(ggplot(mtcars, aes(x='mpg', y='stat(count)')) + geom_histogram()
+ ggtitle('Distribution of cars by MPG') + theme_538())


# In[ ]:


(ggplot(df, aes('mpg'))
+ geom_density()
+ ggtitle('Distribution of cars by MPG')+ theme_538())


# Another reason we might like a kernel density plot over a histogram is that we can add multiple factors (still looking only a single dimension, because we're not looking at the relationship to each other).

# In[ ]:


(ggplot(df, aes('mpg', color='trans'))
+ geom_density()
+ ggtitle('Distribution of cars by MPG'))


# ### Viewing 2 factors and their relationship
# When we want to consider the data in two dimensions, one way to go about this is to consider two axises.  In this way we see the *relationship between* the two variables.

# In[ ]:


# View the inverse linear relationship between a car's weight and it's MPG
(ggplot(df, aes(x='wt', y='mpg'))
 +geom_point()
 + xlab("Car weight in 1000lbs")
 +geom_smooth(method='lm')
+ ggtitle('MPG by car weight'))


# ### Relationship between 3 factors
# Adding a third dimension (in this case `gear`) to our scatterplot allows us to see even more insights in our data.  
# 
# For instance, once we color the chart, we can see that cars in our dataset with 3 gears tend to weigh more and have a lower MPG.  While cars with 4 gears seem to be lighter and more efficient.

# In[ ]:


# Adding a third factor to the analysis
(ggplot(df, aes(x='wt', y='mpg', color='gear'))
 +geom_point()
 + xlab("Car weight in 1000lbs")
+ ggtitle('MPG by car weight'))


# ### Adding a fourth attribute
# Size allows us to add a fourth dimension to our data.  In this case, we've decided to look at the number of cylinders for the size.  While we could certainly have used size for any of the other dimensions that we considered previously, it seems to make sense that we would use size here as it's clear that a 4-cylinder engine is usually smaller than a 6 or 8-cylinder.  Using one of the aesthetics might make sense, but size seems to fit best here.

# In[ ]:


# Here we are going to see the number of cylinders and how these compart
(ggplot(df, aes(x='wt', y='mpg', color='gear', size='cyl'))
 +geom_jitter(alpha=0.5) 
 + labs(x="Car weight in 1000lbs", title='MPG by car weight'))


# So what can we tell now from the chart above.
# * We can still see that a car's weight is inversely proportional to the fuel efficency (MPG)
# * We can tell that cars with more cylinders typically weigh more (and therefore have lower MPG)
# * We can also see that lighter cars with 4 or 6 cylinders often times are 4-speed (4 gears)

# ### Onto a fifth factor
# So far, we have developed a single chart with 4 unique pieces of information all at a glance and we haven't really cluttered our visual a whole lot.  Let's see how much further we can go before the visual gets too busy.  (The key is to select the right aesthetic for the right dimension in order that it makes sense).
# 
# Our next dimension is the type of engine.  Our dataset has V shaped engines and straight.  This is best represented by changing the `shape` of our markers.
# 
# It is clear below now that those larger 6 and 8 cylinder engines not only have straight engines by they are also heavier and tend to be 3-speed gearing ratios.
# 

# In[ ]:


# show engine shape
(ggplot(df, aes(x='wt', y='mpg', color='gear', size='cyl', shape='engine'))
+ scale_shape_manual(["v","s"])
+ geom_jitter(alpha=0.5) 
+ labs(x="Car weight in 1000lbs", title='MPG by car weight'))


# ### Seeing a six dimension using facets
# We can see now up to 5 dimensions, and here is where the interesting steps come in.  Let's say we want to see all the previous information, but we'd like to focus on the particular type of transmission.  We could adjust the shapes to account for the 4 different types (V-shaped + manual, V-shaped + automatic, straight manual, straight automatic) or we could use color with this combined factor.  But instead we can simply split our visual into two visuals using facets.
# 
# Facets allow us to see charts positioned in relationship to each other so we are not overwhelming a chart with too much data, yet we can still see additional relationships.
# 
# Notice here that we see two charts, the one on the left is for manual transmission, the one on the right for automatic transmissions.

# In[ ]:



(ggplot(df, aes(x='wt', y='mpg', color='gear', size='cyl', shape='engine'))
 +geom_jitter(alpha=0.5) 
 + scale_shape_manual(["v","s"])
 +facet_grid('~trans')
  + labs(x="Car weight in 1000lbs", title='MPG by car weight'))


# # More facets
# Now we are getting a lot of information packed into a single visual, but we'll take it one step further, by faceting not just on transmission type, but also on number of carburaters.  This becomes a bit more that we might want to show, but it demonstrates how we can facet both on the X and Y axes.

# In[ ]:


(ggplot(df, aes(x='wt', y='mpg', color='gear', size='cyl', shape='engine'))
 +geom_jitter(alpha=0.5) 
 +geom_point()
 +facet_grid('carb~trans', labeller=label_both)
  + labs(x="Car weight in 1000lbs", title='MPG by car weight, transmission type and carburaters'))


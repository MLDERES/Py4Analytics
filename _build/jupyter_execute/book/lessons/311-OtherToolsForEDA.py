#!/usr/bin/env python
# coding: utf-8

# *** This Notebook is Under Construction ***
# There are no guarantees that this notebook works or has all the required dependencies in the repository.
# ![under construction](../img/under_construction.png)

# # Other tools for Data Analysis
# As you have seen no doubt, all of the techniques are valuable to get a good understanding of our data.  There is hardly a project explanation or walkthrough of using any of the modelling techniques which doesn't first start with some kind of summary stats, a histogram and correlation matrix.  So much so that there are dozens of Python libraries that have encapsulated the most common techniques and [automated them for you](https://towardsdatascience.com/4-libraries-that-can-perform-eda-in-one-line-of-python-code-b13938a06ae).  
# 
# Examples include: [pandas_profiling](https://pypi.org/project/pandas-profiling/), [dtale](https://pypi.org/project/dtale/), [bamboolib](https://pypi.org/project/bamboolib/), and [sweetviz](https://pypi.org/project/sweetviz/)
# 

# In[ ]:


# Import relevant libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns
from pathlib import Path
import sys
sys.path.append('..')
from src.data import load_data

# you can find available styles with plt.style.available
plt.style.use('fivethirtyeight')
plt.rcParams["figure.figsize"] = (20, 10)


# In[ ]:


toyota_df = load_data("ToyotaCorolla")


# In[ ]:


from pandas_profiling import profile_report
toyota_df.profile_report()


# In[ ]:


from dataprep.eda import create_report
create_report(toyota_df)


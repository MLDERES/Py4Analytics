#!/usr/bin/env python
# coding: utf-8

# # Neural Networks
# There are no guarantees that this notebook works or has all the required dependencies in the repository.
# ![under construction](../img/under_construction.png)

# In[ ]:


# import pandas as pd
import pandas as pd
from sklearn import preprocessing
from sklearn.metrics import pairwise
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
from sklearn.cluster import KMeans
import matplotlib.pylab as plt
import seaborn as sns
from pandas.plotting import parallel_coordinates
import sys
sys.path.append('..')
from src.data import load_data,standardize
import pprint

plt.style.use('fivethirtyeight')
pd.set_option('precision',4)


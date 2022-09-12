#!/usr/bin/env python
# coding: utf-8

# # Getting data from a database
# 

# In[51]:


import sqlite3
import pandas as pd
from pathlib import Path

conn = sqlite3.connect('../data/laptopsales.db')
pd.read_sql('select * from sales', conn,index_col='sale_id')


# In[27]:


import sqlite3
import pandas as pd

conn = sqlite3.connect('../data/laptopsales.db')
sales = pd.read_csv('../data/LaptopSales.csv')
sales['sale_date']=pd.to_datetime(sales.Date)
sales.drop(columns='Date',inplace=True)
june_sales = sales[sales.sale_date.dt.month==6]
june_sales.to_sql('sales',conn, if_exists='replace',index_label='sale_id')


# In[36]:





# In[37]:


conn = sqlite3.connect('../data/laptopsales.db')
pd.read_sql('select * from sales',conn, index_col='sale_id')


# In[ ]:


pd.to_sql('sales',conn,index)


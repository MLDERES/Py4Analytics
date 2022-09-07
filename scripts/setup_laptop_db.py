import sqlite3
import pandas as pd

conn = sqlite3.connect('book/data/laptopsales.db')
sales = pd.read_csv('book/data/LaptopSales.csv')
sales['sale_date']=pd.to_datetime(sales.Date)
sales.drop(columns='Date',inplace=True)

sales.to_sql('sales',conn, if_exists='replace',index_label='sale_id')
# Now create a separate db file just for June sales
conn = sqlite3.connect('book/data/june_laptopsales.db')
june_sales = sales[sales.sale_date.dt.month==6]
sales.to_sql('sales',conn, if_exists='replace',index_label='sale_id')


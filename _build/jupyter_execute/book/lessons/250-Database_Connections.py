#!/usr/bin/env python
# coding: utf-8

# # Working with relational database
# One common source of data, especially in institutions, is a relational database.  Microsoft SQL Server, Teradata, Oracle, Postgres, MySql are all examples of relational databases that are in common use for managing transactional data.  Storing and retrieving data from these servers is a regular task in the life of an analyst because any process that does anything interesting is likely to generate or ingest a lot of data.  In this notebook, we'll look at the main components of a database connection, how to establish a connection and put some data into a simple database and read some data out the database.
# 
# ````{note}
# SQL (pronounced S-Q-L or see-kwil) is the primary data manipulation language. This means SQL is the language we use to get/save data with a relational database.  You won't need an in-depth understanding of SQL to work through this notebook, but if you want to brush up on some of the basics, this is [a good resources](https://www.w3schools.com/sql/default.asp).
# ````

# ## Definitions
# Before we start, let's define a few terms generically so that when you see them it becomes more clear what is happening.
# 
# * **Database Server** - A database server is the hardware which runs database software.  We will often refer to the database server as both the hardware and the software together.
# * **Database** - A database is a collection of tables, functions, procedures, et al, which allow access to the actual data.  The distinction between the server and the database are an important distinction, as a single *database server* can be hosting many *databases*.
# * **Connection** - in order to be able to run queries on a particular database, the client software needs to establish a connection to the database server/database combination.
# * **Cursor** - A database [cursor](https://en.wikipedia.org/wiki/Cursor_(databases)) is a mechanism which allows us to traverse the records in the database.  We can have many different cursors using the same connection to the database.
# 
# ## How to run a query
# There are three basic steps in order to execute a query against a relational database.
# 1. Establish a connection to the database
# 2. Using the connection create a cursor upon which to execute one or more SQL commands
# 3. Execute the SQL command using the cursor
# 4. Assuming there is a result, process the results of the query
# 5. The cursor may be reused if there are more commands to run
# 6. When the operation is complete, close the connection
# 
# We are going to look at a few different approaches for making the connection to the database.  Which one you use will depend largely on the destination RDBMS server.  For instance some of the common protocols include ODBC, OLE-DB, and DBAPI.  We'll take a look at a couple of these here.

# ## SQLITE3
# Arguably one of the simplest relational databases to work with in is the [SQLite3](https://www.sqlite.org/index.html) database.  It is also one of the most used databases in the world.  It's built into every [mobile phone](https://www.sqlite.org/mostdeployed.html) and comes bundled in many applications people use on a regular basis.  It has many of the features of a more robust relational database, though the data is all stored in a single portable file format.
# 
# Before we make a connection and read from a SQLite database, we need to describe cursors.  A database [cursor](https://en.wikipedia.org/wiki/Cursor_(databases)) is a mechanism which allows us to traverse the records in the database.  You can think of it as a pointer to a record.  We'll use a cursor in the next example to get data from a predefined database.
# 
# ````{caution}
# If you get an error running the next cell, it's likely that their is a database file already in the `output` folder.  In order to resolve, either delete the file `sample.db` or rename it to something like `sample.db.bak`
# ````

# In[5]:


import sqlite3

# Make a connection to the database
cnn = sqlite3.connect('../output/sample.db')

# Next make a cursor that can be used to run a query on the new connection
cur = cnn.cursor()

# Now we can execute our SQL statement against the database
cur.execute('CREATE TABLE pet(name , breed, owner)',)

# Now we'll check to see if the data was made.
result = cur.execute('SELECT name FROM sqlite_master')
result.fetchone()


# We'll next insert a bit of data into our database to make it a little more interesting.  This is not a lesson on SQLite per se, for that I would point you to the [documentation](https://docs.python.org/3/library/sqlite3.html).  But it should be noted that SQLite requires that transactions which intend to change to the database must be committed.  If you are unfamiliar with transactions, then you can brush up [here](https://en.wikipedia.org/wiki/Database_transaction).

# In[ ]:


cur.execute(""" 
    INSERT INTO pet VALUES
        ('Sparky', 'goldfish', 'Jim'),
        ('Buster','terrier','Louise'),
        ('T-Rex','iguana','Caleb')
"""
)
# Make the changes to the database
cnn.commit()


# In[ ]:


# Now let's get the data back out
result = cur.execute('SELECT * FROM pet')
result.fetchall()

# When we are finally done, we want to be sure to close the connection.
cnn.close()


# ## Connecting to other RDBMS
# Again, this is just an introduction of how to get data to/from a database we are using SQLite as a portable and simple example. All the same principals apply even if you are connecting to a Microsoft SQL, Teradata, Oracle or other DBMS. But the connection mechanism for other databases can vary.  There are a few common libraries we can leverage such as [pyodbc](https://github.com/mkleehammer/pyodbc/wiki).  [ODBC](https://docs.microsoft.com/en-us/sql/odbc/reference/what-is-odbc?view=sql-server-ver16) is a specification for a database API.  Nearly every commercial RDBMS supports connections and transactions using ODBC, meaning that to change between one database and another, the code changes very little - typcially the only thing that needs to change in the connection string and the precise SQL you are trying to execute.  Though that doesn't mean it is easy, connection strings are database platform dependent and can vary widely.  Here's [one source](https://www.connectionstrings.com/) that might help.
# 
# For SQL server, the connection string looks like:
# ```sql
# "Driver=SQL Server Native Client 11.0;Server=myservername; Database=myDatabase; User Id=myUserName; Password=myPassword;"
# ```
# 
# ### Connecting to MS SQL Server
# Most of the major RDBMS providers also provide python specific libraries if you know that you wont have to switch between different databases.  For instance, Microsoft provides [pymssql](http://www.pymssql.org/).  Using one of these libraries tends to make things a bit simpler if you just want to be able to do simple queries with a SQL database.
# 
# ````{note} Environment Variables
# Environment variables are variables that are stored in the operating system, rather than in our program.  Environment variables provide a way to configure your application without having to edit your source code when the configuration changes. Common config items that are often passed to application through environment variables are third-party API keys, network ports, database servers, and any custom options that your application may need to work properly.  For more information on environment variables [see this fantastic resource](https://www.twilio.com/blog/environment-variables-python).
# 
# Additionally, the library I used here [`python-dotenv`](https://pypi.org/project/python-dotenv/) can get your environment from a `.env` file in root of your Python project.
# ````

# In[ ]:


from dotenv import load_dotenv
from os import getenv
import pymssql

# This library allows the environment variables to be loaded from a file
load_dotenv()

# To get this working quickly, you can just replace these variables with your own values
svr = getenv("PYMSSQL_SERVER")
uid = getenv("PYMSSQL_USER")
pwd = getenv("PYMSSQL_PASSWORD")
db = getenv("PYMSSQL_DATABASE")

# Connect to a MS SQL Server Database
cnn = pymssql.connect(server=f'{svr}',user=uid, password=pwd,database=db)

# Create the cursor required to run the command
cur = cnn.cursor()

# Run the SQL command
cur.execute('SELECT top 10 * FROM Actor')

for row in cur:
    print(row)


# ### Dynamic Queries
# As soon as developers understand the value of using Python to connect to SQL the very next step is to put the two things together to create dynamic queries.  For instance look at the following code snippet.

# In[11]:


import datetime as dt
from dateutil.relativedelta import *

last_month = (dt.date.today()+relativedelta(months=-1)).month
sql_query = f"SELECT * FROM sales WHERE month = {last_month}"

# Connect to the database and do something interesting
# ...


# This is super handy, cause now we can get just the data we need like last month's sales and export it to an Excel sheet.  Python of course is terrific at automating this kind of thing and when we combine with SQL, we get some really powerful automation.
# 
# Even better we could ask a user to give us a date and we can create a query from the response
# ```python
# ...
# month = input('Which month should I get sales from?')
# sql_query = "SELECT * FROM sales WHERE month = "+month
# ...
# ```
# Normally we would expect that users wouldn't do anything malicious - they would input a month number and we'd have a perfectly fine query.  But we could run across a user that is less than friendly, they could input something like
# 
# ```sql
# 1; DROP TABLE sales;
# ```
# The resulting string would be 
# ```
# SELECT * FROM sales WHERE month = 1; DROP TABLE sales;
# ```
# If this statement were executed by our program, we would inadvertantly end up losing our entire sales table!

# 
# ## Passing parameters
# Fortunately there is protection.  We can let the SQL parser handle any issues like this, ensuring that we only get valid values for our parameters and not malicious code like above.  We simply pass parameters to fill in the variable parts of our SQL statement.
# 
# In the next code snippet, we are going to use another database in the supplied data, `cereals.db`.  This database has nutrition data for a variety of cereals.  We'll start by getting the columns that are in the database then we'll move on to a query using parameters.

# In[ ]:


# Connect to a sample database
cnn = sqlite3.connect('../data/cereals.db')
cnn.row_factory = sqlite3.Row
cur = cnn.cursor()
cur.execute('select * from cereals')
row = cur.fetchone()
print(row.keys())
cnn.close()


# Now that we know the kind of data we have in the table, we can go ahead with build a query where the number of calories are limited.

# In[15]:


cnn = sqlite3.connect('../data/cereals.db')
cur = cnn.cursor()

# Set the max_calories to be considered a low-calorie option
print("Low calorie cereals")
print("-"*10)
max_calories = 75
cur.execute("SELECT name,calories FROM cereals WHERE calories <= ?",[max_calories])
for row in cur.fetchall():
    print(f'{row[0]}: {row[1]}')


# Now, using the same query we can ask for high-calorie cereals
print()
print("High calorie cereals")
print("-"*10)
max_calories = 150
cur.execute("SELECT name,calories FROM cereals WHERE calories >= ?",[max_calories])
for row in cur.fetchall():
    print(f'{row[0]}: {row[1]}')
cnn.close()


# ## Using pandas
# Using Python, we can depend on one of our favorite data management utility libraries, `pandas` to get and put data into a SQLite database.  This is great news, because we already know how to do alot of different tasks with our utility library pandas.

# In[ ]:


import pandas as pd

conn = sqlite3.connect('../data/laptopsales.db')
pd.read_sql('SELECT * FROM sales', conn,index_col='sale_id')


# Likewise we can do some work with our dataframe and put it into a database with the `pd.to_sql()` function.

# In[ ]:


# Create a pandas dataframe
phone_book_df = pd.DataFrame({
    'Name':['Alice','Bob','Charlie'],
    'Phone':['555-555-1234','123-456-7890','555-867-5309']
    })
phone_book_df


# In[ ]:


# Create a connection to the sqlite3 database
conn = sqlite3.connect('../output/phone_book.db')
# This says to create a table named `phone_numbers` in the phone_book database.
# If the db or table is already there, replace it
# Don't store the index value in the db
phone_book_df.to_sql('phone_numbers',conn,if_exists='replace',index=False)


# In[ ]:


pd.read_sql('SELECT * FROM phone_numbers',conn)


# Being able to connect to a SQL database and run queries from Python is super handy and really useful. Combining the simplicity of Python and the power of a relational database can make for some very compelling and useful automation of common tasks.

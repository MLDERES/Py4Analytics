#!/usr/bin/env python
# coding: utf-8

# # Getting data from a database
# One common source of data, especially in institutions, is a relational database.  Microsoft SQL Server, Teradata, Oracle, Postgres, MySql are all examples of relational databases that in common use for storing and retrieving complex data.  Storing and retrieving data from these servers is a regular task in the life of an analyst because any process that does something interesting is likely to generate or ingest alot of data.  In this notebook, we'll look at the main components of a database connection, establish a connection and put some data into a simple database and read some data out the database.
# 
# ````{note}
# SQL (pronounced S-Q-L or see-kwil) is the primary data manipulation language, meaning SQL is the language we use to get data from a relational database.  You wont need an in-depth understanding to work through this notebook, but if you want to brush up on some of the basics, this is [a good resources](https://www.w3schools.com/sql/default.asp).

# ## Connecting to the database
# There are three basic steps in order to execute a query against a relational database.
# 1. Establish a connection to the database
# 2. Create a command
# 3. Execute the command
# 4. Process the result (if there is a return)
# 
# We are going to look at a few different approaches for making the connection to the database.  Which one you use will depend largely on the destination RDBMS server.  For instance some of the common protocols include ODBC, OLE-DB, and DBAPI.  We'll take a look at a couple of these here.

# ## SQLITE3
# Arguably one of the simplest relational databases to work with in is the [SQLite3](https://www.sqlite.org/index.html) database.  It is one of the most used databases in the world.  It's built into every [mobile phone](https://www.sqlite.org/mostdeployed.html) and comes bundled in many applications people use on a regular basis.  It has many of the features of a more robust relational database, though it is all stored in a single portable file format.
# 
# Before we make a connection and read from a SQLite database, we need to describe cursors.  A database [cursor](https://en.wikipedia.org/wiki/Cursor_(databases)) is a mechanism which allows us to traverse the records in the database.  You can think of it as a pointer to a record.  We'll use a cursor in the next example to get data from a predefined database.

# In[1]:


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

# In[2]:


cur.execute(""" 
    INSERT INTO pet VALUES
        ('Sparky', 'goldfish', 'Jim'),
        ('Buster','terrier','Louise'),
        ('T-Rex','iguana','Caleb')
"""
)
# Make the changes to the database
cnn.commit()


# In[3]:


# Now let's get the data back out
result = cur.execute('SELECT * FROM pet')
result.fetchall()


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
# ````{note}Environment Variables
# Environment variables are variables that are stored in the operating system, rather than in our program.  Environment variables provide a way to configure your application without having to edit your source code when the configuration changes. Common config items that are often passed to application through environment variables are third-party API keys, network ports, database servers, and any custom options that your application may need to work properly.  For more information on environment variables [see this fantastic resource](https://www.twilio.com/blog/environment-variables-python).
# 
# Additionally, the library I used here [`python-dotenv`](https://pypi.org/project/python-dotenv/)can get your environment from a `.env` file in root of your Python project.
# ````

# In[4]:


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

cnn = pymssql.connect(server=f'{svr}',user=uid, password=pwd,database=db)
cur = cnn.cursor()
cur.execute('select top 10 * from Actor')

for row in cur:
    print(row)


# As soon as developers understand the value of using Python to connect to SQL the very next step is to put the two things together to create dynamic queries.  For instance look at the following code snippet
# 
# ```python
# ...
# month = input('Which month should I get sales from?')
# sql_query = "SELECT * FROM sales WHERE month = "+month
# ...
# ```
# Normally we would expect that users wouldn't do anything malicious - they would input a month number and we'd have a perfectly fine query.  But we could run across a user that is less than friendly, they could input something like
# 
# ```
# 1; DROP TABLE sales;
# ```
# The resulting string would be 
# ```
# SELECT * FROM sales WHERE month = 1; DROP TABLE sales;
# ```
# If this statement were executed by our program, we would inadvertantly end up losing our entire sales table!
# 
# ## Passing parameters
# Fortunately we have a fix!  We can let the SQL parser to handle any issues like this, ensuring that we only get valid values for our parameters and not malicious code like above.
# 
# In the next code snippet, we are going to use another database in the supplied data, `cereals.db`.  This database has nutrition data for a variety of cereals.  We'll start by getting the columns that are in the database then we'll move on to a query using parameters

# In[5]:


# Connect to a sample database
cnn = sqlite3.connect('../data/cereals.db')
cnn.row_factory = sqlite3.Row
cur = cnn.cursor()
cur.execute('select * from cereals')
row = cur.fetchone()
print(row.keys())
cnn.close()


# Now that we know the kind of data we have in the table, we can go ahead with build a query where the number of calories are limited.

# In[6]:


cnn = sqlite3.connect('../data/cereals.db')
cur = cnn.cursor()

# Set the max_calories to be considered a low-calorie option
max_calories = 75
cur.execute("select name,calories from cereals where calories <= ?",[max_calories])
print("Low cal cereals")
for row in cur.fetchall():
    print(row)

print()
print("High cal cereals")
# Now, using the same query we can ask for high-calorie cereals
max_calories = 150
cur.execute("select name,calories from cereals where calories >= ?",[max_calories])
for row in cur.fetchall():
    print(row)
cnn.close()


# ## Using pandas
# Using Python, we can depend on one of our favorite data management utility libraries, `pandas` to get and put data into a SQLite database.  This is great news, because we already know how to do alot of different tasks with our utility library pandas.

# In[7]:


import pandas as pd

conn = sqlite3.connect('../data/laptopsales.db')
pd.read_sql('SELECT * FROM sales', conn,index_col='sale_id')


# Likewise we can do some work with our dataframe and put it into a database with the `pd.to_sql()` function.

# In[8]:


# Create a pandas dataframe
phone_book_df = pd.DataFrame({'Name':['Alice','Bob','Charlie'],'Phone':['555-555-1234','123-456-7890','555-867-5309']})
phone_book_df


# In[9]:


# Create a connection to the sqlite3 database
conn = sqlite3.connect('../output/phone_book.db')
# This says to create a table named `phone_numbers` in the phone_book database.
# If the db or table is already there, replace it
# Don't store the index value in the db
phone_book_df.to_sql('phone_numbers',conn,if_exists='replace',index=False)


# In[10]:


pd.read_sql('SELECT * FROM phone_numbers',conn)


# In[11]:





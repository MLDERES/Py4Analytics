#!/usr/bin/env python
# coding: utf-8

# # Gather data from the web
# As a data analyst, data is the fuel that drives the engine of discovery.  Often times this means using data we have collected with web forms, using external systems or via some business process.  Occassionally, we'll be given the data directly or we can download some data from a webpage that meets our needs.  Being able to gather data from sources on the web is a skill that is often very useful.  Wouldn't it be great if you could download [weather data predictions](https://www.abstractapi.com/api/weather#:~:text=What%20does%20the%20Weather%20API%20do%3F%20Abstract%27s%20Weather,and%20forecasted%20weather%20data%20for%20millions%20of%20locations.) as part of your morning routine, or grab [movies reviews](https://www.rottentomatoes.com/) to make plans for the weekend or even get data from the [James Webb Telescope](https://www.nasa.gov/mission_pages/webb/about/index.html) so you can process your own images from outer space!
# 
# Well fortunately you have most of the skills you need to do some of these things already.  In this notebook, we'll look at a few ways to get at data on the web, this is not comprehensive, but it should give you a start in the right direction.  One key skill this notebook leaves out is automating a webpage (like filling out a form or hitting a submit button) this automation takes a bit of extra setup and doesn't work well in a Jupyter notebook, but there are tools that can be helpful.  Check out [selenium](https://www.geeksforgeeks.org/selenium-python-tutorial/) and [scrapy](https://docs.scrapy.org/en/latest/intro/tutorial.html) for a couple of approaches that use Python.
# 
# ## Simple Webscraping with Pandas
# Believe it or not, one of the simplest ways to get data from the web is to use `pandas`, the `read_html` function is fantastic and simple.  All we need is to install a couple libraries and then we can gather data from simpler web pages very quickly.
# 
# In this first example, I went to [boxofficemojo.com](https://www.boxofficemojo.com/) and I selected a particular page where I saw some data I needed.  In this case, [Top Lifetime Grosses by MPAA Rating for PG-13 movies](https://www.boxofficemojo.com/chart/mpaa_title_lifetime_gross/?by_mpaa=PG-13&ref_=bo_cso_ac).  Looking at this page, I can see that there are about 200 movies on the first page.  This is enough for our purposes.  Next, I captured the URL (the link in the browser) and I use this to open with the `pandas` library.  Be careful, the result of the `read_html` method is a *list* of dataframes, so we'll have to know which one we are after.  In this particular case there is only one data frame, so we can use that one.
# 

# In[ ]:


# Start by importing a couple of libraries
import pandas as pd
movies = pd.read_html("https://www.boxofficemojo.com/chart/mpaa_title_lifetime_gross/?by_mpaa=PG-13&ref_=bo_cso_ac")
print(len(movies))


# In[ ]:


# Since there is only one dataframe in the list, we choose the first one
movies_df = movies[0]
movies_df


# With one simple command, we have scraped 200 rows of data!  A little clicking [around on the website](https://www.boxofficemojo.com/chart/mpaa_title_lifetime_gross/?by_mpaa=PG-13&offset=200) and I can gather another page of movies as well.
# 
# Now, with a little detective work I can see that the only difference between the two URLs is that last item `offset=200`.  I wonder what happens if I change that value to `offset=400`?  Try it, I'll wait here....

# In[ ]:


# Since I already know there is only 1 dataframe in the list, let's just grab the first one immediately
movies_200_df = pd.read_html("https://www.boxofficemojo.com/chart/mpaa_title_lifetime_gross/?by_mpaa=PG-13&offset=200")[0]
movies_200_df


# You can see where this is going right?  I could easily setup a loop and simply change the value of `offset` from 200 to 400 to 600 to 800 and gather all the top 1000 movies.

# In[ ]:


# Build the basic url string
base_url = 'https://www.boxofficemojo.com/chart/mpaa_title_lifetime_gross/?by_mpaa=PG-13'

# Start over with our movies dataframe, in case this cell runs more than once
movies_df = pd.read_html(base_url)[0]
# We need a list to put all the dataframes in prior to joining it back together
movie_list = []
# Go through the loop by 200s from 200 to 1000 (step = 200)
for offset in range(200,1000,200):
    # Store 200 movies at a time into a temporary dataframe
    temp_url = base_url+f'&offset={offset}'
    print (temp_url)
    m_df = pd.read_html(temp_url)[0]
    movie_list.append(m_df)

# Now that we have all the movies in a list, append the datasets together into one master dataframe
movies_df = movies_df.append(movie_list,ignore_index=True)
movies_df


# Now that is super helpful!  We just downloaded 1000 top grossing pg-13 rated movies in a few seconds.  But what exactly was that thing we did at the end, the whole `offset=200` thing.  This is called a query parameter and be a very transparent way for webpages to communicate to the server about the data they want.
# 
# ## Query parameters
# A bit of background, (a very little bit), web page links usually only "resolve" to a particular page on a particular server.  The webserver looks up the page and returns whatever is stored there.  This isn't very handy if you have alot of data to display - for instance in the case of boxofficemojo.com, they don't want to have to create 5 different web pages for each set of 200 movies.  So instead they built one web page and used parameters (yes!  just like function parameters in Python) which define the exact contents to display.  Fortunately for us, this makes it very transparent how to manipulate the page.  We can see exactly what details the server needs to give the data we want.
# 
# The URL format is, `<protocol>` (like https://) followed by the endpoint (www.boxofficemojo.com/chart/mpaa_title_lifetime_gross) then a `?` followed by 0 or more query parameters.  Query parameters are name/value pairs and delimited by an `&`.  So let's look at that url from before again.
# 
# > https://www.boxofficemojo.com/chart/mpaa_title_lifetime_gross/?by_mpaa=PG-13&offset=200
# 
# Here the query parameters are `by_mpaa` and `offset`.  So that's interesting, now that we notice this, it's possible that we could change the `by_mpaa` parameter as well and get R rated movies as well?  Let's try it by hand first.  Paste the link into the website and change the PG-13 to R and see what happens.
# 
# That's great, so with a simple change we could also R rated movies in a dataframe as well.  (You can copy the code above and try it out for yourself below).

# In[ ]:


# Copy the code from above and replace PG-13 with R to get the top 100 grossing R rated movies


# It's kind of a pain to navigate all that string building and trying to keep up with encoding each part of the URL.  Spaces for instance, can't be used in a parameter and what if you need to use an `&` symbol for a parameter name.  Well fortunately, we have a helpful built-in library called `urllib` which takes care to make sure our format is right everytime.  All we need to do is supply a dictionary of parameters and tell the library to encode it into a proper request.

# In[ ]:


from urllib.parse import urlencode

# Build the basic url string
base_url = 'https://www.boxofficemojo.com/chart/mpaa_title_lifetime_gross/?'

# Setup the parameters
params = {'by_mpaa':'R','offset':0}
print(base_url + urlencode(params))


# # Using APIs 
# Another common way to get data from a website is with a known endpoint.  While the concepts for using these endpoints are similar, the implementation is usually left to the specific webpage based on the kind of information provided, so it's a bit difficult to generalize.  Here we'll look at an example that is very useful and gives a sense of the Python tools used to navigate the endpoint when you see something similar.
# 
# ## Using the requests library
# The [`requests`](https://requests.readthedocs.io/en/latest/) library is a very common library for automating the interaction with webpages.  There are lots and lots of features, we'll focus on just a few.  For more information, you can see the excellent documentation [here](https://requests.readthedocs.io/en/latest/).
# 
# There are several different request types that can sent to a webpage (GET, PUT, DELETE, HEAD, et al). GET is used to navigate a static website, sometimes using query parameters as we have seen already.  PUT and POST are used to submit data on a form.  We'll leave the others for a more advanced treatise.  For our purposes, we'll just take a look at GET.  
# 
# Let's take a new example.  What if we want get the current price of bitcoin?
# 

# In[ ]:


import requests

url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
r= requests.get(url)
r.text


# That was easy.  Notice we always get a response object, which may be a number of different formats, it could be HTML/text, JSON, or even some binary format (useful for images or encoded data).  We asked for the result as text, but in reality this looks like JSON.  We could apply the JSON methods we've learned earlier to turn this into a dictionary, but `requests` helps us out a bit with this by offering a method to get the response as a JSON like object.

# In[ ]:


url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
r= requests.get(url)
bitcoin_json = r.json()
print(type(bitcoin_json))
bitcoin_json


# So we already get the data as a dictionary!  This is helpful.  We could do something useful without much issue then.

# In[ ]:


# Give the user the current price of Bitcoin in USD, GBP, and EUR
price_index = bitcoin_json['bpi']
last_update = bitcoin_json['time']["updated"]
print(f'As of {last_update}')
for currency in ['USD', 'GBP', 'EUR']:
    units = price_index[currency]
    print(f'\tCurrent price of bitcoin in {currency}: {units["rate"]}')


# Parameters are dealt with in a similar way as with the `urlparse` library above, we put the parameters into a dictionary and pass them along.  Following is an example of finding out when the International Space Station will pass over a specific point.

# In[ ]:


iss_url = "http://api.open-notify.org/iss-pass.json"
query_params = {'lat':'45', 'lon':'180'}
resp = requests.get(iss_url,params=query_params)
resp.json()


# ## Using APIs
# ### Query Based Parameters
# ### REST services
# 
# ## Simple Webscraping with BeautifulSoup

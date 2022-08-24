#!/usr/bin/env python
# coding: utf-8

# # Differing data formats
# In this notebook, we'll look at a few different data formats that are common in analytics.  This includes, delimited formats (.csv), extensible markup language (.xml) and javascript notation (.json) formats.  There are several other types of data files that you may come across, but these are common for a couple reasons.
# * Portability.  This means that the files can be shared across different kinds of computer operating systems without too much trouble
# * Readibility.  There is no special encoding for these files.  They can be created or opened with a standard text editor.  
# * Compatibility.  Because they are easy to pass around and simple to understand they are supported by lots and lots of platforms.

# ## Delimited formats
# Probably the most common format for portable files is the delimited format (often comma-delimited).  In these files, each line represents a single record and the fields of each record are denoted by some kind of special separator character (usually a comma and sometimes a tab or space).  There are no rules for these kinds of files, just conventions.  For instance, the first line of the file is typically a "header" record.  This record serves to describe the contents in the rows that follow.  This makes is straightforward for someone reading the file to understanding what is expected in the data rows.  Take for instance
# > 
# > ```
# > Id,Name,Phone Number
# > 1,Alice,555-1234
# > 2,Bob,555-0898
# > 3,Charlie,555-9099
# > 4,Doug,867-5309
# > ```
# 
# In this example, we can see clearly that there are 4 records with the id values from 1 to 4.  The first record, that is with id 1, has a name of Alice and a Phone Number of 555-1234.  While we can easily see each of the other records- we can tell in this simple example that line 4 is missing a phone number.
# 
# While easy to read for simple/small files - it becomes increasingly complex to read this file in a text editor if we are to try and find errors and missing values.  Fortunately, we can use the tools we have to import the file rather easily and find missing values, misaligned fields and generally interpret the data.
# 
# ### Reading/Writting Delimited Files
# We can certainly read data files line by line and processing them this way, but most often, for our purposes we are looking to do something specific like evaluate the data, use it for analysis or convert it to another format.  If you are interested in the nuts and bolts of reading files line by line then I would refer you to [this documentation](https://docs.python.org/3/library/csv.html) or simply google 'reading csv file in Python'.  In order to use the data effectively, we'll depend instead on our ever useful and super-handy `pandas` library.
# 
# The `pandas` library actually can help us to read lots of different file formats from CSV files and Excel files, XML, JSON and even web pages (and suprisingly the clipboard!).  Mostly they work a lot alike, so we'll focus on the format and the nuances of the most common cases you'll run across.
# 
# ````{admonition} Optional Parameters
# The `read_csv()` function takes a number of optional parameters, so it's best to be explicit about what you mean rather than calling the function and counting on the order of the parameters.  Recall that in a function definition if the parameter is defined with an `=` after it, this means the parameter is optional and if not specified will use the default value as specified in the parameter definition.  For instance, 
# ```python
# def my_func(a, b=0, c='all'):
#     print(a)
#     print(b)
#     print(c)
# ```
# ````
# In this example, `a` is required, but `b` and `c` are optional.  This means you can specify values for these parameters and if you don't the defaults will be `0` and `"all"`.
# 
# You can try this in the next cell.  Try a few of your own combinations until you get the hang of it.

# In[ ]:


def my_func(a, b=0, c='all'):
    print(a, b, c)

print("Only specifying `a`")
my_func('Hello')
print("Providing `a` and `b` only")
my_func('Hello', 12)
print("Providing `a` and `b` explicitly")
my_func(a='Hello',b=12)
print("Providing `a` (by position) and `c` explicitly.")
my_func('Hello',c='everyone')
    


# Now back to the [`read_csv()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html?highlight=read_csv#pandas.read_csv) function.  The function definition can be intimidating because it has lots of options, but this is also helpful to ensure that the operation works exactly as we expect it to.  For instance, there are parameters which define what the delimiter is (especially if we choose not to use commas), an option to specify the field names, several parameters which help specify the date format (day first) and whether the file has an index defined in it.
# 
# In each case, we are interested in reading the file into a dataframe and then working on it with the tools we know about dataframes.  Let's look at a couple of simple examples.  All the data files can be found in the `data` directory so you can take a look in any text editor to read the file.
# {download}`ApplianceShipments.csv <../data/ApplianceShipments.csv>`

# In[ ]:


import pandas as pd

# Read a file from the data directory
shipments_df = pd.read_csv('../data/ApplianceShipments.csv')
shipments_df


# Sometimes the files have an identifier that we want to keep.  For instance the bankruptcy file has an account number which we want to use as our index.  We can tell pandas to keep this as the index rather than specifying a new one.  Here we are using the 
# {download}`Bankruptcy.csv <../data/Bankruptcy.csv>` file found in the data directory.

# In[ ]:


bankruptcy_df = pd.read_csv('../data/Bankruptcy.csv',index_col='NO')
bankruptcy_df.head()


# In[ ]:


# Also, we can limit the columns we can read so instead of all 26 columns - let's say I'm only interested in the D, YR, and R1-R3 (notice, since I want NO as the index, it needs to be in the column list)
bankruptcy_df = pd.read_csv('../data/Bankruptcy.csv',index_col='NO',usecols=['NO','D','YR','R1','R2','R3'])
bankruptcy_df.head()


# ### Outputing using pandas
# It is also helpful to gather data in one format a write to another.  There are many, many ways to go about this, but one simple way to handle this is to use the `to_*` functions.  We'll look a few others, but for now, let's say we have cleaned up our bankruptcy file and need to import into Excel.  We can easily write it to a csv file with a simple command.  Run the next cell and then check out the result.
# 
# {download}`my_new_file.csv <../data/my_new_file.csv>`

# In[ ]:


# Write the output to a CSV file
bankruptcy_df.to_csv('../output/my_new_file.csv')


# ## Structured text formats 
# XML (and JSON) provide similar portability as you can find with CSV files, but they tend to be more descriptive.  These formats allow for sub-records and descriptive field names.  They handle missing data a bit more effectively and obviously especially if they are being read by a human.  The second most common way to get data from the internet is through web-scraping or an API (application programming interface). Often, APIs will return a more structured format because of the level of detail they offer.  In this case, XML and JSON are used often.  In the case of web-scraping, that is getting data from a web page that doesn't offer a programmable end-point, parsing HTML becomes an important skill. Best of all, HTML is very similar to XML (it could be called a subset), so learning to deal with XML will go along way to learning how to deal with HTML.
# 
# ### Extensible Mark-up Language (XML)
# While the formatting of XML files and how they work is left to the lecture (it's better described in PowerPoint rather than code), we'll look at an example here.
# 

# In[ ]:


# We could just as easily read this from a file, but it helps to see the actual XML, so we'll read it directly from a string instead

xml_data = '''<?xml version='1.0' encoding='utf-8'?>
<data xmlns="http://example.com">
 <row>
   <shape>square</shape>
   <degrees>360</degrees>
   <sides>4.0</sides>
 </row>
 <row>
   <shape>circle</shape>
   <degrees>360</degrees>
   <sides/>
 </row>
 <row>
   <shape>triangle</shape>
   <degrees>180</degrees>
   <sides>3.0</sides>
 </row>
</data>'''
df = pd.read_xml(xml_data)
df


# ### Hierarchical data
# While this works fine with data that is just one level deep (for instance, we just have `rows` in the prior data.)  Things get a bit more complex and unwieldy to use `pandas` for complex data types.  Say for instance we want details about a cd collection
# 
# ```xml
# <music>
#   <artist name="Radiohead">
#     <album title="The King of Limbs">
#       <song title="Bloom" length="5:15"/>
#       <song title="Morning Mr Magpie" length="4:41"/>
#       <song title="Little by Little" length="4:27"/>
#       <song title="Feral" length="3:13"/>
#       <song title="Lotus Flower" length="5:01"/>
#       <song title="Codex" length="4:47"/>
#       <song title="Give Up the Ghost" length="4:50"/>
#       <song title="Separator" length="5:20"/>
#       <description link="http://en.wikipedia.org/wiki/The_King_of_Limbs">
# 	The King of Limbs is the eighth studio album by English rock band Radiohead, produced by Nigel Godrich. It was self-released on 18 February 2011 as a download in MP3 and WAV formats, followed by physical CD and 12" vinyl releases on 28 March, a wider digital release via AWAL, and a special "newspaper" edition on 9 May 2011. The physical editions were released through the band's Ticker Tape imprint on XL in the United Kingdom, TBD in the United States, and Hostess Entertainment in Japan.
#       </description>
#     </album>
#     <album title="OK Computer">
#       <song title="Airbag"  length="4:44"/>
#       <song title="Paranoid Android"  length="6:23"/>
#       <song title="Subterranean Homesick Alien"  length="4:27"/>
#       <song title="Exit Music (For a Film)"  length="4:24"/>
#       <song title="Let Down"  length="4:59"/>
#       <song title="Karma Police"  length="4:21"/>
#       <song title="Fitter Happier"  length="1:57"/>
#       <song title="Electioneering"  length="3:50"/>
#       <song title="Climbing Up the Walls"  length="4:45"/>
#       <song title="No Surprises"  length="3:48"/>
#       <song title="Lucky"  length="4:19"/>
#       <song title="The Tourist"  length="5:24"/>
#       <description link="http://en.wikipedia.org/wiki/OK_Computer">
# 	OK Computer is the third studio album by the English alternative rock band Radiohead, released on 16 June 1997 on Parlophone in the United Kingdom and 1 July 1997 by Capitol Records in the United States. It marks a deliberate attempt by the band to move away from the introspective guitar-oriented sound of their previous album The Bends. Its layered sound and wide range of influences set it apart from many of the Britpop and alternative rock bands popular at the time and laid the groundwork for Radiohead's later, more experimental work.
#       </description>
#     </album>
#   </artist>
#   <artist name="Portishead">
#     <album title="Dummy">
#       <song title="Mysterons"  length="5:02"/>
#       <song title="Sour Times"  length="4:11"/>
#       <song title="Strangers"  length="3:55"/>
#       <song title="It Could Be Sweet"  length="4:16"/>
#       <song title="Wandering Star"  length="4:51"/>
#       <song title="It's a Fire"  length="3:49"/>
#       <song title="Numb"  length="3:54"/>
#       <song title="Roads"  length="5:02"/>
#       <song title="Pedestal"  length="3:39"/>
#       <song title="Biscuit"  length="5:01"/>
#       <song title="Glory Box"  length="5:06"/>
#       <description link="http://en.wikipedia.org/wiki/Dummy_%28album%29">
# 	Dummy is the debut album of the Bristol-based group Portishead. Released in August 22, 1994 on Go! Discs, the album earned critical acclaim, winning the 1995 Mercury Music Prize. It is often credited with popularizing the trip-hop genre and is frequently cited in lists of the best albums of the 1990s. Although it achieved modest chart success overseas, it peaked at #2 on the UK Album Chart and saw two of its three singles reach #13. The album was certified gold in 1997 and has sold two million copies in Europe. As of September 2011, the album was certified double-platinum in the United Kingdom and has sold as of September 2011 825,000 copies.
#       </description>
#     </album>
#   </artist>
# </music>
# ```
# This doesn't look like the tabular data we are use to, each item in the list is an album, but each album can also include some songs.  In this case, we need to depend on other libraries to help us out.
# 
# We first need to read in the tree, then we can deal with each of the records individually.  Keep in mind we have attributes and tags here so there's a need to be a bit more specific.  And we'll need to use a bit of XPath to get there

# In[ ]:


import xml.etree.ElementTree as ET

xml_data = '''
<music>
  <artist name="Radiohead">
    <album title="The King of Limbs">
      <song title="Bloom" length="5:15"/>
      <song title="Morning Mr Magpie" length="4:41"/>
      <song title="Little by Little" length="4:27"/>
      <song title="Feral" length="3:13"/>
      <song title="Lotus Flower" length="5:01"/>
      <song title="Codex" length="4:47"/>
      <song title="Give Up the Ghost" length="4:50"/>
      <song title="Separator" length="5:20"/>
      <description link="http://en.wikipedia.org/wiki/The_King_of_Limbs">
	The King of Limbs is the eighth studio album by English rock band Radiohead, produced by Nigel Godrich. It was self-released on 18 February 2011 as a download in MP3 and WAV formats, followed by physical CD and 12" vinyl releases on 28 March, a wider digital release via AWAL, and a special "newspaper" edition on 9 May 2011. The physical editions were released through the band's Ticker Tape imprint on XL in the United Kingdom, TBD in the United States, and Hostess Entertainment in Japan.
      </description>
    </album>
    <album title="OK Computer">
      <song title="Airbag"  length="4:44"/>
      <song title="Paranoid Android"  length="6:23"/>
      <song title="Subterranean Homesick Alien"  length="4:27"/>
      <song title="Exit Music (For a Film)"  length="4:24"/>
      <song title="Let Down"  length="4:59"/>
      <song title="Karma Police"  length="4:21"/>
      <song title="Fitter Happier"  length="1:57"/>
      <song title="Electioneering"  length="3:50"/>
      <song title="Climbing Up the Walls"  length="4:45"/>
      <song title="No Surprises"  length="3:48"/>
      <song title="Lucky"  length="4:19"/>
      <song title="The Tourist"  length="5:24"/>
      <description link="http://en.wikipedia.org/wiki/OK_Computer">
	OK Computer is the third studio album by the English alternative rock band Radiohead, released on 16 June 1997 on Parlophone in the United Kingdom and 1 July 1997 by Capitol Records in the United States. It marks a deliberate attempt by the band to move away from the introspective guitar-oriented sound of their previous album The Bends. Its layered sound and wide range of influences set it apart from many of the Britpop and alternative rock bands popular at the time and laid the groundwork for Radiohead's later, more experimental work.
      </description>
    </album>
  </artist>
  <artist name="Portishead">
    <album title="Dummy">
      <song title="Mysterons"  length="5:02"/>
      <song title="Sour Times"  length="4:11"/>
      <song title="Strangers"  length="3:55"/>
      <song title="It Could Be Sweet"  length="4:16"/>
      <song title="Wandering Star"  length="4:51"/>
      <song title="It's a Fire"  length="3:49"/>
      <song title="Numb"  length="3:54"/>
      <song title="Roads"  length="5:02"/>
      <song title="Pedestal"  length="3:39"/>
      <song title="Biscuit"  length="5:01"/>
      <song title="Glory Box"  length="5:06"/>
      <description link="http://en.wikipedia.org/wiki/Dummy_%28album%29">
	Dummy is the debut album of the Bristol-based group Portishead. Released in August 22, 1994 on Go! Discs, the album earned critical acclaim, winning the 1995 Mercury Music Prize. It is often credited with popularizing the trip-hop genre and is frequently cited in lists of the best albums of the 1990s. Although it achieved modest chart success overseas, it peaked at #2 on the UK Album Chart and saw two of its three singles reach #13. The album was certified gold in 1997 and has sold two million copies in Europe. As of September 2011, the album was certified double-platinum in the United Kingdom and has sold as of September 2011 825,000 copies.
      </description>
    </album>
    <album title="Third">
      <song title="Silence"  length="4:58"/>
      <song title="Hunter"  length="3:57"/>
      <song title="Nylon Smile"  length="3:16"/>
      <song title="The Rip"  length="4:29"/>
      <song title="Plastic"  length="3:27"/>
      <song title="We Carry On"  length="6:27"/>
      <song title="Deep Water"  length="1:31"/>
      <song title="Machine Gun"  length="4:43"/>
      <song title="Small"  length="6:45"/>
      <song title="Magic Doors"  length="3:32"/>
      <song title="Threads"  length="5:45"/>
      <description link="http://en.wikipedia.org/wiki/Third_%28Portishead_album%29">
	Third is the third studio album by English musical group Portishead, released on 27 April 2008, on Island Records in the United Kingdom, two days after on Mercury Records in the United States, and on 30 April 2008 on Universal Music Japan in Japan. It is their first release in 10 years, and their first studio album in eleven years. Third entered the UK Album Chart at #2, and became the band's first-ever American Top 10 album on the Billboard 200, reaching #7 in its entry week.
      </description>
    </album>
  </artist>
</music>
'''

tree = ET.fromstring(xml_data)
print('All Artists')
for artist in tree.findall('artist'):
    print(artist.attrib)


# In[ ]:


# Interesting, but what about albums, can we find all the albums for each artist?
# Notice we can also read the data from a file rather than a string
tree = ET.parse('../data/music.xml')
print('All Artists/Albums')
for artist in tree.findall('artist'):
    # This time, just get the value of the 'name' attribute
    print('Artist:', artist.attrib['name'])
    # Notice we are searching starting with the current artist to find all their albums
    for album in artist.findall('album'):
        # Again, since we know the attribute we are after we'll just index it directly
        print(f'\t{album.attrib["title"]}')


# In[ ]:


# Now let's find all the songs on each album
tree = ET.parse('../data/music.xml')
print('All Artists/Albums')
for artist in tree.findall('artist'):
    # Notice, we can use the index or directly use `get`
    print('Artist:', artist.get('name'))
    # Notice we are searching starting with the current artist to find all their albums
    for album in artist.findall('album'):
        # Again, since we know the attribute we are after we'll just index it directly
        print(f'\tAlbum: {album.attrib["title"]}')
        for song in album.findall('song'):
            print(f'\t\t{song.get("title")}')


# ### Going further with XPath support
# This is the simplest situation, where we are just wanting to iterate through every element in the XML tree.  We can get much more creative with a specific query syntax for XML called [XPath](https://docs.python.org/3/library/xml.etree.elementtree.html#elementtree-xpath).  XPath allows for alot more complex situations, such as if we want to find only songs on albums by Radiohead or gathering the album description links only.  See these examples below.

# In[ ]:


# Only songs off of Radiohead albums
tree = ET.fromstring(xml_data)
print('Radiohead only')
for artist in tree.findall('./artist/[@name="Radiohead"]'):
    print('Artist:', artist.get('name'))
    # Notice we are searching starting with the current artist to find all their albums
    for song in artist.findall('.//album/song'):
        print(f'\t\t{song.get("title")}')


# In[ ]:


# Only album names and descriptions
tree = ET.fromstring(xml_data)
print('Only album name and description links')
for album in tree.findall('.//album'):
    print('Album:', album.get('title'))
    print('Link:',album.find('description').get('link'))


# ### Javascript Notation
# JSON is similar, a little less decoration (no `<>` and `</>`) but still very readable.  In the case of Python, JSON data is parsed into a dictionary with one key for every top-level element and the corresponding structure as it's value.  For instance, if we have an object like such, then we have one key in the dictionary and the value is a list.
# 
# ```json
#     "shapes":
#     [
#         {"shape": "square","degrees": 360,"sides": 4.0},
#         {"shape": "circle","degrees": 360},
#         {"shape": "triangle","degrees": 180,"sides": 3.0}
#     ]
# ```

# In[ ]:


import json
# Same data as above, described in JSON format
json_data = '''{"shapes":
    [
        {"shape": "square","degrees": 360,"sides": 4.0},
        {"shape": "circle","degrees": 360},
        {"shape": "triangle","degrees": 180,"sides": 3.0}
    ]
}
'''
# Notice the use of `loads` this is to load json from a string
data = json.loads(json_data)
print(data)
print(data['shapes'])


# In[ ]:


for row in data['shapes']:
    # Notice that the items in the list are themselves key/value pairs or as we know them dictionaries
    print(row)


# In[ ]:


# Since the values are dictionaries, we can access the values with string indexes
for row in data['shapes']:
    # Notice that the items in the list are themselves key/value pairs or as we know them dictionaries
    print(f"Shape: {row['shape']}")
    print(f"Degrees: {row['degrees']}")
    # But keep in mind, that we aren't guaranteed to have all the same name/value pairs
    # So using the 'get' method is a better option when dealing with unreliable data
    print(f"Sides: {row.get('sides',0)}")
    print()


# In[ ]:


# We can also load the data directly from a file
f = open('../data/shapes.json')
json_data_file = json.load(f)
print(json_data_file)


# Just remember that with JSON we are dealing with dictionaries and lists, so accessing the items is the same thing we know how to do with them.  The complexity comes in keeping track of when we have a dictionary and when we have a list - and then working with the items appropriately.
# ```json
# {
#   "data": [{
#     "type": "articles",
#     "id": "1",
#     "attributes": {
#       "title": "JSON:API paints my bikeshed!",
#       "body": "The shortest article. Ever.",
#       "created": "2015-05-22T14:56:29.000Z",
#       "updated": "2015-05-22T14:56:28.000Z"
#     },
#     "relationships": {
#       "author": {
#         "data": {"id": "42", "type": "people"}
#       }
#     }
#   }],
#   "included": [
#     {
#       "type": "people",
#       "id": "42",
#       "attributes": {
#         "name": "John",
#         "age": 80,
#         "gender": "male"
#       }
#     }
#   ]
# }
# ```
# In this example, we have a dictionary with two "keys" - `data` and `included`.  These keys have associated values which are lists (see the `[]`) even though their is only one item in each of these value lists.  So in order to processing the "sub-dictionaries" it becomes necessary first to get the first item in the list, then use the resulting dictionary to parse the next set of name/value pairs.

# In[ ]:


#
json_data = """{
  "data": [{
    "type": "articles",
    "id": "1",
    "attributes": {
      "title": "JSON:API paints my bikeshed!",
      "body": "The shortest article. Ever.",
      "created": "2015-05-22T14:56:29.000Z",
      "updated": "2015-05-22T14:56:28.000Z"
    },
    "relationships": {
      "author": {
        "data": {"id": "42", "type": "people"}
      }
    }
  }],
  "included": [
    {
      "type": "people",
      "id": "42",
      "attributes": {
        "name": "John",
        "age": 80,
        "gender": "male"
      }
    }
  ]
}
"""
api_data = json.loads(json_data)
# Notice only two keys in the json data
for k in api_data.keys():
    print(k)


# In[ ]:


# This is a list with one item, a dictionary
print(api_data['data'])


# In[ ]:


# So now we get the first item in the list, and it's a dictionary
data_dictionary = api_data['data'][0]
print(data_dictionary)


# In[ ]:


# With the `data_dictionary` in hand, we can access the items
for dd_key, dd_value in data_dictionary.items():
    print(f'{dd_key}: {dd_value}')


# In[ ]:


# We notice that again we have two more 'sub-dictionaries', attributes and relationships.  
attributes_dict = data_dictionary['attributes']
print(attributes_dict)
print()
for a_key, a_value in attributes_dict.items():
    print(f'{a_key}: {a_value}')


# In[1]:


# Relationships is even more complex with extra sub-dictionaries, so take it one step at a time
relationships_dict = data_dictionary['relationships']
print(relationships_dict)
print()
author_dict=relationships_dict['author']
print(author_dict)
print()
data_dict = author_dict['data']
print(data_dict)
print(data_dict["id"])


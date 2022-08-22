#!/usr/bin/env python
# coding: utf-8

# # Try it: Getting Started with Python
# 
# Now it's your turn to try out some of the techiques identified in the first few notebooks.  For each example, take a look first at the question.  Try to work out the logic in plain language first, then work out the coding logic afterward.  The outcome is described after each of the steps.
# In this notebook, we'll look at:
# - output (using the `print()` function)
# - input (using the `input()` function)
# - conditional statements
# - building resuable code (functions)
# - dealing with strings
# 

# ## Hello World
# 
# One of the first things all programmers learn to do is to write Hello World!  It's a time honored tradition, so let's start there.  In the next cell, set the value of the name variable and run the cell.

# In[ ]:


# Set the value of the my_name variable to your name
my_name = ...
print(f'Hello World!  My name is {my_name}')


# ### Hello, user
# Hello world is a great start, but what if we want this to work for everyone without changing our code.  Well we can use a built-in Python function called ```input()``` which will ask the user for some text.  The result of this function is a string.  Run the next cell to see how this works.

# In[ ]:


# Ask user for their name, store the value in the user_name variable
user_name = input('What is your name?')

# Print the value of the user_name variable
print(f'You said: {user_name}')


# Did you see the computer output the user's name?  Let's incorporate this into our Hello World, example from above.
# 
# Ask for the user's name.  Instead of Hello World, print a message that says hello to the user.  Make sure that you also introduce yourself.  Assuming the user's name is Mel, and my name is Ned - the output should look like
# 
# ```Hello Mel!  My name is Ned```

# In[ ]:


# Assign the variable to my_name
my_name = ...

# Ask for the user's name

# Print the greeting including the user's name and your name


# #### Dealing with time
# 
# Our greeting is plesant, but we can do better.  We should have a greeting that takes into account the time of day.  The first few lines determine the hour of the day (where 0 is midnight and 23 is 11pm).  Using an ```if/else``` construct, greet the user appropriately for the time of day (morning, afternoon, evening).
# 

# In[ ]:


# Getting the current time
from datetime import datetime as dt
import pytz
current_hour = dt.now(pytz.timezone("US/Central")).hour
print(f'The current hour is: {current_hour}')

# Assign the variable to my_name
my_name = ...

# Ask for the user's name
user_name = input('What is your name?')

# Set the greeting to default to nothing
greeting = ''
# If the the current hour is less than 12, change the greeting to 'Morning'
# Otherwise, if the current hour is between 12 and 17 (5pm) set the greeting to 'Afternoon'
# Otherwise, set the greeting to 'Evening'

print(f'Good {greeting}, {user_name}!  My name is {my_name}')


# ### Creating a function
# 
# That was fun, right?  But every time we want to use this code, we have to type it over and over again.  Or if we want to share it with someone else we have to tell them to change ```my_name``` to their own name.  Let's take this one step further and create a reusable function.
# 
# As you will remember, a function is a set of instructions that are combined together and can be referred to with a single name.  We assign variables to the function when we "call" the function.  So for instance, if we have a function called ```sum``` it takes two variables.  The value of these variables are defined outside the function, and when we call the function the values of ```x``` and ```y``` are replaced with the values we provide.  This allows us to something complex with these values and they can change each time.

# In[ ]:


# Create a function called 'add' which takes two variables x and y
def sum(x,y):
    print(f'The value of x is {x}')
    print(f'The value of y is {y}')
    # Assign the variable result to be the sum of x and y
    result = x+y
    return result

print(f'When we call the sum function the result is {sum(5,4)}')

first_number = 10
second_number = 12

# Using two variables to call the sum function and assigning the result to a third variable
sum_of_first_second = sum(first_number,second_number)

print(f"Let's use two variables to call the sum function: {sum_of_first_second}")
    


# You can see from the example above that ```x``` and ```y``` are placeholders that are defined when the function is called.  When we called the ```sum``` functions ```x``` and ```y``` changed each time, the first time because we specified the numbers 4 and 5 the second time we used variables to set the values to be used for  ```x``` and ```y```.
# 
# How can we use this to improve our greeting?  Let's create a function called ```greeting``` which takes as it's inputs the name of the author and the name of the person we are greeting.  This way, we can decide how we want to get these values (create them as variables, ask for input, read from a file, etc).
# 
# In the next cell, we have defined the function for you.  You just need to put your code in the body of the function.  Remember, the body of the function is everything that is indented at least one level.  Also, it is handy to know that words between ```'''``` (three single quotes) are comments that span multiple lines.  So these two blocks are both valid comments (that is they are ignored by Python).  By convention (it's not required, just good practice), when we define a function we put a multi-line comment which starts with the purpose of the function and also defines the parameters and any result the function returns.  This helps others wanting to use the function to know what to expect and how to use it.
# 
# ```python
# # Function purpose
# #
# # Parameters:
# #
# 
# ''' Function Purpose
#     
#     Parameters:
# '''
# ```

# In[ ]:


# Defining the greeting function
def greeting(author_name, user_name):
    ''' Greet a user 

        Parameters: 
            author_name (str) - the name of the program's author
            user_name (str) - the name of the user to greet

        Returns:
            A greeting (str)
    '''
    # author_name is supplied in the function call, and so is the user name
    
    # Get the current time
    current_hour = dt.now(pytz.timezone("US/Central")).hour

    # Set the greeting to default to nothing
    greeting = ''
    # If the the current hour is less than 12, change the greeting to 'Morning'
    # Otherwise, if the current hour is between 12 and 17 (5pm) set the greeting to 'Afternoon'
    # Otherwise, set the greeting to 'Evening'

    result = f'Good {greeting}, {user_name}!  My name is {my_name}'
    return result

# Assign the variable to my_name
my_name = ...

# Ask for the user's name
user_name = input('What is your name?')

# Call the function assigning the proper variables to the associated parameters
computer_greeting = greeting(...,...)

# Print the result


# Now that we have defined the function, we can use it again here.  Let's not ask the user for their name this time, let's just define it for them

# In[ ]:


# Call the `greeting` function, but instead of asking for a user_name just assign the variable here.
my_name = ...
user_name = 'Mercedes'

# Call the function again
computer_greeting = greeting(...,...)

# Print the result
print(f'{computer_greeting}')


# ## Count the number of occurrences of a word
# 
# Now well try something a little tricker.  This one requires the use of a couple of built in functions. And also the understanding classes and objects.
# 
# A class is a template or definition of a datatype.  We have already dealt with a couple of datatypes - strings, integers and lists.  string, int and list are all classes.  Classes have properties and functions as member items that we can get to using the ```.``` syntax.  In other words, if I want to change the case of a string, I can call any string's ```lower()``` member function.  Like.  Feel free to copy this code into a new cell and try it!
# 
# ```python
# my_variable = 'Some String' # my_variable is a variable of the type/class string
# my_variable.lower() # this says return me the same string but in lowercase.
# ```
# 
# Strings have [a whole bunch of built-in functions](https://docs.python.org/3/library/string.html) we can call.  A few helpful ones include:
# 
# ```str.capitalize()``` - Return a copy of the string with its first character capitalized and the rest lowercased.
# ```str.lower()``` - Return a copy of the string with all the cased characters converted to lowercase.
# ```str.lstrip()``` - Return a copy of the string with leading characters removed. The chars argument is a string specifying the set of characters to be removed. If omitted or None, the chars argument defaults to removing whitespace.
# ```str.rstrip()``` - Same as lstrip, but starting from the right
# 
# With this sytax in mind, let's see if we can write a function that will count up the number of times a word shows up in a given string.
# 
# So we start with our plain english recipe
# 
# Split the supplied string into separate words
# For every word in the supplied string
#     If we have seen this word before, add 1 to the count for that word
#     Otherwise, keep track that we have seen this word before and set the count to 1
# 
# A dictionary list will come in really handy here.  Remember that a dictionary is just a list that has strings as the index and the value is whatever we want it to be.  So, let's create a dictionary that will have every word we encounter, and we'll set the value of each item in the list to the number of occurances of that word.  Run the next cell as an example.
# 
# 

# In[ ]:


# Here's an example of what a dictionary would look like from this sample sentence
#  See Jane run.  Is that Jane

word_dictionary = { 'See': 1,  # See shows up 1 time in the word, so we set the value of the 'See' item to 1
                    'Jane': 2, # Jane is in the sentence 2 times, so we set the value of 'Jane' to 2
                    'run': 1,
                    'Is': 1,
                    'that': 1,
                 }

# Now let's see how to get the number of times a few items are found in the sentence
print(word_dictionary['Jane'])

# And here we can see all the items in the dictionary at once
print(word_dictionary)


# Now that we know what the outcome should look like for a sample sentence, let's see if we can build a counter for any number of sentences
# 
# Let's build the steps first using a known sentence where we can test the outcomes, then we'll put it into a function and try it with a slightly more complex string.

# In[ ]:


# This is the sentence we'll use to test our close
sample_string = 'See Jane run.  Is that Jane'



# Let's start by making all the characters in the sentence lowercase,
#  This will help when we are comparing strings, because `See` isn't the same as `see`
#  and for our purposes we don't want to make a distiction

sample_string = ... #  Replace ... with a function that will convert the characters to lowercase

print(sample_string)


# In[ ]:


# That was pretty straightforward, next we need to break the sentences up into the different words

words = ... # replace the ... a function that will "split" the sentences into words

print(words)


# Did you get output that looks like ```['see', 'jane', 'run.', 'is', 'that', 'jane']```?
# 
# Next we need to process each word
# Remove any punctuation from the end of the word
# If the word already in the dictionary
#   Increment the count by 1
# Else
#   Set the count to 1 (this is the first time we've seen the word)
# 
# The code below needs you to write the code for 
# - removing punctuation 
# - what to do in the case where the word isn't already in our dictionary
# 
# ```{hint}
# Remember the ```rstrip``` string function?  This function can take a list of characters to remove (by default it only strips off spaces)
# maybe it would be helpful to use this function to take off periods, commas and question marks?
# ```

# In[ ]:



# Initialize the empty dictionary
word_dictionary = {}

# For every word, 
for w in words:
    # Remove any punctuation from the end of the word
    ## YOUR CODE HERE ##
    
    # If the word already in the dictionary
    if w in word_dictionary.keys():
        # Increment the count by 1
        word_dictionary[w] = word_dictionary[w] + 1
    # Otherwise, set the count to 1
    ## YOUR CODE HERE ##

print (word_dictionary)


# You should see output like 
# ```python
# {'see': 1, 'jane': 2, 'run': 1, 'is': 1, 'that': 1}
# ```
# 
# If you don't see this, try this
# - Insert a print statement in your for loop to see if you can figure out where things are going wrong
# - Did you make sure to remove punctuation from the end of the words?
# - Did you write the "else" case for when the word doesn't already exist?
# 
# If you got it work, that is fantastic!  Next, we'll bring all the pieces together and create a function where we can test our logic

# In[ ]:


# Now bring it all together in a function

def word_counter(sentence, target_word):
    '''
    Count the nuber of times a particular word occurs in a given sentence, phrase or excerpt

    Parameters:
    ----------
        sentence (str) - the string to parse

        target_word (str) - the word to count in the supplied sentence

    Returns
    -------
        int 
            number of times the word is found in the sentence (-1, if not found)
    '''
    # Initialize the empty word dictionary
    word_dictionary = {}
    # Initialize the return value to -1
    count_of_target = -1

    # Split the supplied phrase `sentence` into a collection of words
    # For every word, 
    #   Remove any punctuation from the end of the word
    #   If the word already in the dictionary
    #       Increment the count by 1
    #   Otherwise, set the count to 1

    # Find the count associated with the `target_word` and assign it to count_of_target
    # Return the resulting count
    return count_of_target

print(f'As a test, this result should be 2.  Your function returned: {word_counter(sample_string,"jane")}')


# In[ ]:


# Run this cell to make sure your function works as expected
sample_string_2 = "A wonderful serenity has taken possession of my entire soul, like these sweet mornings of spring which I enjoy with my whole heart. I am alone, and feel the charm of existence in this spot, which was created for the bliss of souls like mine. I am so happy, my dear friend, so absorbed in the exquisite sense of mere tranquil existence, that I neglect my talents. I should be incapable of drawing a single stroke at the present moment; and yet I feel that I never was a greater artist than now. When, while the lovely"
sample_string_3 = "A wonderful serenity has taken possession of my entire soul, like these sweet mornings of spring which I enjoy with my whole heart. I am alone, and feel the charm of existence in this spot, which was created for the bliss of souls like mine. I am so happy, my dear friend, so absorbed in the exquisite sense of mere tranquil existence, that I neglect my talents. I should be incapable of drawing a single stroke at the present moment; and yet I feel that I never was a greater artist than now. When, while the lovely valley teems with vapour around me, and the meridian sun strikes the upper surface of the impenetrable foliage of my trees, and but a few stray gleams steal into the inner sanctuary, I throw myself down among the tall grass by the trickling stream; and, as I lie close to the earth, a thousand unknown plants are noticed by me: when I hear the buzz of the little world among the stalks, and grow familiar with the countless indescribable forms of the insects and flies, then I feel the presence of the Almighty, who formed us in his own image"
sample_string_4 = "A wonderful serenity has taken possession of my entire soul, like these sweet mornings of spring which I enjoy with my whole heart. I am alone, and feel the charm of existence in this spot, which was created for the bliss of souls like mine. I am so happy, my dear friend, so absorbed in the exquisite sense of mere tranquil existence, that I neglect my talents. I should be incapable of drawing a single stroke at the present moment; and yet I feel that I never was a greater artist than now. When, while the lovely valley teems with vapour around me, and the meridian sun strikes the upper surface of the impenetrable foliage of my trees, and but a few stray gleams steal into the inner sanctuary, I throw myself down among the tall grass by the trickling stream; and, as I lie close to the earth, a thousand unknown plants are noticed by me: when I hear the buzz of the little world among the stalks, and grow familiar with the countless indescribable forms of the insects and flies, then I feel the presence of the Almighty, who formed us in his own image, and the breath of that universal love which bears and sustains us, as it floats around us in an eternity of bliss; and then, my friend, when darkness overspreads my eyes, and heaven and earth seem to dwell in my soul and absorb its power, like the form of a beloved mistress, then I often think with longing, Oh, would I could describe these conceptions, could impress upon paper all that is living so full and warm within me, that it might be the mirror of my soul, as my soul is the mirror of the infinite God! O my friend -- but it is too much for my strength -- I sink under the weight of the splendour of these visions! A wonderful serenity has taken possession of my entire soul, like these sweet mornings of spring which I enjoy with my whole heart. I am alone, and feel the charm of existence in this spot, which was created for the bliss of souls like mine. I am so happy, my dear friend, so absorbed in the exquisite sense of mere tranquil existence, that I neglect my talents. I should be incapable of drawing a single stroke at the present moment; and yet I feel that I never was a greater artist than now. When, while the lovely valley teems with vapour around me, and the meridian sun strikes the upper surface of the impenetrable foliage of my trees, and but a few stray gleams steal into the inner sanctuary, I throw myself down among the tall grass by the trickling stream; and, as I lie close to the earth, a thousand unknown plants are noticed by me: when I hear the buzz of the little world among the stalks, and grow familiar with the"

print(f'Sample 2.  Expected: 4.  Your result: {word_counter(sample_string_2,"my")}')
print(f'Sample 3.  Expected: 19.  Your result: {word_counter(sample_string_3,"the")}')
print(f'Sample 3.  Expected: 42.  Your result: {word_counter(sample_string_4,"the")}')
print(f'Sample 3 (searching for feel).  Expected: 5.  Your result: {word_counter(sample_string_4,"feel")}')


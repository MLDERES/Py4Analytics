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


# ## Now we'll take it one step further
# For this exercise, continue to write the classic Hello World! with a twist.  Your output should be a string that contains an introduction to yourself, by stating your name and your age (not your real age if you don't wish).  You can use string concatenation or `f'strings`, it's up to you.  Two caveats, we want to make this easy for someone else to try and your age never stays they same, therefore the name must be stored in a variable `my_name` and the age should be calculated based on the current year something like 
# ```python 
# age = 2020 - 1985
# ```
# 
# The output should look like<br>
# ```
# Hello World!  My name is Michael and I am currently 40 years old
# ```
# 
# **BONUS**: _Can you calcuate your age in months instead of years?  How about days? (built in date functions is cheating)_

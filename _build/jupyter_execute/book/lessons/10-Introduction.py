#!/usr/bin/env python
# coding: utf-8

# # Welcome to Jupyter Notebooks
# 
# Notebooks are a handy way to combine code with text/explanations.  What's more, we can use notebooks to break up a program or analysis into several parts, running just one piece of code at a time.  For our purposes what this will do is allow us to look at a topic, execute some sample code to see how it works and then try writing something similar all in the same environment.
# 
# So for a quick background.  Notebooks are broken up into 'cells'.  Each cell can be interpretted by the browser in many different ways, but for our purposes each cell is either a documentation (Markdown) cell or a code (Python) cell.  Each cell is 'run' or 'executed' by either pressing a key combination or selecting one of the buttons at the top of the page.  For instance to run a cell, select the cell by clicking you mouse on in the box, then press CTRL+Enter.  
# <br>
# Try that with the cell below.

# In[ ]:


print('Welcome to Jupyter.  You have successfully run a code cell.')


# If you have done this correctly, you will see the results of running the cell immediately below the cell like such.
# ![image.png](../img/jupyter_welcome.png)

# The number on the left side of the cell just tells us the order in which the cell was run, so yours maybe different than the picture.
# 
# You can also run the cell by using the 'Cell' menu item at the top of screen.  This is useful if you want to run a series of cells, such as the entire notebook at once or all the cells up to a certain point.  For instance, say you are working your way through this notebook at get pulled away and decide to come back later.  You can scroll the browser down to the cell where you left off and simply select Cell-> Run All Above and this will ensure that all the prior cells are run before picking up where you left off.
# 
# ![image.png](../img/jupyter_run.png)

# ## In case something goes wrong
# Occassionally, this page will lose connection to the server or show an error message. You can simply refresh your webpage and most times the page will ask you if you want to restart the server.  Press yes.
# 
# In case things don't seem to be moving/running in your code, you can interrupt and restart your kernel.

# Now, run the next cell.  This cell just makes sure that you see all the results of running the cells that follow in the notebook.

# In[ ]:


from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"


# ## Before we begin
# There are two primary challenges for people to learn to code:
# 1. Thinking like a computer (we call this the algorithms)
# 2. Understanding the words and symbols to use to tell the computer how to run the steps of the algorithm (syntax)
# 
# ### Algorithms
# Algorithms are simply a set of steps required to complete a task.  We use algorithms all the time - for instance, the steps used to make a peanut butter and jelly sandwich or something very complex such as framing a house.  Algorithms have a few different kinds of steps - for instance, we have steps for PREPARING, TASK EXECUTION, DECISION MAKING and REPEATING instructions.  Each of the steps can be general steps - like grabbing peanut butter from the cabinet or taking an action on a particular item such as OPEN the peanut butter jar.  Learning to think in this way is one of the first challenges for people learning to code.
# 
# ### Syntax
# In order to make a computer complete the tasks that we desire, we need to talk in a language that can be understood by the computer.  This is called language syntax.  There are many different languages/syntaxes that humans can use to tell the computer what to do.  Python is the language we'll use because it reads alot like english and can become more intuitive with a few less symbols than other languages.
# 
# Often times, new learners, once they have successfully identified the algorithm that completes the task at hand, converting this algorithm to words, phrases and symbols that the computer understands is the second challenge.  These notebooks are focused on Python syntax, but students should constantly be on the lookout for the algorithms as well.  The algorithms used here are small/simple tasks - but they are often building blocks for more complex algorithms.

# 

# # Let's talk Python
# 
# Okay, there are [many](https://medium.com/velotio-perspectives/the-ultimate-beginners-guide-to-jupyter-notebooks-6b00846ed2af), [many](https://www.kdnuggets.com/2018/05/jupyter-notebook-beginners-tutorial.html) valuable resources to learn the ins and outs of Jupyter notebooks, so I'll leave you to explore the many ways they can be used.  _If you are already a Python whiz_ try some of the [Coding Challenges](../exercises/Coding_Challenges.ipynb) or explore [Jupyter Notebook Tips,Tricks](https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/). 
# 
# Now, one more thing before we get too far. You will see in many places, where there is non-computer code that gives other humans an idea of what is going on in the code. We call these pieces of text comments. Comments in Python start with a `#` symbol and tell the computer that everything following this symbol _on the current line_ is to be ignored. Comments are a valuable part of coding as they can help you to capture what you are trying to do (algorithm) before writing any code (syntax) and can be used once the code is in place to remember or clarify what exactly a bit of code is supposed to do. Here are a few examples of comments.
# 
# ```python
# # this is the first comment
# spam = 1  # and this is the second comment
#           # ... and now a third!
# text = "# This is not a comment because it's inside quotes."
# ```
# You will see comments sprinkled in among the examples, these don't need to be typed to make your code work, but it's a good idea to get in the habit early on so that you have good practice

# ## Strings, numbers, and lists
# 
# All programming languages can deal with many different kinds of datatypes.  The most common ones are boolean (`True` or `False`), numbers, strings, and collections of items.  Numbers are represented just by typing them out with no special characters.  Strings are characters that are surrounded by either `'` or `"` as we will see a bit later.  Boolean values can only either be `True` or `False` and are incredibly valuable as we'll see in a bit.

# In[ ]:


# Output a number
5
# Output a string
"This is a string"
# Output a boolean
True
# This is a list
[5, "Some String", True]


# ## Output
# Typically in a Python program if we want to show the user some response we need to use a print function to see the result.  Here's a few examples:

# In[ ]:


print("This is a string")
print("This is a number: ", 5)
print("This is a boolean:", True)


# One of the reasons we use Jupyter notebooks is so that we can see the result immediately without having to run the entire code base everytime, we can just run one piece of code at a time.  Also, Jupyter doesn't require us to `print` our output (it's just a handy way to try something without worrying about extra syntax).

# In[ ]:


# We can add numbers
2+2


# ## Working with numbers
# Computers do math really well. Working with numbers is one of the easiest ways to bridge the gap between algorithms and syntax.  If I were to ask you to count up the number of apples and oranges in a grocery basket, you know that you can simply count the apples and add to that number the number of oranges.  This translates really well to Python, adding two numbers is done with a `+` sign.  The next section covers all the different operations we can perform on numbers.

# ### Operators
# [Operators](https://www.tutorialspoint.com/python/python_basic_operators.htm) are the constructs that execute on operands.  For instance, in the equation 4+5,the operator is '+' and the operands are 4 and 5.  For more details on all the Python Operators check the [on-line docs](https://docs.python.org/3/library/operator.html#mapping-operators-to-functions).
# 
# A few of the most valuable ones to us are '+', '-', '*' (multiplication), '/' (division), '>', '<', '=', and '=='.
# 
# 

# In[ ]:


53*285


# With Python, math works exactly as you expect.  Equations are evaluated left to right, and the order of precidence can be changed using parentheses.

# In[ ]:


5+5*5 # This equals 30 because 5*5 happens first (order of precidence)


# In[ ]:


(5+5)*5 # This evaluates to 50 because we have told Python to add first due to parenthesis


# In[ ]:


5*(5+5) # Same thing, this will be 50 because of parens


# Feel free to go to the previous cell and try a few more calculations.  Or if you want to keep the original, just 'insert' a cell above this one and try a few others.
# 
# 

# #### About = and ==
# Python uses a single `=` sign to specify assignment, whereas a double `=` like `==` is a check for equality.  So,
# ```python
# a = 5 # Set the value of a variable named 'a' to be the value 5
# a == 5 # Returns True if the value of the variable a is 5 or False otherwise
# ```
# 
# So in the example below, after assigning x to the value 10, the second statement tells us if the value of x is indeed 10

# In[ ]:


x = 10  # Doesn't display anything, we are just assigning the value 10 to the variable x
print(f'The value of x is {x}')
x == 10 # Displays True


# ### Booleans
# 
# Boolean dataypes play an extremly important role in programming.  In fact, booleans are the only way in which decisions can be made in our code.  (In the next section we'll see how these decisions are made).  

# As a reminder, of the rules of boolean math
# 
# *AND*|True|False        
# -----|-----|-----|
# **True**| True | False|
# **False**| False | False|
# 
# <br>
# 
# 
# *OR*|True|False
# -----|-----|-----|      
# **True**| True | True|
# **False**| True | False|
# 
# 

# So therefore the operators `>` greater than, `<` less than and `==` equal to (and their counterparts `>=`, `<=`, and ~ (not)) are extremely important.  Run the next cell for examples

# In[ ]:


print('Is 10 equal to 10? ')
print(10 == 10) # This will return True because 10 is equal to 10
print()
print ('Is 10 less than 5?',10 < 5) # This will of course be false


# This one is a little trickier, before you run the cell what do you think the result will be?
# 

# In[ ]:


(15 < 5) == False


# Did this come out the way you thought?  Let's break it down a bit...
# 
# We start by evaluating the left side, (15 < 5).  Of course we know that this is False so we can replace the left side with False
# 
# ```
# False == False
# ```
# 
# Now it's easy to see, that False does indeed equal False, therefore the result is True!

# ## Variables 
# As you are no doubt already aware, variables are text used to store values in our programs.  The computer doesn't care what you call your variables, but other humans do, so name your variables something useful such as
# ```python
# width = 5
# height = 12
# area = width * height
# ```
# 
# You will notice when we use assignment (`=`) that the value is not displayed on the output of the cell, also if we try to use a variable before it has been defined we'll get an error.  Try executing the next cell.  
# 
# You should get an error like
#     
#     NameError: name 'Area' is not defined
#     
# Try removing the n on the last line and replace that line with the variable 'area'

# In[ ]:


width = 5
height = 12
area = width * height

print(Area)


# In[ ]:


width = 5
height = 12
area = width * height
print(area)


# What we tried to do was to show the value of a variable before we gave it a value!  Let's edit the previous example and replace `n` with the variable `area` instead.

# ### Strings
# Besides numbers, Python can also manipulate strings.  Strings are one of the most basic concepts in many languages and have tremendous value, as we most often use text to communicate with users.  Strings are used to provide real time feedback (think text boxes and labels, usernames and passwords), error messages, status logs, and communication with other programs.  Getting good with manipulating strings is extremely important to be successful.  Read about all the things you can do with strings in the Python [tutorial](https://docs.python.org/3/tutorial/introduction.html#strings).
# 
# Strings in Python can expressed in several ways.  They can be enclosed in single quotes('...') or double quotes("..."), both are equally acceptable. 

# In[ ]:


print('spam eggs')  # single quotes
print("Yes, I said that")  # double quotes


# If you need to use one or the other in your string definition, you can use the '\' as an escape character or just define the string using the opposite type of quote (that is if you need a single quote then wrap your string in double quotes).  Run the next cell to see the results (note that the output for the interactive cell will always quote strings in single quotes.  

# In[ ]:



'doesn\'t'  # use \' to escape the single quote...
"doesn't"  # ...or use double quotes instead
'"Yes," they said.'
"\"Yes,\" they said."
'"Isn\'t," they said.'


# If you want a cleaner version of the output try using ```print()``` instead

# In[ ]:


print('spam eggs')
print('"Yes," they said.')


# #### Joining strings together
# Strings have some other handy features as well.  Say we want to put two strings together, that's easy just use the '+' operator.  

# In[ ]:


print('Hello '+'World!') # Two strings concatenated together


# What's more, all Python objects can be represented as strings (some more cleanly than others) so we can use this handy trick to show the result of a function for instance, we just have to tell Python to convert the thing to a string.

# In[ ]:


print('4 + 3 = ' + str(7)) # We need to tell Python this is supposed to be a string


# Of course this also works with variables so long as they are strings as well

# In[ ]:


seven = '7' # Assigning the value of 7 to the variable named seven
print('4 + 3 = ', seven) # Since 'seven' is already a string (see the quotes above) no need to tell Python to convert.


# #### String formatting
# This can be a little clunky when dealing with a string that has some variable in the middle of it like:
# "Hi, my name is Michael.  What's your name?"
# 
# In order to change the name `Michael` to a variable the result would be something like
# ```python
# my_name = 'Michael'
# 'Hi, my name is '+my_name+'. What\'s your name?'
# ```
# That gets ugly real quick.  Fortunately, Python has helped us out by giving us 'f-strings' (f stands for format).  So what we can do instead is to put an expression in the middle of the string and have it figured out when we need the string.  So the last example looks like:
# ```python
# my_name = 'Michael'
# f'Hi, my name is {my_name}. What\'s your name?'
# ```
# In this way, everything in the `{}` are figured out at the last possible minute.  Here's a few more examples

# In[ ]:


#Try it!
my_name = 'Joe'
print(f'Hi, my name is {my_name}. What\'s your name?')


# And since everything inside the `{}` is just seen as Python code we can ask Python to do some work and put the result into the string right away rather than putting in an intermediate variable

# In[ ]:


# We can use the result of a statement in a string
x = 4+8
print(f'Calculating stuff is easy too, see 4+8 = {x}')

# Or we can let Python calculate it straight away and skip defining the variable
print(f'Calculating stuff is easy too, see 4+8 = {4+8}')


# ## Input
# While sending the results of calculations to the screen, to a file or across the world is super helpful and one of the main activities we'll automate with Python.  Soliciting input from outside the program is equally helpful.  We'll look at many different ways of getting data later on, but for now, the simplest way to do this is to use the `input` function.  `input` will prompt the user to type some text in response to an optional prompt.  Try the next cell and see what happens. (You may notice that the cell continues to run until you have answered the prompt and hit the enter key.)

# In[ ]:


input('Hello, what is your name?')


# Just like other actions in Jupyter, the result of the operation is immediately shown in the cell's result.  Usually we want to keep track of what was given to us so that we can use it later on.  In this case, we can use a variable to capture the result of the `input` function and then print it.  See the next example.

# In[ ]:


# Ask the user for their name, store the result in the variable user_name
user_name = input("Hello, what is your name?")
print("Your name is: " + user_name)


# One thing that is important to note is that the result of the `input()` function is always a string, even if the user types in numbers.  This means if we want to assume that the result is a number that we will have to convert it from a string to a number.  Try the next example:
# 
# (NOTE: if you don't enter a number as input, you will get an error message.  We'll talk about how to deal with this a bit more gracefully later, but for now it would be best to just input numbers at the prompt.)

# In[ ]:


# Ask the user for their age, store the result in user_age
user_age = input(f"Hello, {user_name}.  What is your age?")
print(int(user_age))


# ### Your turn- Hello, World!
# For this exercise, write the classic Hello World! with a twist.  Your output should be a string that contains an introduction to yourself, by stating your name and your age (not your real age if you don't wish).  You can use string concatenation or f'strings, it's up to you.  Two caveats, we want to make this easy for someone else to try and your age never stays they same, therefore the name must be stored in a variable `my_name` and the age should be calculated based on the current year something like `age = 2020 - 1985`.
# 
# The output should look like<br>
# ```
# Hello World!  My name is Michael and I am currently 40 years old
# ```
# 
# **BONUS**: _Can you calcuate your age in months instead of years?  How about days? (built in date functions is cheating)_

# In[ ]:


# Display a string introducing yourself to the world with your name and your age


# In[ ]:


# Can you now combine what you've learned and ask the user for their name and then their age, 
#  then respond with a statement similar to the output above?


# ### Lists
# Python knows about a number of different _compound_ data types that is ways to store many values together.  Two of the most common are _list_ and _dictionary_.  We'll start first with a list and then give you a chance to work with a list in a simple challenge.
# 
# Lists are written as a set of values between square brackets that are separated by commas.  While lists, can have different types of 'elements' most often they are the same type.

# In[ ]:


squares = [1,4,9,16,25,36] # This is a list of squares
people = ['Alice', 'Bob', 'Charlie'] # this is a list of people's names
print(squares)
people


# What is super handy about lists is that they can be indexed, that is we can ask for a particular item in the list.  The first item in the list is  index 0 the last item in the list is the `length of the list-1`.  So a list with 5 elements can be indexed on any value between 0 and 4.  

# In[ ]:


print('The item in index 0 of the list (the first item) is: ',squares[0])

print('The item in index 4 of the list (the fifth item) is: ',squares[4])


# In[ ]:


# What happens if you try to get the item at index 5?


# #### Slicing
# Sometimes we want more than one item in the list, in that case we can ask Python to get sequential items by telling it the first item we want and the last item. (It can be a little confusing, but Python doesn't include the right side of the slice, so that a slice of 0:2 only includes items 0 and 1).

# In[ ]:


people[0:2] # Give me the items in slot 0 and slot 1
squares[1:4] # Return the items from slot 1 to slot 4 (non-right inclusive)


# The full syntax of the `slice` subscripting method is [start:stop:step] meaning if we want to get every other item then we just define the `step` to be 2, if we want every 3rd item, then the step is 3 and so on.

# In[ ]:


squares = [1,4,9,16,25,36] 
# This notation says, starting at index 1, move 2 spots and give me the next number until I reach index 6
squares[1:6:2] 


# And if we leave a part out, Python guesses what we mean.  For instance if we leave out the starting point, Python assumes 0, if we leave out the end point, Python assumes the end, and if we leave out the step Python assumes 1.

# In[ ]:


print(f'Leaving out the starting point')
squares[:4:2]   # Give me the items starting at index 0 to index 4 by 2's
print(f'Leaving out the end point')
squares[2::3]   # Give me the items starting at index 2 (9) to the end, by 3's


# Finally, Python also knows what do with negative numbers.  We can use negative numbers to index starting at the right or as our step.

# In[ ]:


squares[-1]   # Give me the first value starting on the right of the list
squares[5::-1]  # Starting at index 5, give me all the values in reverse order


# For more see [sequence types](https://docs.python.org/3/glossary.html#term-sequence) (including strings) and [slicing](https://docs.python.org/3/library/functions.html#slice).

# Lists support concatenation just like strings

# In[ ]:


squares + [49,64,81]


# Lists are changable too, so we can do something like

# In[ ]:


f'Names before the change: {people}'
people[1] = 'Bonita'
f'Names after the change: {people}'


# Another handy feature of sequence types is that support several built-in functions.  Probably one of the most useful is the `len()` function, which returns an integer that shows the length of the sequence.

# In[ ]:


len(people)
len(squares)


# Finally, lists can contain other lists.  In the example below, I've created a list of numbers `n` and a list of letters `l`.  Then I created a list that has two items in it, the list `n` and the list `l`.

# In[ ]:


n = [1,2,3]  # Define a list of integers and assign it to a variable named 'n'
l = ['a','b','c'] # This is a list of characters in a list called 'a'
x = [n,l] # Here we are creating a list of lists!
print(x)


# So, the first item in the list is actually the list `n`, and the second item in the list is the list of letters `l`

# In[ ]:


print(f'The item at index 0 is a list of numbers : { x[0]}')
print(f'The item at index 1 is a list of letters: { x[1] }')


# So if we want to get at the items in list `n` we can unpack the list into another variable or use a shortcut.

# In[ ]:


# We can assign the list to a new variable first and then index it 
y = x[0] # Assign y to the list of numbers
print(f'The value in the index 1 of the sublist is {y[1]}\n')

# Or we can just do a double subscript
print(f'Same value using the double subscript approach:')
print(x[0][1])


# ## Your Turn - Hello Worl?
# For this challenge, use what you have learned about strings, integers and indexing to fix the message stored in `message`.  It seems that when I typed up this example I left out a letter and also used a question mark instead of a `!`.  Can you fix this by using indexing and replacement and then print the parts into a single line?
# 

# In[ ]:


message = ['Hello', 'Worl','?']

print(message[0]+' ' + message[1]+message[2])


# In[ ]:


# Don't change this declaration directly, instead just manipulate the output by putting the correct
# in place of the ellipsis `...`

message = ['Hello', 'Worl','?']

message[1] = ...
message[2] = ...

print(f'{message[0]} {message[1]}{message[2]}')


# In[ ]:


# One more challenge.  The list here is the number of days in the months of the year.
# Complete the code below so that it tells the days of the month requested
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
print('The number of days in June is: ', days_in_month[5])
print('The number of days in December is: ', ...)
print('The number of days in Jan and Feburary together is:'...)


# ## Dictionaries
# 
# Lists are great when we are okay with accessing the items in order or if we know exactly where the items in the list are that we want, but sometimes it is handy to access items in a collection using a more descriptive name.  One approach is to use a data structure called a dictionary.  Dictionaries are similar to lists in that they store a collection of items, but instead of using numbers to get to the content we can use strings.
# 
# Name|Number|
# --------|---------------
# |Alice | 555-479-2222|
# Bob | 555-555-1234 |
# Charles | 888-555-9889

# Say we want to store a list of people's phone numbers.  It would be really inconvenient to put there name and phone number in a list and then search everyone for who we are looking for.  
# 
# ``` 
# phone_numbers = ['Alice 555-479-2222',
#                  'Bob 555-555-1234',
#                  'Charles 888-555-9889']
# ```
# 
# Instead we can store the phone numbers in a list and use the names as the 'keys' to lookup the phone numbers.
# 
# In order to define a dictionary we have to provide both the 'key' (the index) and the 'value' (the thing we are storing).  These are separated by a ':' and we separate items within the dictionary with ',' just like in a list.

# In[ ]:


# This says, create a dictionary where Alice, Bob and Charlie are the keys/index
#   and their numbers are the values
# Notice, the items are on separate lines for readability
phone_numbers = {'Alice':'555-479-2222',
                 'Bob':'555-555-1234',
                 'Charles':'888-555-9889'}

# Then we can grab just Alice's phone number
print("Alice's phone number is " + phone_numbers['Alice'])

# And also we can get Bob's
print(f"Bob's phone number is: {phone_numbers['Bob']}")


# ### Your Turn - Dictionaries
# In the next code block, again we'll see the days of the month, but instead of knowing which month it is in the year, we're going to store the dates using the month's name.

# In[ ]:


days_in_month_dict = {'Jan':31,'Feb':28,'Mar':31, 'Apr':30, 'May':31, 'Jun':30, 'Jul':31, 'Aug':31, 'Sep':30, 'Nov':30, 'Oct':31, 'Dec':31}
print('The number of days in June is: ', days_in_month_dict['Jun'])
print('The number of days in December is: ', ...)
print('The number of days in Jan and Feburary together is:'...)


# ## Conclusion
# This is a good start and a very basic introduction to types in Python, there are many, many more things that can be done with built-in functions to manipulate strings, numbers, dates and lists.  In order to do anything interesting (more complex algorithms) our code needs to be able to make decisions and execute different actions based on conditions - often many times over.  In the next notebook we'll look at how to get Python to make decisions and act on the results. 
# 
# Feel free to play around here by adding cells and experimenting with different language elements.  When you are ready to move on, head over to the next section.
# 
# 
# 
# 

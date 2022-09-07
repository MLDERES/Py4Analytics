#!/usr/bin/env python
# coding: utf-8

# # Making Decisions & Looping
# By now you have a solid understanding of a few of the data types that Python makes available to everyone.  Numbers, strings, list and dictionaries.  But often times we want to do more than just Python as a fancy calculator or simple word processor, for this need to combine together a set of actions that will be completed over and over again.  We want to let our algorithms make decisions or repeat actions until a particular condition is met.  
# 
# Let's take a quick look at a loop that counts from 1 to 10
# 
# Before going on, make sure that you have run the first cell in this notebook otherwise you may not see all the output that is intended**

# In[ ]:


from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"


# In[ ]:


# Start with a counter at 0
counter = 0
# While the counter is less than 10 repeat the following
while counter <= 10:
    # Output the current value
    print(f'{counter}')
    # Increment the counter by 1
    counter = counter + 1

print('All Done')


# So what's happening here?
# - The first line assigns the value of 0 to the variable `counter`
# - Next the `while` statement checks to see if the test `counter <= 10` is `True`, if it is then all the statements that are indented after the `while` statement are executed in order.  (In Python, any non-zero integer value is `True`; and zero is `False`.  This test uses a simple comparison `<=` (less than or equal), we can use many different kinds of comparisons `>`, `==`, `<=` for instance or any expression that results in a boolean value (e.g. `True` or `False`)
# - The _body_ of the loop - the statements to be executed when the condition is `True` are indented.  Indention is how Python decides that statements should be grouped together.  All the statements that should be in the body of the function need to be indented the exact same number of spaces (usually 4), most Python editors know to automatically indent lines in a group, but they don't know when you are done with the grouping, so it's up to you to un-indent when you are done closing the body.
# - Once all the indented statements are executed, Python goes back up to the top of the loop (to the `while` statement) and checks again if the statement is `True` or `False`, if it is still `True` then the _body_ will be run again.  If the statement no results in `False` (such as when the value of `counter` becomes 11), then Python skips the indented statements and continues executing the program, in this case the final `print()` statement.

# ## Reminder about boolean math
# Boolean math is incredibly important to manage the flow of most computer programs.  So as a quick reminder, Boolean values can only be 1 or 0, that is `True` or `False`.  `and` means that both values must be `True` for the statement to be `True`, while the `or` statement says that only one of the values must be `True` in order for the condition to evaluate to `True`.  For instance,

# In[ ]:


print('True and True is: ')
print(True and True )
print()

print('True and False is:') 
print(True and False)
print()

print(f'But True or False is:') 
print(False or True)
print()

print('And False or False is: ')
print(False or False)
print()


# |*OR*|True|False|
# |------|----|-----|
# |**True**|True|True|
# |**False**| True|False|
# 
# <br/>
# 
# |*AND*|True|False|
# |------|----|-----|
# |**True**|True|False|
# |**False**|False|False|

# We can use combinations of expressions that evaluate to booleans and the boolean values themselves in different combinations, all of the following statements yield _True_

# In[ ]:


(4 < 5) and True

(4 < 5) and (6 < 9)

(1 == 2) or True


# Python also gives us a unary operator _not_, this simply means that the operation only works on a single value not two like _and_ and _or_.  The _not_ operator simply evaluates the opposite of the boolean value.

# In[ ]:


# This evaluates to False
not True 

# What do you think this evaluates to?
not not True


# (code-blocks)=
# ## Blocks of Code
# One more item we need to address before we get too far, code blocks.  While code is mostly meant to run from the top to the bottom on the page, we can put groups of statements together into code blocks. You can tell when you are looking at a code block because of indentions.<br/>
# 
# Three rules apply to code blocks
# 1.  Blocks begin when indention increases
# 2.  Blocks can contain other blocks
# 3.  Blocks end when the indention decreases to zero or a containing block's indention
# 
# You've seen an example of this already, but let's look at one more and be explicit.
# 
# ```python
# name = 'Daniel'
# password = 'baby tigers are cute'
# 
# if name == 'Daniel':
#     print('Hello Daniel')
#     if password == 'baby tigers are cute':
#         print('Access granted')
#     else:
#         print('Access denied')
# 
# print('Next Command')
# ```
# Here we have a code block that starts with `print('Hello Daniel')` **(rule 1)** and contains all the lines up to `print('next command')` **(rule 3)**.  There are two other code blocks `print('Access granted')` and `print('Access denied')` **(rule 2)**.

# ## Flow Control
# Most of the interesting algorithms that we want to automate are more complex than just a list of tasks.  We often have to react to changing conditions or adjust the list of steps based on outcome of previous steps or the environment.  For instance, if we are going to make a PB&J sandwich, we might want to ask the person that is going to eat the sandwhich if they would like the bread toasted first.  If they say yes, then we will add a step to our algorithm which says "toast the bread".
# 
# __Making a PB&J__ (on bread or toast)
# * Gather bread, peanut butter, jelly
# * Take out two slices of bread
# * Ask the consumer, "Do you want the bread toasted?"
# * If YES then 
#     * Toast bread
# * Place bread (or toast) onto a plate
# * Spread PB onto a single slice of bread/toast
# * Spread jelly onto other slice of bread/toast
# 
# Notice that all the steps will be executed exactly the same, except that if the bread is to be toasted, we'll add one more step.
# 
# ### Conditional Statements
# The most well-worn statement in all of programming is the `if` statement.  This expressions says: _if this condition is true, then execute the next block of code_.  One step further, we might want to take a different path 
# 
# Following is an example using Python

# In[1]:


## Ask the user for a number which is greater than zero.
## If the number is less than 0 change the value to zero

# When asking for input, the result is always a string
user_response = input("Please enter integer: ")
# We'll need to change it into an integer
user_input_as_int = int(user_response)

# Save the result ahead of the checks
result = user_input_as_int
if user_input_as_int < 0:
    print('Value was less than zero, setting to 0')
    result = 0

print('The result is: ',result)


# ### Alternate paths
# Even more interesting are scenarios where we choose one of two different paths (or more) and do something different in either path.  For instance, what if we offer the consumer the choice between grape (default) or strawberry jelly.  Most of the steps are the same, but we would use a different jar of jam based on the user's preference.
# 
# __Making a PB&J__ (with choice of jelly)
# * Gather bread, peanut butter, jelly
# * Take out two slices of bread
# * Ask the consumer, "Do you want the bread toasted?"
# * If YES then _Toast bread_
#     * Place bread (or toast) onto a plate
# * Spread PB onto a single slice of bread/toast
# * Ask the consumer, "Would you like grape jelly or strawberry?"
# * If STRAWBERRY then
#     * Get out the strawberry jam jar
# * Otherwise (assume grape)
#     * Get out the grape jelly jar
# * Spread jelly onto other slice of bread/toast
# 
# The key to this example is that our default option is to select grape jelly and we only do something different if we want to use strawberry.  Notice, if we didn't specify the alternative (get out the grape jelly) we wouldn't have any jelly to put on the bread later.
# 
# Next, we'll create a simple number guessing game.  If the user guesses our number then we'll let them know they got it, otherwise we'll tell them they didn't.
# 
# **??** What would happen if we don't do the _else_ part of the conditional statement?  Try it out.
# 

# In[ ]:


import random
# Get a number between 0 and 10
our_random = random.randint(0,10)

# When asking for input, the result is always a string
user_response = input("Please enter integer: ")
# We'll need to change it into an integer
user_input_as_int = int(user_response)

if (user_response == our_random):
    print("Congratulations you guessed it!")
else:
    print("Didn't guess it this time")

print(f"My number was: {our_random}")


# ### Multiple alternatives
# Some people actually like bananas on their peanut butter sandwiches (yuck!), but since it's an option, let's allow our consumer to choose between one of the two jelly choices or bananas.
# 
# 
# __Making a PB&J__ (with choice of jelly)
# * Gather bread, peanut butter, jelly
# * Take out two slices of bread
# * Ask the consumer, "Do you want the bread toasted?"
# * If YES then _Toast bread_
#     * Place bread (or toast) onto a plate
# * Spread PB onto a single slice of bread/toast
# * Ask the consumer, "Would you like grape jelly or strawberry?"
# * If STRAWBERRY then
#     * Get out the strawberry jam jar
# * Otherwise If BANANAS then
#     * Get bananas ready to put on the sandwhich
# * Otherwise (assume grape)
#     * Get out the grape jelly jar
# * Spread jelly or bananas onto other slice of bread/toast
# 
# We can have an infinite number of choices (though we try to generalize our approach to as few options as possible to keep our code simpler).
# 
# In Python we use the keyword `elif` as-in "else-if", this is a short cut for a new code block so where we would have to do
# ```
# if `some condition is true` then
#    first_condition was true
# else
#     if `some second condition is true` then
#         some second condition was true
#     else
#         neither the first or second condition was true
# ```
# 
# In the cell below, let's change the game to let the user know if their pick was high or low.

# In[ ]:


# Get a number between 0 and 10
our_random = random.randint(0,10)

# When asking for input, the result is always a string
user_response = input("Please enter integer: ")
# We'll need to change it into an integer
user_input_as_int = int(user_response)

## If the value was too high
if : 
   print("Didn't guess it this time, your guess was too high")

# If the value too low
elif :
    print("Didn't guess it this time, your guess was too high")

else: 
    print("Congratulations you guessed it!")

print(f"My number was: {our_random}")


# ### Conditions in other languages
# `if` statements are incredibly valuable and are seen nearly everywhere in all different kinds of applications.  Every language uses `if` statements, it is just the syntax that changes.  For instance, you have likely seen in Excel something like 
# ```
# =IF(A1 < B1, "Yes", "No")
# ```
# In this simple example, we are testing if the value in cell A1 is less than the value in B1 and if so, place _Yes_ in the current cell, otherwise fill the cell with _No_.

# ## Repeating Statements
# Another useful feature of common algorithms that we tend to use is to repeat a set of steps.  For instance, printing address labels for all our customers, reading lines from a file, or processing items in an ecommerce basket.  These situations may not happen quite as often in real life, but with compute power - repeating tasks is super cheap and incredibly efficient.
# 
# There are two common kinds of loops in Python.  
# * Looping over a known set of items.  The set of items can be numbers, strings or something else.  For instance, make 4 sandwiches or make sandwiches for Alice, Bob and Charlie.
# * Continue to loop until a condition is met.  An example of this would be: keep making sandwiches until someone tells us to stop.
# 
# ### `for` statement
# The `for` statement in Python is an incredibly valuable and prevalent statement.  This statement will iterate over a some sequence of items (e.g. a list, letters in a string) with each pass assigning the next item to a common variable.  Let's take for instance
# ```python
# words = ['cat','house','window']
# for w in words:
#     print(f'{w}')
# ```
# In this simple example, the variable `w` is assigned the value `cat` for the duration of the code block following the for statement, then when the block has completed, `w` is assigned the value `house` and finally `window`.  The next cell shows this in action.
# 

# In[ ]:


words = ['cat','house','window']
for w in words:
    print(f'{w}')


# ### Creating a list of numbers automatically with `range`
# In order to execute a for loop, it is sometimes helpful to have a sequence of numbers to iterate over.  And while you could type out a list with each number it in, that gets cumbersome and error prone.
# ```python
# for i in [0,1,2,3,4]:
#     print(i)
# ```
# This is where the `range` function comes in.  `range` will generate an arithmetic progression given the number of items you specify for instance.
# ```python
# for i in range(5):
#     print(i)
# 0
# 1
# 2
# 3
# 4
# ```
# In this case, we asked for 5 numbers, so Python started at 0 and created us 5 numbers (0-4).  You can also specify a different starting number and the increment (or decrement!) called step.  Here's a few examples.  (Note: `range` is a special datatype which doesn't have an expected string representation, so we have to make it into a list for viewing, this is not necessary when using it directly)

# In[ ]:


list(range(5,10)) # Values starting with 5 up to (not including 10)
list(range(0,10,3)) # Every 3rd number starting at 0 up until (not including 10)
list(range(10,0,-1)) # Starting at 10, count *down* to 0 (not including 0)

for i in range(10,0,-1):
    print(i)


# Below is one more fun example.  Combining `for` loops with decision making `if` statements.  Don't be put off by the use of emojis instead of characters, strings or numbers.  Emojis are just characters like any other character as far as Python is concerned.  (Which means you could use these in your variable or function names, but you probably shouldn't if you want your code to be understood by other humans).

# In[ ]:


# Here's another fun example
# In order to type an emoji anywhere in Windows, just press ⊞ Win + .
all_the_fruits = '🍇🍈🍉🍊🍌🍍🍑🍒🍓🍋🍐🍎🍏🥭'  # Notice this is just a string

# This is a list of "characters"
fruits_i_like = ['🍇','🍊','🍌','🍍','🍒','🍓']

# This statement says:
# One at a time, assign the characters in the string 'fruits_i_like'
#    to the variable named fruit
for fruit in all_the_fruits:
    print(f'{fruit}')
    # Check if the current fruit is in the list of fruits I like
    if fruit in fruits_i_like:
        print(f'I like this one {fruit}!')


# So as you can see, with just these two simple statements `if` and `for` we can implement some pretty interesting algorithms.
# 
# Now would be a good time to head over to the [exercises](../exercises/120-Flow_Control-ex.ipynb) and try a couple on your own.

# ## `while` Statements
# You have already seen an example of the `while` statement a bit earlier, but it is helpful to address again briefly.  The `while` statement is useful when the condition that is being tested happens _in the code block of the loop_.  For instance, `while` loops are often used when reading lines from a file.  
# ```python
# line = ''
# while not line is not None:
#     print(line)
#     line = read_line_from_file(f)
# ```
# In this case, we start by setting the value of `line` to be an empty string, then we tell Python to continue to execute the code block until the value of `line` has no value.  If we were to do this with a `for` loop, we would need to know ahead of time how many lines were in the file or have a specific number of lines in mind.  For instance,
# 
# ```python
# line = ''
# for line_number in range(num_lines_in_file):
#     line = read_line_from_file_by_number(file, line_number)
#     print(line)
# ```
# 
# ````{caution}
# Because of the way the blocks execute in `while` loops vs `for` loops, you will often see a little different logic.  For instance, with a `while` loop, the first value is set before the loop starts so typcially we will use the value initially and the last step in the loop is to update the condition we are checking.  In `for` loops the value is set when the loop starts, so there is no need to update the condition in the loop.
# ````

# One more common use of `while` is to avoid getting bad data from user inputs.  So for instance, the next cell shows an example of asking the user to specify a value between 1-10.  So long as the user doesn't provide a valid value, the prompt is repeated.
# 
# Next we'll go back to our guessing game and this time, we'll let the user continue to guess until they get the right answer.

# In[1]:


# Get a number between 0 and 10
our_random = random.randint(0,10)

# We need to establish the check condition before the loop starts
user_input_as_int = int(input("Please enter integer: "))

# Until the users input matches our random number, do these steps
while (user_input_as_int != our_random):
    ## If the value was too high
    if user_input_as_int > our_random:
        print("Didn't guess it this time, your guess was too high")
    else:
        print("Didn't guess it this time, your guess was too low")
    
    # We need to make sure that user_input_as_int changes in the loop
    user_input_as_int = int(input("Please enter integer: "))

print(f"You got it!  My number was: {our_random}")


# ````{note} 
# There are a few things that catch new coders with `while` statements.  
# * First, the check condition will need to be established _before_ the loop starts, or else the loop won't start.  
# * Also, if there is no way for the condition to change in the loop, then the loop will not stop!
# ````

# ### How to do nothing
# There are rare occassions when our code requires us to have a block of statements even though we don't want to do anything with them.  This is common when we are starting to write our code and we want a placeholder or we aren't sure what to do just yet, but we want to be syntactically correct.  This is where we can use the keyword `pass` similar to comments, this is skipped over by the computer, but makes sure that our code works correctly.
# ```python
# if x is True:
#     pass
# else:
#     do_something_useful
# ```
# This is a poor paradigm to actually use, just know that it is helpful when you are building up your program and need a short-term placeholder.

# ## Conclusion
# Logical decision making and looping are essential building blocks in nearly every single computer application.  Everything from ensuring that data is entered correctly, to making business decisions.  Even video games are based on loops.  The main function of a video game loop is usually something like
# ```python
# while(application_is_running):
#     if move_right:
#         move_spaceship_right()
#     if move_left:
#         move_spaceship_left()
#     if button_pressed:
#         fire_missles()
#     if missle_hit_invader:
#         score_points()
#         remove_invader()
#     update_screen()
# ```    
# Pretty crazy to know that something as complex as Call of Duty is these same primitives as our simple guessing game!

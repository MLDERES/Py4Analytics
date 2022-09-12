#!/usr/bin/env python
# coding: utf-8

# # Reusing Code
# One of the fundamental skills that every programmer must have is the ability to make their code reusable.  Not just cut/paste reusable, but being able to be reused with in a variety of conditions without having to rework the code.
# 
# When you think about a simple task, like making a peanut butter and jelly sandwich, you can tell your friend how to make that sandwich with just a few words.  For instance,
# - Grab the peanut butter
# - Choose the jelly
# - Open the bread
# - Spread the PB on one slice and the jelly on another piece of bread
# - Put the bread slices together with the PB and jelly touching
# 
# We've really shortcutted a bunch of steps here right?  I mean, "grabbing the peanut butter" means going to the pantry, openning the door, finding the jar, selecting the jar, walking back...
# 
# This would get very frustating if we had to explain this over and over for each kind of sandwich we want to make or with different kinds of jelly right?  So we have learned that, using words, we can communicate whole steps without having to break down the details each time.  We might have to provide a bit of context - say, if you're at my house, the PB is in the cabinet, but at your place it's in the pantry.  But in general humans can fill in the blanks.
# 
# Computers can't fill in the blanks, we have to be very precise.  But we also don't want to have to be extremely precise everytime we want to do a simple task, so we use abstractions in programming to help us with the mundane.  One example, the `print()` statement we saw earlier.  There is a lot of stuff happening to make a couple of letters appear on the screen.  Fortunately for us, someone else figured this out already and we can rely on their work.  
# 
# Functions (in other languages called subroutines) are self-contained lines of code which accomplish a specific task.  Functions can "take in" data, process it, and then "return" a result.
# 
# ## Defining Functions
# In Python we define functions with the `def` keyword followed by the name of the function, a set of parenthesis, and a `:`.  To use the function, we just type it's name and the parenthesis. (There are a few more options, but this is the simplest form.)
# 

# In[ ]:


# This function will output the phrase, Hello World!
def say_hello_world():
    print('Hello World!')

say_hello_world()


# Now that we have defined the function, we can call it over and over again without having to define it again.  Even better, if we decide to change it - we don't need to update the code that is calling the function to change it.
# 
# You can try it here.  Create a new code cell and type `say_hello_world` into the new cell and see it prints out the same message.

# Functions can replace several lines of code into a single statement when used, because they "encapsulate" the details.  In this example, we just repeated the `print()` function but what about something more complex like getting input from a user and then responding to the message.  Could we shortcut all this into one function?

# In[ ]:


# Say hello to a particular user
def say_hello_user():
    users_name = input("What's your name?")
    print("Hello, ",users_name," it's nice to meet you!")

say_hello_user()


# Functions can be very simple or much more complex.  The best practice though is to make functions just big enough to complete a task and no more.  This could mean calling other functions and doing some other processing, but let's not worry about complexity just yet.

# ## Configurable functions
# While our previous examples were simple, they weren't very useful because they only do one thing.  Most often what we want to complete a task with some specific parameters or configurable steps.  For instance, the `print` function wouldn't be very helpful if we had to write a new function everytime we wanted to change the output! Instead, we can send in the characters we want outputted to the screen using _arguments_.  Functions define temporary variables to hold the value of these arguments, called parameters.
# 
# Starting with a simple example.  Let's rewrite our `say_hello_user()` function, but this time, let's supply the greeting and the users name outside of the function.

# In[ ]:


# Say hello to a particular user
def say_hello(greeting, name):
    
    print(greeting, name)

users_name = input("What's your name?")

# We can pass parameters with a "fixed" value or as a variable
say_hello("Hello ", users_name)
say_hello("Hi ", users_name)
say_hello("Ciao ", users_name)


# ## Getting something back
# Many functions are helpful just as they are, they do some work and then go away.  Sometimes we want feedback from a function or the result of doing some work in a function.  In these cases, we use another Python keyword `return`.  The `return` keyword says the function is complete and this bit of information is the result of the effort.  As a caller of the function we can use the returned value just like we use variables, we can assign it to variable for safe-keeping pass it along to another function or ignore it all together.

# 
#   Let's consider a simple example:
# ```python
# def add(a, b):
#     c = a+b
#     return c
# ```
# Here we have a function named `add`, we know it is a Python function because it has the word `def` in front of the name.  Our `add` function "takes in" two values (paramters) named `a` and `b`, these two values become variables that exist only while the function is called we call these _function parameters_.  Finally, our function does something useful and sends back the result `c`.  So now, when we want to use this function, we just need to specify the name of the function, the value for the two parameters and collect the result into another variable.

# In[ ]:


# Add the numbers represented by the parameters a and b
def add(a, b):
    c = a+b
    return c

return_value = add(5,4)
print(return_value)


# Now what we have is a function that will perform a set of actions, but we don't have to know ahead of time what the values for `a` and `b` will be.  We just know that they should be two numbers.
# 
# This is a very simple example of course and the number of lines in a function can be very long.  As a matter of fact we can even call other functions inside of our functions.

# In[ ]:


def multiply(x,y):
    z = 0
    for i in range(y): 
        z = add(z,y) # Calling our add function
    return z

print(multiply(5, 4))


# ## Why write functions?
# <ol>
# <li><b>Functions allow us to conceive the program as a series of steps where each substep is captured in its own block.</b><br/> When a program seems too difficult, break down the substeps functions.  And if necessary, break that sub-step down into another function, keep going until each substep is understandable and does exactly one task, then combine the steps together into bigger subtasks.</li>
# <li><b>Functions allow us to reuse code.</b><br/> This is essential, because it saves us from typos, ensures that we are doing calculations and tasks consistently whereever it is used and even allows others to use our code without understanding how the subtask is executed.</li>
# <li><b>Functions encapsulate the variables keeping our "namespace" clean.</b><br/>  Since a, b, and c only contains values when the function is called, we can use the variable names a, b and c as parameters in other functions or in our main code without confusion.</li>
# <li><b>Functions allow us to test our program in small pieces.</b><br/>  If we can execute a part of our program correctly by calling just one function, then we can continue to build our program knowing that the building blocks are solid.</li></ol>

# ## Best Practices
# There are a few things that should be considered when creating functions in any language and a few things that are specfic to Python.
# <ul><li><b>Functions should perform exactly one task.</b><br/> Functions should have a very specific and limited intention.</li>
# <li><b>Documenting your function is a must.</b><br/>  You may not believe this now, but even the best programmers forget how their function is supposed to work or what it was supposed to do when the come back to use it a few days, months or years later.  The convention in Python is to write documentation comments immediately after the function definition.</li>
# <br/>
# <div style="indent:20px">There are several different common formats <a href="https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings">Google has their own</a>, another is based on <a href="https://en.wikipedia.org/wiki/ReStructuredText">reStructuredText - ReST</a>, and also <a href="https://numpydoc.readthedocs.io/en/latest/format.html">numpydoc</a>. Which format you choose is mostly up to you, although sometimes a project will already have defined the standard when you get to work on it.<div>
# <br/>
# <li><b>Function names, and their parameters should be as descriptive as possible.</b><br/> While these examples above use parameter names like a and b (there is no reason to name them differently) the function names themselves immediately tell you the purpose and do exactly what you expect (add numbers, subtract numbers).</li>
# <li><b>Function names ought to use all lowercase letters and use '_' to separate words.</b><br/> If your function name is more than a single word, it is common practice (in Python, other languages differ) to separate the names with an `_` character.  For instance</li>
# <li><b>Function parameters should be descriptive</b><br/>Functions can be self-documenting if the coder uses good names for the function name and also for the parameters.<br/>
# 
# ```python
# def this_is_a_long_function_name(with_well_defined_parameters):
#     return None
# ```

# In[ ]:


def power(x,y):
    ''' 
    Raises x to the power of y and returns the result
    
    Parameters:
    -----------
    x: int - the base number
    y: int - the exponent
    
    Returns:
    --------
    int : result of performing the operation
    
    Example:
    --------
    >>> power(2,3)
    8
    
    '''
    return x ** y


def add_subtract(x, y, add=True):
    '''
    This function will either add or subtract the two values provided

    Parameters
    ----------
    x : int
        the first value in the equation
    y : int 
        the second value in equation

    Returns:
    --------
    int : result of performing the operation
    
    Example:
    --------
    >>> add_subtract(4,4)
    8
    >>> add_subtract(3,8, True)
    11
    >>> add_subtract(4,4, add=False)
    0
    >>> add_subtract(3,8, False)
    -5
    '''


# ## Conclusion
# You've learned quite a bit in this set of exercises and probably already knew some it.  Next, put your skills to the test in the [Exercises](../exercises/130-Functions-ex.ipynb).

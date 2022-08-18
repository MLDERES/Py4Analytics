#!/usr/bin/env python
# coding: utf-8

# # Coding Challenges
# Now it's time to put all you have learned together to try some unique coding puzzles.  The coding challenges presented here range from very easy to challenging.  For each one there are few hints that you can use if you get stuck.  Each challenge has a space for you to write the answer and a cell following which can be executed to check your answer against a few test cases.
# 
# ```{note}
# **Before starting the challenges be sure to run the following cell first, which sets up functions for testing your answers.**
# ```
# 

# In[ ]:


#  This cell brings in a function called assert_equal() which is used to test 
#  the output of your function with the expected output.  
#  After each challenge, the cell following your code will run your function and compare the result to the expected output.
get_ipython().run_line_magic('run', '../src/challenge_tests.py')


# ## Challenge 1 - What day of the year is it?
# In this challenge you are to write a function called _day_of_year_ which accepts three integer parameters _day_, _month_, _year_ the result of the function should be an integer representing the number of days that have elapsed since January 1st of the year provided until the date.  For instance, if the function were asked for the day of the year on Feb 2, 2015 the answer returned should be 33 (31 days in Jan + 2 days in February).
# 
# Remember to take into account leap year! There are three criteria for leap year:
# <li>The year can be evenly divided by 4</li>
# <li>If the year can be evenly divided by 100 it is NOT a leap year, unless:</li>
# <li>The year is also divisble by 400, in which case it is a leap year</li>

# In[ ]:


def day_of_year(day, month, year):
    ''' A function to determine what day of the year it is.
    
    Day of the the year is a number between 1 and 366 where Jan 1 is day 1 and Dec 31 is day 366 (in 2020)
    
    Parameters
    ----------
    day : int
        The day of the month
    month : int
        The month of the year
    year : int
        The year which the day is being calculated
    
    Returns
    -------
    int
        The day of the year
    '''
    # Replace pass with your code
    pass


# Here's an example to see how your code will be run

print(f'Jan 1st is the {day_of_year(1,1,2000)} day of the year')


# You can test your work by running the next cell.

# In[ ]:


# Run this cell to test your work

assert_equal(day_of_year(1,1,2000),1,'Jan 1, 2000')
assert_equal(day_of_year(15,2,2015),46,'Feb 15, 2015')
assert_equal(day_of_year(30,6,2020),182,'June 30, 2020', 'Did you check for leap year?')
assert_equal(day_of_year(1, 1, 2001), 1, "Jan 1, 2001")
assert_equal(day_of_year(17, 11, 2020), 322, "Nov 17, 2020")
assert_equal(day_of_year(31, 12, 2020), 366, "Dec 31, 2021")
assert_equal(day_of_year(14, 8, 2021), 226, "Aug 14, 2021")
assert_equal(day_of_year(9, 5, 2022), 129, "May 9, 2022")


# ## Challenge 2 - Create me a monogram
# Traditional monograms are represented by three initials (first name, last name and middle initial).  The challenge here is to build a monogram from a name that is supplied.  The monogram should use lowercase letters for the first initial and middle initial, while the last name initial is in caps.  
# 
# For example,
# 
# <li>Dwight K. Shrute => d.K.s</li>
# <li>Eye See Deadpeople => e.S.d</li>
# <li>Mers Sadees Benz => m.B.s</li>
# 

# In[ ]:


def monogram(full_name):
    '''
    Creates a traditional monogram from a supplied full name
    
    Parameters
    ----------
    full_name : str
        The full name (first middle last) of the person for which to build the monogram
    '''
    # Replace pass with your code
    pass

# Put your name here to try out your monogram function
my_name = ''
print(f'My monogram is {monogram(my_name)}')


# In[ ]:


# Run this cell to test your work

assert_equal(monogram('Dwight Kevin Shrute'),'d.S.k')
assert_equal(monogram('Eye see deadpeople'),'e.D.s', hint='Did you check the case?')
assert_equal(monogram('mers sadees benz II'),'m.B.s',hint='Did the extra suffix throw you off?')


# # Challenge 3 - Are you my mother?
# In this coding challenge you are to determine the matriarchical family tree given a list of mother/daughter pairs.  
# 
# For this challenge you will need to understand the concept of tuples.  A tuple is a sequence of elements much like a list, but unlike a list, tuples are immutable (that is, they cannot be changed).  Tuples are represented by the parathenses surrounding a comma separated list of items such as (5,6) or ('mother', 'daughter').  In the first case, the tuple is made up of two integers and the second case the tuple is two strings.  Accessing items in a tuple is similar to accessing items in other sequences in Python - by using square brackets.
# ```python
# > pair = ('mother','daughter')
# > pair[0]
# 'mother'
# > pair[1]
# 'daughter'
# ```
# 
# Now on with the challenge.  You will be provided a list of tuples, the first name will always be the mother of the second name.  Given this list of names, you are to develop the family tree and provide the relationship between the target pair.
# 
# For instance, if the `source_list` is 
# ```[('Enid','Susan'),('Enid','Diane'),('Susan','Deborah')] ```
# then the family tree represented is 
# ```
#         Enid
#           |
#      |--------|
#    Susan     Diane
#      |
#    Deborah
# ```
# and then if the `target_list` is `[('Enid','Deborah')]` then the correct response is `Granddaughter`, as Deborah is the _granddaughter_ of Enid.
# 
# There will only every be only 3 generations (maximum) with varying number of children for each parent, but each child will only have a single parent (we are only dealing with the females in the tree).  Your response should be one of 
# ```python
# Mother
# Daughter
# Grandmother
# Granddaughter
# Sister
# Cousin
# Aunt
# Niece
# ```
# >**Remember**
# ><li>Sisters have the same mother.</li>
# ><li>Cousins have the same grandmother.</li>
# ><li>A niece's grandmother is the mother of her Aunt.</li>
# ><li>An Aunt's mother is the grandmother of her niece.</li>
# 
# **Hint**: You may consider using a [dictionary](https://www.w3schools.com/python/python_dictionaries.asp#:~:text=%20Python%20Dictionaries%20%201%20Dictionary.%20A%20dictionary,Items.%20%208%20Removing%20Items.%20%20More%20) data type to solve this one.
# 

# In[ ]:


def relations(family_tree, relationship):
    ''' Determine the relationship between two people in a given family
    
    Parameters
    ----------
    family_tree : list of tuple of str
        The family tree is defined by tuples of mother/daughter pairs 
        where the first item in the tuple is the mother of the second name in the tuple.
    relationship: tuple of str
        The relationship to be determined of the second person in the tuple to the first person in the tuple
        
    Returns
    -------
    str : {'Grandmother','Granddaughter','Mother','Daughter','Sister','Cousin','Aunt','Niece'}
        The relationship of the second person in the `relationship` tuple to the first person in the tuple
        
    '''
    # Replace pass with your code
    pass

# You can run this to try out the function you wrote. 

# First we define the family tree.
# The variable test_family represents a family tree where:
#   Ingrid is Sally's mother
#   Ingrid is also Jackie's mother
#   Sally is Betty's mother
#   
# Therefore,
#    Sally and Jackie are sisters (same mother)
#    Ingrid is Betty's grandmother (Sally's mother is Ingrid)
#    Jackie is Betty's aunt (Betty's mother has the same mother as Jackie)
test_family = [('Ingrid','Sally'), ('Ingrid','Jackie'), ('Sally','Betty')]

# Let's see how Ingrid and Sally are related
relationship_1 = relations(test_family, ('Ingrid','Sally'))
print(f'Ingrid is Sally`s {relationship_1}')

# Let's see how Ingrid and Betty are related (should be gradmother)
relationship_2 = relations(test_family, ('Ingrid','Betty'))
print(f'Ingrid is Betty`s {relationship_2}')

# Now let's see how Betty is related to Ingrid (should be granddaughter)
relationship_3 = relations(test_family, ('Ingrid','Betty'))
print(f'Betty is Ingrid`s {relationship_3}')


# In[ ]:


# Run this cell to test your work

family_a = [("Enid", "Susan"), ("Susan", "Deborah")]
family_b = [('Enid', 'Susan'), ('Susan', 'Deborah'), ('Enid', 'Dianne'), ('Dianne', 'Judy'), ('Dianne', 'Fern')]

assert_equal(relations(family_a,('Enid','Susan')),'Daughter')
assert_equal(relations(family_b,('Enid','Judy')),'Granddaughter')
assert_equal(relations(family_b,('Enid','Deborah')),'Granddaughter')
assert_equal(relations(family_b,('Enid','Dianne')),'Daughter')
assert_equal(relations(family_b,('Enid','Fern')),'Granddaughter')
assert_equal(relations(family_b,('Susan','Enid')),'Mother')
assert_equal(relations(family_b,('Susan','Deborah')),'Daughter')
assert_equal(relations(family_b,('Susan','Dianne')),'Sister')
assert_equal(relations(family_b,('Susan','Judy')),'Niece')
assert_equal(relations(family_b,('Susan','Fern')),'Niece')
assert_equal(relations(family_b,('Fern','Susan')),'Aunt')
assert_equal(relations(family_b,('Fern','Judy')),'Sister')


# # Challenge 4 - Money in the bank
# 
# For this challenge you are to dispense bills from an ATM in the least number of bills possible.
# 
# In this challenge you are writing the code for an ATM which can dispense up to 1500 dollars per transaction with the least number of bills possible.  The ATM has bills available in these nominal amounts 10, 20, 50, 100 and 500 and plenty of them so no need to worry about running out!  You function should return the number of bills required, if the amount requested cannot be met, then your function should signal an error by returning a -1.

# **HINT**: Python has an operator for [floor division](https://python-reference.readthedocs.io/en/latest/docs/operators/floor_division.html) which you may find helpful for this example.  You may also consider the [divmod() function](https://python-reference.readthedocs.io/en/latest/docs/functions/divmod.html?highlight=divmod())

# In[ ]:


def dispense_cash(amount):
    ''' Determine the minimum number of ATM bills to meet the requested amount to dispense
    
    Parameters
    ----------
    amount : int
        The amount of money requested from the ATM
        
    Returns
    -------
    int
        The number of bills needed, -1 if it can't be done
    '''
    pass

# Start simple
print(f'If I ask for $500, I should get back 1 bill.  Your answer: {dispense_cash(500)}')

# A bit more complex
print(f'If I ask for $110, I should get back 2 bills (1x $100, 1x$10).  Your answer: {dispense_cash(110)}')

# Finally
print(f'If I ask for $290, I should get back 4 bills (2 x $100, 1 x $50, 2 x $20).  Your answer: {dispense_cash(290)}')


# In[ ]:


# Run this cell to test your answer

assert_equal(dispense_cash(1120), 4)
assert_equal(dispense_cash(492), -1)
assert_equal(dispense_cash(440), 6)
assert_equal(dispense_cash(370), 5)
assert_equal(dispense_cash(80), 3)


# # Challenge 5 - Fruit Calculator
# 
# Given a word problem as a string, complete the calculation and return the result.
# 
# This one is going to be tricky.  You are given a word problem telling with some math in it.  For instance, 
# > Panda has 8 apples and loses 2 apples.  How many apples?
# 
# The format will always be a number followed by a fruit, and may contain the words `gains` or `loses`.  The question will always end in a question about a fruit (which may or may not be mentioned in the question).  Here are a few examples:
# 
# > Panda has 2 apples, 3 bananas and 1 watermelon.  He gains 1 apple.  How many apples?
# 
# > Panda has 2 apples and gains 3 bananas.  How many watermelon?
# 
# > Panda has 2 apples and loses 2 apples but gains 4 bananas.  How many bananas?
# 
# **Hints**<br>
# Built-in string functions will be helpful.  Three in particular: `isdigits()`, `rtrim()`, `split()`

# In[ ]:


def fruit_calculator(question):
    '''
    Given a word problem, answer the question
    
    Parameters
    ----------
    question : str
        A question which has one or more sentences describing the situation and a question.
    
    Returns
    -------
    int
        A number which answers the question
    '''
    # Your code here
    pass

# Start with 3 apples
apples = fruit_calculator('Jim has 3 apples.  How many apples?')
print(apples)

# Now add 3 apples
apples = fruit_calculator('Jim has 3 apples and gains 2 apples.  How many apples?')
print(apples)

# Now drop a few
apples = fruit_calculator('Jim has 3 apples and loses 2 apples.  How many apples?')
print(apples)

# Add in another fruit
apples = fruit_calculator('Jim has 3 apples and loses 2 bananas.  How many apples?')
print(apples)


# In[ ]:


# Run this cell to test your work

assert_equal(fruit_calculator('Panda has 8 apples and loses 2 apples.  How many apples?'), 6)
assert_equal(fruit_calculator('Panda has 8 apples, 2 bananas and gains 3 bananas.  How many bananas?'), 5)
assert_equal(fruit_calculator('Panda has 8 apples, 2 bananas and gains 3 bananas.  How many apples?'), 8)    
assert_equal(fruit_calculator('Jim has 12 bananas. He loses 2 apples.  Then he gains 1 apple.  How many bananas?'), 12)
assert_equal(fruit_calculator('Jim has 2 bananas and gains 3 bananas.  How many watermelons?'), 0)


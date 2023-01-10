#!/usr/bin/env python
# coding: utf-8

# # Chapter 2
# 
# You should already have Anaconda Installed. Great. Now open a Jupyter Notebook, as we did at the end of chapter 1. In this chapter I'll show you some basic Python, and you can run it using your own Jupyter Notebook. Not everything here is intended to be practical for you in the future. Some of it will be, but mostly the purpose of this chapter is to familiarize yourself with Python 3.
# 
# It's necessary to discuss coding practices a bit. When writing code, it's useful to leave comments so that you and others can follow it! Comments are for human readers, and not code for the computer to execute. Below, are some comments and some actual code. If you hover your mouse over the right side of the box below, a *copy* button should appear; click it and copy the code, then paste it into your open Jupyter Notebook. (If you need to open a new cell, click the + icon near the top of the page, and make sure the cell is "code" (not "markdown", or "Raw NBConvert", or "Heading").

# In[1]:


#anything after the hashtag is a comment, not code.
#I'm setting up a variable called MyVariable
MyVariable = 1.0

#the statement below will show the output...
print("The value of MyVariable is " + (str(MyVariable)))


# This code doesn't do anything interesting. Notice the print statement at the end. This is necessary so we know that our "program" actually did something. In other Python development environments, the output of print statements may appear in different places, but print statements are still useful for developing and debugging. To make useful print statements, it's necessary to understand how variables work in Python 3. 

# ## Variables
# 
# *Variables* are things that can vary. There are different kinds of variables (and different systems for categorizing variables!). 
# 
# ### Assigning Values
# In Python, variables are assigned values using the equal sign ("="). Here are a few different kinds of variables.

# In[2]:


MyInt = 1 #an integer
MyFloat = 1.0 #a floating point number
MyString = "One" #a character string, so this is not numerical
MyBool = True #Bool, could also have been False

print(MyInt)
print(MyFloat)
print(MyString)
print(MyBool)


# ### Checking Type
# Notice that the variables are different types: an integer, or number with no decimal; a floating point number, which has a decimal; a string, which is characters; and a boolean variable. We can check the type of variable using the *type* function.

# In[3]:


MyInt = 1 #an int
MyFloat = 1.0 #a floating point number
MyString = "One" #a character string, so this is not numerical
MyBool = True #Bool, could also have been False

print(type(MyInt))
print(type(MyFloat))
print(type(MyString))
print(type(MyBool))


# It is very important to keep track of what type of variables you're working with, because different variable types do different things. We won't go into an exhaustive list of any such thing here, but an example will do. Take the operator for addition. When you add numbers (ints and floats), the result are different than if you add strings. See example below.

# In[4]:


MyNumber = 1.0
MyOtherNumber = 2.0
MyString = "1.0" #Notice that by putting the 1.0 in quotes, it becomes a string.
MyOtherString = "2.0"

print(MyNumber + MyOtherNumber)
print(MyString + MyOtherString)


# That's just an example. Since we will be focusing on data analysis, we'll focus on some basic mathematical operations here.  [Here](https://www.tutorialspoint.com/python/python_operators.htm) is a link to a more comprehensive list of operators in Python.
# 
# ### Updating and changing values
# Python executes lines of code in order, top to bottom. (Though, with some programming styles, it doesn't always seem that way).

# In[5]:


x1 = 1.0
x2 = x1
x1 += x1 #you can use plus-equal to add a variable to itself. Works with -= and *= too.
print(x1)#Can you figure out why these print statements have the output they do?
print(x2)


# In the example above, we assigned x2 the value of x1. Next we updated the value of x1, and printed the value of each variable. x1 was initially equal to 1, but we added it to itself so what printed was 2.0. x2 was never updated though; it was assigned the value of x1 when x1 was 1, so x2 equals 1. If you had some reason to make sure that x2 updated when x1 does, what could you do?

# ## Basic Arithmetic Operators
# 
# The section above snuck in some novel arithmetic operators. In this secion, let's look at a few more standard ones. The code block below is larger, but you can copy it and run it in your own notebook. It shows addition, subtraction, multiplication, exponentiation, and division for floating point numbers and integers.

# In[6]:


#the assignment operator is =, set up two floats and two ints
x = 1.0
y = 2.0

xi = 1
yi = 2

#store result of addition as new variable and then print
additionFloat = x + y
additionInteger = xi + yi
print("Addition results:")
print(additionFloat)
print(additionInteger)

#store result of subtraction as new variable and then print
print("\nSubtraction results:")
subtractionFloat = x - y
subtractionInteger = xi - yi
print(subtractionFloat)
print(subtractionInteger)

#store result of multiplication as new variable and then print
multFloat = x * y
multInteger = xi * yi
print("\nMultiplication results:")
print(multFloat)
print(multInteger)

#store result of exponents as new variable and then print
expFloat = y**2
expInteger = yi**2
print("\nExponentiation results:")
print(expFloat)
print(expInteger)

#store result of division as new variable and then print
divFloat = x / y
divInteger = xi / yi
print("\nDivision results:")
print(divFloat)
print(divInteger)


# With Python 3, the float/int distinction isn't as important as it used to be, but note that sometimes the difference has implcations for computation. Notice (with the division results) that with Python 3, integers are converted to floating point numbers when the result of integer division results in a floating point. Floating point numbers are usually safe, at least for most of what psychologists need.
# 
# ### Modulo: A cool operator you may not be familiar with
# Finally, a few more useful basic operators: the modulo operator (%). This will return the remainder of a division, so 5%4 will return 1, 6%4 returns two, 7%4 returns 3, and 8%4 returns 0. . This is actually very useful for making sure that things are checked cyclically, e.g. that a computer monitor updates every 10 frames.

# In[7]:


#The modulo operator returns the remainder of a division,
MyModulo = 5.0%4
print(MyModulo)


# ## Comparison operators
# 
# Sometimes you need to compare two values. Comparison operators do this, and return a boolean. Note also that the booleans had to be converted to strings in order for the print statments to work, so the comparison operators themselves are presented in a way that doesn't match how they are used. Typically, comparison operators are useful for controling the flow of a program using if/else, while, and other statements in Python. 

# In[8]:


x = 1.0
y = 2.0

#had to convert bool to str
equal = str(x==y) # check if two things are equal ==
notequal = str(x!=y)# check if two things not equal !=
greater = str(x>y)# greater than >
less = str(x<y)#less than <
greaterequal = str(x>=y)# greater or equal
lessequal = str(x<=y)#less or equal

print ("x == y: " + equal)
print ("x != y: " + notequal)
print ("x > y: " + greater)
print ("x < y: " + less)
print ("x >= y: " + greaterequal)
print ("x <= y: " + lessequal)


# Variables are incredibly important, and it will be worth your time to become familiar with variable types and how each works in Python. What has been presented here is a start, hopefully enough so you can follow the intructions at websites like Tutorials Point or the official Python documentation.

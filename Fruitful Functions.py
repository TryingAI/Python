
# coding: utf-8

# In[1]:


#Exercise 6.1. Write a compare function that returns 1 if x > y, 0 if x == y, and -1 if x < y.
def compare (x,y):
    if x>y:
        return 1
    if x<=y:
        return 0
    
a = int (input ("Enter a value for x \n"))
b= int(input("Enter a value for y \n"))
compare(a,b)

    


# In[2]:


#Exercise 6.2. Use incremental development to write a function called hypotenuse that returns the
#length of the hypotenuse of a right triangle given the lengths of the two legs as arguments. Record
#each stage of the development process as you go.

import math

def hypotenuse (a,b):
    c2 = a**2 + b**2
    print (" the squared value is ", c2)
    c = math.sqrt (c2)
    print ("The Length of the Hypotenuse is :")
    return c
x = int (input ("Enter a value for a length of the triangle: \n"))
y = int (input ("Enter a value for a length of the triangle: \n"))

hypotenuse (x,y)


# In[ ]:


def is_divisible (a,b):
    return a%b == 0

x = int (input ("Enter a value : \n"))
y = int (input ("Enter a value : \n"))
is_divisible(x,y)


# In[ ]:


#Exercise 6.3. Write a function is_between(x, y, z) that returns True if x  y  z or False otherwise
def is_between (x,y,z):
    if x<=y and y<=z:
        return True
    else:
        return False
        
a = int (input ("Enter a value : \n"))
b = int (input ("Enter a value : \n"))
c = int (input ("Enter a value : \n"))
is_between(a,b,c)


# In[10]:


#fibonacci
def fibonacci (n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)

x= int(input("Enter a number "))
fibonacci(x)
    
    


# In[13]:


# calculating factorial
def factorial(n):
    if n<0:
        return -1
    elif n<2:
        return 1
    else:
        return n*factorial(n-1)
x = int (input ("Enter a number to calculate the factorial of \n"))
factorial(x)


# In[16]:


#Exercise 6.7. A number, a, is a power of b if it is divisible by b and a/b is a power of b. Write a
#function called is_power that takes parameters a and b and returns True if a is a power of b. Note:
#you will have to think about the base case.


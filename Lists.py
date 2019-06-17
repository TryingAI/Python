
# coding: utf-8

# In[ ]:


# NOTE:   initially b is counting the index from the right side
cheeses = ["cheddar", "Edam", "Gouda", "taj"]
for b in cheeses:
    print (b)    


# In[ ]:


#* operator on a list
[1,2,3]*3


# In[ ]:


#List slicing
t = ['a','b','c','d','e','f']
print (t[1:3])
print (t[:4])

t[1:3]=['x','y']
print (t[:])
#list append
t.append('g')
print (t[:])
#list extend
t2 = ['...','w','v','u']
t.extend(t2)
print (t)


# In[ ]:


# list append, extend and sort
t= ['b','c','e','d','f','a']
print (t)
t.append ('g')
t.append ('h')
print (t)
t2 = ['j','k','i','l']
t.extend(t2)
print (t)
t.sort()
print (t)


# In[ ]:


#list sort function (low to high)
t = [6,4,8,2,0,99]
print (t)
t.sort ()
print (t)
t2 = [66,45,3,52,85]
t.extend(t2)
t.sort()
print (t)


# In[ ]:


t = ['a', 'b', 'c']
t2 = ['d','e','f']
t3 = [['g','h','i'], ['w','q','y']]
print (t)
#t.append(t2)
print (t)
t.extend (t2)
print (t)
t.extend (t3)
print (t)


# In[ ]:


#Exercise 10.1. Write a function called nested_sum that takes a nested list of integers and add up
#the elements from all of the nested lists.

def nested_sum(l4):
    result = 0 
    for item in l4:
        if type(item) == list:
            result += nested_sum(item)
        else:
            result += item 
    return result
      
l1 = [1,2]
l2= [3,4]
l3 = [[1, 2], [3, 4], 5, 6]
l4 = l1+l2+l3
print (len (l4))
print (l4)

nested_sum(l4)
#add_all(l4)


# In[ ]:



def nested_sum(l1):
    i = 0
    sum = 0
    for i in range(len(l1)):
        sum= sum + l1[i]
    return sum
        
l1 = [1,2,3]
l2 = [4,5,6]
l3 = l1+l2
print (len(l3))
print (l3)

nested_sum(l3)


# In[ ]:


def sim (ar):
    i=0
    s = 0
    for i in range (len (ar)):
        s = s +ar[i]
    return s
l1 = [1,2,3,4,5,6]
sim (l1)


# In[ ]:


t=[1,2,3]
sum(t)


# In[2]:


#Capitalising each letter
def capital (t):
    res = []
    for i in t:
        res.append(i.capitalize())
    return res
s = input ("enter a text to capitalize: \n")
capital(s)


# In[3]:


#Exercise 10.2. Use capitalize_all to write a function named capitalize_nested that takes
#a nested list of strings and returns a new nested list with all strings capitalized.

def cap_nested (t):
    print (t)
    result =0
    for i in t:
        #print (i)
        if type (i)== list:
            capital(i)
        print (capital(i))
        
        #return (capital(i))
        
s = ["this", "is", "survival",["of", "the"],"fittest"]

cap_nested(s)


# In[17]:


# only_upper returns the string IF it contains only upper case letters
def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res
    
s = ["THIS","IS","survival","OF", "The","FITTEST"]

only_upper(s)


# In[5]:


# Reverse sort letters and numbers
inpt = ['a','f','c','b']
inpt.sort(reverse =True)
print (inpt)
inpt =[1,4,7,3]
inpt.sort(reverse=True)
print (inpt)
    


# In[65]:


#Exercise 10.3. Write a function that takes a list of numbers and returns the cumulative sum; that
#is, a new list where the ith element is the sum of the first i + 1 elements from the original list. For
#example, the cumulative sum of [1, 2, 3] is [1, 3, 6].

def cum_sum(t):
    t1 = []
    total =0
    for i in t:
        print ("value of i ", i)
        total += i
        print ("value of total ", total)
        t1.append(total)
    print ("Cumulative sum is : ",t1)
        
        
x = [1,4,6]
print (x)
cum_sum(x)


# In[9]:


#pop modifies the list and returns the element that was removed.
x= ['2','a','b']
y = x.pop(1)
print (y)
print (x)
y=x.pop()
print (y)
print(x)


# In[28]:


#If you don’t need the removed value, you can use the del operator:
x = ['a', 'b', 'c']
del x[1]
print (x)

#If you know the element you want to remove (but not the index), you can use remove:

y = ['a','b','c','d']
y.remove ('c')
print (y)

#To remove more than one element, you can use del with a slice index:
w = ['a','b','c','d','e','f','g']
w.sort()
del w[-2:-1]
print (w)
del w[0:1]
print (w)


# In[33]:


"""Exercise 10.4. Write a function called middle that takes a list and returns a new list that contains
all but the first and last elements. So middle([1,2,3,4]) should return [2,3]."""

def middle(element):
    del element[-1]
    del element [0]
    element1 = element
    return element1

element0 = ['a','b','c','d','e','f','g']
middle (element0)
    
    


# In[37]:


"""Exercise 10.5. Write a function called chop that takes a list, modifies it by removing the first and
last elements, and returns None."""

def chop(L1):
    del L1[1:-1]
    print (L1)
    return ('None')

L = ['a','b','c','d','e','f','g']
chop (L)


# In[58]:


# LIST AND STRINGS
# To convert from a string to a list of characters, you can use list:

x = input ("Enter a string: \n")
y = list(x)
print (y)

# To break a string into words, use the split method:

w = x.split()
print (w)
print (w)

# NOT WORKING

s= 'spam-spam-spam'
delimiter = '-'
s.split (delimiter)
print (s)

#Join
# NOT WORKING

delimeter = ' '
delimeter.join(w)
print (w)


# In[6]:


# append modifies a list
# + creates a new list

t1 = [1,2]
t2 = t1.append(3)
print ("t1 = ",t1)
print ("t2 = ",t2)

t1.append(5)
t2=t1
print ("t1 = ",t1)
print ("t2 = ",t2)

t3 = t1 + [4]
print ("t1 = ", t1)
print ("t3 = ", t3)


# In[66]:


#10.15 Exercises


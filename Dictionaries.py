"""
Created on Tue Apr 28 2019

Python for Absolute Beginners

Coding Exercise:
Creating Dictionaries, Accessing by Key, Adding to Dictionaries, and
Length of a Dictionary:
1.create a 3 key: value pair dictionary and assign it to a variable
2.access and print a value from the list in step 1 by key
3.add a fourth key: value pair to the dictionary from step 1
4.print the dictionary from step 3
5.print the length of the dictionary from step 3

Solutions @author: SjGanguly (trying_ai)

"""
#1
fruit = {1:'apple',2:'orange',3:'pear'}
print('Original dictionary: fruit\n', fruit);

#2
print(fruit[3]);

#3
fruit[4] = 'grapes';

#4
print(fruit);

#5
print(len(fruit));


"""
Reassignment by Key and Del:
1.create a 2 key: value pair dictionary and assign it to a variable
2.print the dictionary from step 1
3.reassign a key from the dictionary in step 1 a different value than its original value
4.print the dictionary from step 3
5.remove a key: value pair from the dictionary from step 3 using del
6.print the new dictionary
"""

#1
name = {1:'sub', 2:'put'};

#2
print (name);

#3
name[2]= 'arhbus'

#4
print(name)

#5
del name[2]

#6
print (name)

input();




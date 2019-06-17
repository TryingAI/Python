"""
Created on Tue Apr 27 2019

Python for Absolute Beginners

Coding Exercise: For Loops and Tuples

1.create a 4 element tuple that consists of a float, an integer, a Boolean value,
and a string. Assingn this tuple to a variable
2.print the tuple from step 1
3.print the the second element from the tuple you made in step 1
4.print the first element from the tuple you made in step 1
5.slice and print the first 3 elements of the tuple from step 1
6.slice and print the last 3 elements of the tuple from step 1
7.slice and print the middle 2 elements of the tuple from step 1

Solutions @author: SjGanguly (trying_ai)

"""
#1
a = (1.5,55,True,'Tuple');

#2
print('Printing Tuple: ', a);

#3
print ('Printing 2nd element: ',a[1]);

#4
print ('Printing 1st element: ',a[0]);

#5
print ('Printing first 3 element: ',a[0:3]);

#6
print ('Printing the last 3 element: ',a[-4:-1]);

#7
print ('Printing middle 2 element: ', a[1:3]);

"""
For Loops:
1.create a variable and assign it the tuple ("Bohr", "Leibniz", "Einstein")
2.create a variable and assign it an empty list
3.create a variable and assign it the list [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
4.use a for loop to go through and print each of the elements from the tuple in step 1 individually
5.use a for loop, flow control statement(s), and .append() to add the middle 6 elements to the empty
list from step 2
6.print the new list
"""
#1
var1 = ("Bohr", "Leibniz", "Einstein");

#2
l1 = [];

#3
l2 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0];

#4
for i in var1:
    print(i);

#5
for j in l2:
    if j >1 and j<8:
      l1.append(j);
    
#6
print('the new list is: ',l1);

input();


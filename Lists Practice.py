"""
Created on Tue Apr 27 2019

Python for Absolute Beginners

Coding Exercise: 

Creating A List and Accessing by Index:
1.create a 4 element list that consists of values that are all strings and assign it to a variable
2.create a 3 element list that consists of values that are all numbers and assign it to a variable
3.create a 5 element list that contains at least 1 string, 1 number, and 1 Boolean value and assign it to a variable
4.Print the list you created in step 1
5.Access by index and print the second element of the list you made in step 2
6.Access by index and print a boolean value from the list you made in step 3

Solutions @author: SjGanguly (trying_ai)
"""

#1
l1 = ['cat','dog','elephant','tiger'];
print(l1);

#2
l2 = [5,6,7];
print(l2);

#3
l3 = ['rug',2,3.5,False,True];
print(l3);

#4
print('\nReprinting the first list : ', l1);

#5
print('printing 2nd element of the 2nd list :', + l2[1]);

#6
print('printing a boolean value from the 3rd list : ', + l3[-2]);


"""
Index Reassignment and .append():
1.create a variable and assign it the list [1, 2, 3]
2.print the list from step 1
3.reassign the first element in the list from step 1 the value 2
4.reassign the second element in the list from step 1 the value 3
5.reassign the third element in the list from step 1 the value 4
6.use .append() to add the value 6 to the end of the list from step 1
7.print the resulting list
"""

#1
v1 = [1,2,3];

#2
print('\n\n\n',v1);


#3
v1[0] = 2;

#4
v1[1]= 3;

#5
v1[2]= 4;

#6
v1.append(6);

#7
print(v1);

"""
List Slicing:
1.create a 7 element list and assign it to a variable
2.slice the list from its first element to its fourth element and print the resulting 4 element list
3.slice the list from its third element to its fifth element and print the resulting 3 element list
4.slice the list from its second element to its last element and print the resulting 6 element list
"""

#1
var = list('subhraj');
print ('\n\n\n printing the list', var);

#2
print('printing sliced list (0:4): ', var[0:4]);

#3
print('printing sliced list (3:5): ', var[2:6]);

#4
print('printing sliced list (2:): ', var[1:]);


"""
.index() and .insert()
1.create a variable and assign it the list ["Bob Dylan", "Like a", "Rolling Stone"]
2.use the .index() function to find and print the index of the string "Rolling Stone" from the list in step 1
3.use the .insert() function to insert the string 1965 at index 0 of the list from step 1
4.print the list that results from step 3
"""

#1
var1 = ["Bob Dylan", "Like a", "Rolling Stone"];

#2
print('\n\n\nindex for Rolling Stone in the list: ', var1.index('Rolling Stone'));

#3
var1.insert(0,1965);

#4
print('\nThe final resulting list is: ', var1);

"""
.remove() and .pop()
1.create a variable and assign it the list ["McCartney", "Lennon", "Starr", "Harrison", "Sutcliffe"]
2.use .remove() to remove of the "Sutcliffe" from the list created in step 1.
3.print the new list
4.use .pop() to remove and print "Lennon" from the list
5.use .pop() to remove and print "Harrison" from the list
6.print the new list
"""

#1
var1 = ["McCartney", "Lennon", "Starr", "Harrison", "Sutcliffe"];

print('\n\n\nPrinting the original list: \n', var1);
#2
var1.remove('Sutcliffe');

#3
print('Printing new list\n', var1);

#4
print(var1.pop(1));

#5
print(var1.pop(-2));

#6
print('\n\n Printing the final list', var1);

input();



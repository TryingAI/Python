"""
Created on Tue Apr 26 2019

Python for Absolute Beginners

Coding Exercise: 

and, or, and not:
1.create a variable and set it equal to True using a statement containing an "and" Boolean operator
2.create a variable and set it equal to False using a statement containing an "and" Boolean operator
3.create a variable and set it equal to True using a statement containing an "or" Boolean operator
4.create a variable and set it equal to False using a statement containing an "or" Boolean operator
5.create a variable and set it equal to True using a statement containing an "not" Boolean operator
6.create a variable and set it equal to False using a statement containing an "not" Boolean operator

Solutions @author: SjGanguly (trying_ai)
"""
var1 = 1+2 and 3<=3
print(var1);

var2 = 2**3 and False;
print(var2);

var3 = (2**3 == 8) or 8<7;
print(var3);

var4 =  False or False;
print(var4);

var5 = not 5 != 5
print(var5);

var6 = not((5-6)*100) >= -100;
print(var6);
input();

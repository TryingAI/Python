"""
Created on Tue Apr 26 2019

Python for Absolute Beginners

Coding Exercise: 
Single parameter and zero parameter functions:
1.define a function that takes no parameters and prints a string
2.create a variable and assign it the value 5
3.create a function that takes a single parameter and prints it
4.call the function you created in step 1
5.call the function you created in step 3 with the variable you made in step 2 as its input

Solutions @author: SjGanguly (trying_ai)
"""
# 1 and # 4

def func1():
    print('Function with no arguments printing a string');

#2
var1 =5 ;

#3
def prnt(x):
    print (' the value is', x);

#4
func1();

#5
prnt(var1);


"""
Coding Exercise:

multiple parameter functions:
1.create 3 variables and assign integer values to them
2.define a function that prints the difference of 2 parameters
3.define a function that prints the product of the 3 variables
4.call the function you made in step 2 using 2 of the variables you made for step 1
5.call the function you made in step 3 using the 3 variables you created for step 1

"""
#1
var1 = 5; var2 = 10; var3= 20;

#2
def diff(x,y):
    z = x-y;
    print(z);
#3
def prod(x,y,z):
    p = x*y*z;
    return p;

#4
diff(var1, var2);

#5
print(prod(var1,var2,var3));

"""
Coding Exercise:
Calling previously defined functions within functions:
1.create 3 variables and assign float values to them
2.create a function that returns the quotient of 2 parameters
3.create a function that returns the quotient of what is returned by the function from the second step and a
third
parameter
4.call the function you made in step 2 using 2 of the variables you created in step 1. Assign this to a
variable.
5.print the variable you made in step 4
6.print a call of the function you made in step 3 using the 2 variables you created in step 1

"""
#1
var1 = 1.5; var2 = 3.99; var3 = 5.78;

#2
def quo(x,y):
    z = x/y;
    return(z);

#3
def quo2(x1,y1):
    z1 = x1/y1;
    return (z1);

#4
quotient1 = quo(var3,var1);

#5
print(quotient1);

#6
print (quo2(quotient1, var2));
    
input();    


















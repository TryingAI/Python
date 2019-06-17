"""
Created on Tue Apr 30 2019

Coding Exercise: Python provides a built-in function called len that returns the length of a string, so the value of len('allen') is 5.
Write a function named right_justify that takes a string named s as a parameter and prints the
string with enough leading spaces so that the last letter of the string is in column 70 of the display.

Solutions @author: SjGanguly (trying_ai)
"""
def right_justify(s):
    print(" " * (70 - len(s))+s)

n = input ("Enter a string to check the length and right justify: ")
print ("lenght is ", len(n))
right_justify(n)


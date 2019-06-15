"""
Created on Tue May 02 2019

Python from Beginner to Intermediate
Coding Exercise: 1. A Caesar Cipher (or Cipher Wheel) encrypts a message by shifting each alphabetic character
                 in the text by a fixed amount. For example, a Caesar cipher with a shift of 4 translates a to e, b to f etc.

            abcdefghijklmnopqrstuvwxyz
            efghijklmnopqrstuvwxyzabcd  

            and would encrypt helloworld as lippsasvph.

Write a program in python that would, covert a string into Caesar cipher. 

Solution: @author: SjGanguly (trying_ai)
"""

#################### ENCRYPTION ####################################
# Getting user input to encrypt
inp = list(input('Enter a string to encrypt using Caesar Cipher: '));
i =0;

#Reference for encryption
alphabets = tuple('abcdefghijklmnopqrstuvwxyz');

print('encrypted text: \n');

for i in range(len(inp)): 
    j=0;
    try:
        while inp[i] != alphabets[j]:
            j+=1;
        else:
            inp[i] = alphabets[j+4];
    except:
        if inp[i] =='w':
            inp[i]='a';
    
        if inp[i]=='x':
            inp[i]='b';
        if inp[i]=='y':
            inp[i]='c';
        if inp[i]=='z':
            inp[i]='d';
        if inp[i]==' ':
            inp[i]=' ';
    

    print(inp[i],end="");  

###################### DECRYPTION ##################################
print('\n\nDecrypted text: \n');

for i in range(len(inp)): 
    j=0;
    try:
        while inp[i] != alphabets[j]:
            j+=1;
        else:
            inp[i] = alphabets[j-4];
    except:
        if inp[i]=='a':
            inp[i]='w';
    
        if inp[i]=='b':
            inp[i]='x';
        if inp[i]=='c':
            inp[i]='y';
        if inp[i]=='d':
            inp[i]='z';
        if inp[i]==' ':
            inp[i]=' ';
    

    print(inp[i],end="");  


input();
            
    
        
        

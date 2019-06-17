"""

Created on Tue Apr 24 2019

Python for Absolute Beginners
Coding Exercise: 

1.Your program should take an integer as an input from the user (either a 1, 2, or 3) that corresponds with an option
for a drink from the vending machine outlined below and assign the corresponding price to a variable as a float.
Use your knowledge of if, elif, and else statements to complete this part of the problem. Your code should
have an else statement that prints a message and ends the program using sys.exit() if the user does not enter a valid
input number.
Vending Machine:
1.water = $1.00
2.cola = $1.50
3.gatorade = $2.00

Solutions @author: SjGanguly (trying_ai)

"""
print(' Vending Machine:\n 1.water = $1.00 \n 2.cola = $1.50\n 3.gatorade = $2.00')
inp1 = int(input('Please select an option. Enter 1 or 2 or 3: '));
if inp1 == 1:
    water = 1.00;
    print(water);
elif inp1 == 2:
    cola = 1.50;
    print(cola)
elif inp1 == 3:
    gatorade = 2.00;
    print(gatorade);
else:
    print ('not a valid option');
input();
    



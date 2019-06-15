"""
Hackerrank List Comprehension Problem
Created on 30/05/2019
@author: SjGanguly (trying_ai)

Let's learn about list comprehensions! You are given three integers X,Y and Z representing the dimensions of a cuboid along with an integer N.
You have to print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k is not equal to N .

Sample Input 
1
1
1
2

Sample Output
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
"""
if __name__ == '__main__':
    x = int(input('x: '))
    y = int(input('y: '))
    z = int(input('z: '))
    n = int(input('n: '))
 
output = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k) !=n]
print(output)
input()


          

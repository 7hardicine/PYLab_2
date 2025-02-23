import math as m

a = int(input('Input the value of a: '))
b = int(input('Input the value of b: '))
while (b < a):
    b = int(input('The value of b cant be less than a, input b again: '))
N = int(input('Input the value of N: ')) 
while (N < 10):
    N = int(input('The value of N must be over than 9, input N again: '))  

dx = (b - a) / N
print('The value of step dx will be ', dx)

flag = 0
temp = 0
while b > a:
    y = 1 - m.cos(2 * a) - m.log(a)
    if temp * y < 0:
        flag += 1
    temp = y
    print('y = ', y)
    a += dx

print('Y changed sign ', flag, ' times')
import math as m

a = float(input('Введите значение a: '))
b = float(input('Введите значение b: '))
while (b < a):
    b = int(input('Значение b не может быть меньше значения a, повторите ввод: '))
N = int(input('Введите значение N: ')) 
while (N < 10):
    N = int(input('Значение N не может быть меньше 10, повторите ввод: '))  

dx = (b - a) / N
print('Значение шага dx равно: ', dx)

flag = 0
temp = 0
while b + dx > a:
    y = 1 - m.cos(2 * a) - m.log(a)
    if temp * y < 0:
        flag += 1
    temp = y
    print('y = ', y, ' x = ', a)
    a += dx

print('Y поменял знак ', flag, ' раз(а)')

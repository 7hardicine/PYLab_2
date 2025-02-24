
IsInput = 1
U_summ = 0
amount = 0
U_average = 1
MoreThan60 = 0

while (IsInput):
    U = int(input('Введите скорость автомобиля: '))
    U_summ += U
    if U == 0:
        IsInput = 0
    else:
        amount += 1
        if U >= 60:
            MoreThan60 += 1

if amount == 0:
    print('Камера неисправна')
else:
    U_average = U_summ / amount
    print('Средняя скорость автомобилей равна ', U_average)
    if MoreThan60 >= 3:
        print('Есть автомобили со скоростью не меньше 60')
    else:
        print('Нет автомобилей со скоростью не меньше 60')
    

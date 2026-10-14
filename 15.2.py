year = int(input('Введите год: '))

if year % 100 == 0:
    if year % 400 == 0:
        print('Високосный')
    else:
        print('Не високосный')
elif year % 4 == 0:
    print('Високосный')
else:
    print('Не високосный')
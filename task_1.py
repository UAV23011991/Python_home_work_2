# Напишите программу, которая принимает на вход вещественное
# число и показывает сумму его цифр.

# Пример:
# - 6782 -> 23
# 0,56 -> 11

x = input('Введите число: ')
def sum(x):                             
    if float(x) < 0:                            
        x = float(x) * (-1)
    num = 0

    for i in str(x):
        if i != '.':
            num += int(i)
    return num
print(f'Сумма чисел равна {sum(x)}')
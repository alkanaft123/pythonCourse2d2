# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

n = input('enter N')
if n.isdigit():
    n = int(n)
    number = 1
    summ = 0
    while n > 0:
        summ = summ + number
        n-=1
        number/=-2
    print(summ)
else:
    print('error type N')


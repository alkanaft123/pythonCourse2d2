# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

a = input('enter number')
t2 = 0
tx = 0
if a.isdigit():
    for symb in a:
        if int(symb) % 2 == 0:
            t2+=1
        else:
            tx+=1
    print('even',t2,'odd',tx)
else:
    print('error type number')




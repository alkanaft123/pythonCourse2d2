# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

import timeit

n = int(input('enter N'))
a = input('enter symbol')

count = 0
while n>0:
    my_num = input('enter number')
    for j in my_num:
        if j == a:
            count+=1
    n-=1
print(count)


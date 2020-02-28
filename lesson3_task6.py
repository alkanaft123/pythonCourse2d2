# В одномерном массиве найти сумму элементов,
# находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random


my_list = [random.randint(0, 100) for _ in range(10)]
print('list:', my_list)

max = float('-inf')
max_ind = float('-inf')
min = float('inf')
min_ind = float('inf')

for i, el in enumerate(my_list):
    if el > max:
        max = el
        max_ind = i
    if el < min:
        min = el
        min_ind = i
print('min:', min, ', min index:', min_ind, ', max:', max, ', max index:', max_ind)

my_sum = 0


ind1 = min_ind + 1 if min_ind < max_ind else max_ind + 1
ind2 = max_ind if max_ind > min_ind else min_ind

for el in my_list[ind1: ind2]:
    my_sum+=el
print('sum = ', my_sum)
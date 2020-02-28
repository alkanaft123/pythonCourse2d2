# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random


my_list = [random.randint(0, 100) for _ in range(10)]


print(my_list)

my_max = float('-inf')
max_ind = float('-inf')
my_min = float('inf')
min_ind = float('inf')
for i, el in enumerate(my_list):
    if el > my_max:
        my_max = el
        max_ind = i
    if el < my_min:
        my_min = el
        min_ind = i


my_list[min_ind], my_list[max_ind] = my_list[max_ind], my_list[min_ind]
print(my_list)

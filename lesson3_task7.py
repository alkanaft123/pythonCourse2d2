# В одномерном массиве целых чисел
# определить два наименьших элемента. Они могут быть
# как равны между собой (оба являться минимальными),
# так и различаться.

import random


my_list = [random.randint(0, 100) for _ in range(10)]
print(my_list)



min = float('inf')
min2 = float('inf')

for el in my_list:
    if el < min:
        if min < min2:
            min2 = min
        min = el
    elif el < min2:
        min2 = el
print(min, min2)
# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве. Примечание
# к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.

import random


my_list = [random.randint(-100, 100) for _ in range(10)]

my_max = float('-inf')
max_ind = float('-inf')

for i,el in enumerate(my_list):
    if el < 0:
        if el > my_max:
            my_max = el
            max_ind = i

print(my_list)
print('el: ', my_max, ' index: ', max_ind)


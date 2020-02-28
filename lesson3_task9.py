# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

matrix = []
for i in range(0, 5):
    row = []
    for j in range(0, 5):
        row.append(random.randint(0, 10))
    matrix.append(row)

print('original matrix:')
for row in matrix:
    print(row)

list_min = []
for col in list(zip(*matrix)):
    min = float('inf')
    for el in col:
        if el < min:
            min = el
    list_min.append(min)
print('list of minimums: ', list_min)

max = float('-inf')
for el in list_min:
    if el > max:
        max = el

print('max el:', max)
# 2). Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random
my_lst = []
for _ in range(10):
    num = random.uniform(0, 50)
    if num != 50:
        my_lst.append(num)
print(my_lst)

def mergesort(m):
    left = []
    right = []
    result = []
    if len(m) <= 1:
        return m
    else:
        middle = len(m) / 2
        for i,x in enumerate(m):
            if i < middle:
                left.append(x)
            if i >= middle:
                right.append(x)
        left = mergesort(left)
        right = mergesort(right)
        result = merge(left, right)
        return result

def merge(left,right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while len(left) > 0:
        result.append(left.pop(0))
    while len(right) > 0:
        result.append(right.pop(0))
    return result

print(mergesort(my_lst))


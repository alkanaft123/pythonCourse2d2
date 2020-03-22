#3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
#Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
#в другой – не больше медианы. Задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
#то используйте метод сортировки, который не рассматривался на уроках

import random
m = 5
lst = [random.randint(-10,10) for _ in range(m*2 + 1)]
print('original array: ', sorted(lst))
print('control middle lane: ', sorted(lst)[m])
i = 0
while i <= len(lst)-1:
    counter_less = 0
    counter = 0
    j = 0
    while j <= len(lst)-1:
        if i != j:
            if lst[j] < lst[i]:
                counter_less+=1
            elif lst[j] == lst[i]:
                counter+=1
        else:
            counter+=1
        j+=1
    if (counter_less + counter) > m and counter_less <= m:
        print('middle lane: ', lst[i])
        break
    i+=1

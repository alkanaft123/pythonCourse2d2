import sys
import random

print(sys.platform)

my_list = [random.randint(-1000, 1000) for _ in range(10)]

def showall(arr, my_sum=0):
    for el in arr:
        my_sum+=show(el)
    return my_sum

def show(obj, my_sum=0):
    my_sum+=sys.getsizeof(obj)
    # print(f'type={type(obj)}, size={sys.getsizeof(obj)}, {obj}')

    if hasattr(obj, '__iter__'):
        if hasattr(obj, 'items'):
            for key, value in obj.items():
                my_sum+=show(key)
                my_sum+=show(value)
        elif not isinstance(obj, str):
            for item in obj:
                my_sum+=show(item)
    return my_sum

# всплывающий пузырек
def test1(my_list):
    my_max = float('-inf')

    for i,el in enumerate(my_list):
        if el < 0:
            if el > my_max:
                my_max = el
    lst = [my_max, i, el, my_list]
    print(f'memory: {showall(lst)}')
    return my_max

# отдельный список и встроенная функция
def test2(my_list):
    my_list2 = []

    for el in my_list:
        if el < 0:
            my_list2.append(el)
    lst = [el, my_list, my_list2]
    print(f'memory: {showall(lst)}')
    return max(my_list2)

# встроенная сортировка и первый меньше нуля
def test3(my_list):
    my_list = sorted(my_list)

    for i,el in enumerate(my_list):
        s = sys._getframe()
        if el >= 0:
            lst = [i, el, my_list]
            print(f'memory: {showall(lst)}')
            return my_list[i-1]


test1(my_list)
test2(my_list)
test3(my_list)
# Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
# Примечание. Идеальным решением будет:

# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве. Примечание
# к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.

import random
import timeit
import cProfile

# всплывающий пузырек
def test1(my_list):
    my_max = float('-inf')

    for i,el in enumerate(my_list):
        if el < 0:
            if el > my_max:
                my_max = el
    return my_max

# отдельный список и встроенная функция
def test2(my_list):
    my_list2 = []

    for el in my_list:
        if el < 0:
            my_list2.append(el)

    return max(my_list2)

# встроенная сортировка и первый меньше нуля
def test3(my_list):
    my_list = sorted(my_list)

    for i,el in enumerate(my_list):
        if el >= 0:
            return my_list[i-1]



my_list = [random.randint(-1000, 1000) for _ in range(1000000)]
print(test1(my_list))
print(test2(my_list))
print(test3(my_list))

print(timeit.timeit('test1(my_list)', number=100, globals = globals())) # 0.649002272
print(timeit.timeit('test2(my_list)', number=100, globals = globals())) # 0.6283566620000001
print(timeit.timeit('test3(my_list)', number=100, globals = globals())) # 1.913870228

# первые два решения примерно одинаковы по времени

cProfile.run('test1(my_list)')
# 1    0.000    0.000    0.006    0.006 <string>:1(<module>)
# 1    0.006    0.006    0.006    0.006 lesson4_task1.py:9(test1)
# 1    0.000    0.000    0.006    0.006 {built-in method builtins.exec}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('test2(my_list)')
#     1    0.000    0.000    0.012    0.012 <string>:1(<module>)
#     1    0.008    0.008    0.012    0.012 lesson4_task1.py:18(test2)
#     1    0.000    0.000    0.012    0.012 {built-in method builtins.exec}
#     1    0.001    0.001    0.001    0.001 {built-in method builtins.max}
# 49841    0.003    0.000    0.003    0.000 {method 'append' of 'list' objects}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('test3(my_list)')
# 1    0.000    0.000    0.022    0.022 <string>:1(<module>)
# 1    0.003    0.003    0.021    0.021 lesson4_task1.py:27(test3)
# 1    0.000    0.000    0.022    0.022 {built-in method builtins.exec}
# 1    0.018    0.018    0.018    0.018 {built-in method builtins.sorted}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# все 3 алгоритма имеют асимптотику O(n)
# первый алогоритм работает быстрее всех, его преимущество в том что поиск максимального
# элемента выполняется методом всплывающего пузырька и значение мы ищем сразу налету в процессе
# обхода попутно проверяя элементы на отрицательность

# второй алогоритм работаешь чуть медленнее так как тут тратится процессорное время на вызовы append и также оператива для хранения списка

# третий самый медленный - самый долгий вызов это первоначальная сортировка (к сожалению не знаю как выполняется сортировка)
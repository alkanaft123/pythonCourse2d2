# Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна
# принимать на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов


import timeit
import cProfile

# my
def test1(n):
    my_lst = []
    k = 0
    i = 2
    while True:
        for j in range(2, i):
            if i % j == 0:
                k = k + 1
        if k == 0:
            my_lst.append(i)
        else:
            k = 0
        if len(my_lst) == n:
            return(my_lst[n-1])
        i+=1


print(test1(100))
print(timeit.timeit('test1(5)', number=100, globals = globals()))      # 0.0006400660000000016
print(timeit.timeit('test1(50)', number=100, globals = globals()))     # 0.148620954

cProfile.run('test1(100)')
# 1    0.000    0.000    0.007    0.007 <string>:1(<module>)
#         1    0.007    0.007    0.007    0.007 lesson4_task2.py:9(test1)
#         1    0.000    0.000    0.007    0.007 {built-in method builtins.exec}
#       540    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       100    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# eratosphen
def test2(n):
    sieve = list(range(n*n + 1))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    i = 0
    while i < len(sieve):
        if sieve[i] == 0:
            sieve.remove(sieve[i])
        else:
            i+=1

    return sieve[n-1]

print(test2(100))
print(timeit.timeit('test2(5)', number=100, globals = globals()))      # 0.0011188089999999984
print(timeit.timeit('test2(50)', number=100, globals = globals()))     # 0.656483672

cProfile.run('test2(100)')
# 1    0.000    0.000    0.078    0.078 <string>:1(<module>)
#         1    0.006    0.006    0.077    0.077 lesson4_task2.py:39(test2)
#         1    0.000    0.000    0.078    0.078 {built-in method builtins.exec}
#     11231    0.001    0.000    0.001    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      8772    0.071    0.000    0.071    0.000 {method 'remove' of 'list' objects}

# мой алгоритм работает гораздо хуже, также у решета есть один недостаток, в своей основе он содержит изъян
# который делает решето не очень подходящим для выолнения данной задачи, так как для алгоритма решета необходимо само решето
# то есть оно ищет простые числа в списке до N, а в задаче требуется найти N-е по счету число, можно конечно при недостижении
# N-го элемента достраивать решето, но в таком случае мне кажется его асимптотика может даже ухудшиться, так как придется для
# всех вновь добавленных элементов заново проверять их делители
# определить асимптотику обоих пока у меня не хватает мозгов
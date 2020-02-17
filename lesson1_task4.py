import random

# task 4

# Написать программу, которая генерирует в указанных пользователем границах:
# ● случайное целое число, ● случайное вещественное число, ● случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

a = int(input('input a: '))
b = int(input('input b: '))
print(random.randint(a, b))

a = int(input('input a: '))
b = int(input('input b: '))
print(random.uniform(a, b))

a = input('input a: ')
b = input('input b: ')
a.encode('windows-1251')
b.encode('windows-1251')
print(chr(random.randint(ord(a), ord(b))))
## 7. Напишите программу, доказывающую или проверяющую, что для множества
# натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n — любое натуральное число.

def calculate(my_sum, i, n):
    if i == n:
        return my_sum + i
    else:
        return calculate(my_sum + i, i + 1, n)

n = input('enter N')
if n.isdigit():
    n = int(n)
    my_sum = calculate(0, 1, n)
    my_sum2 = n * (n + 1) / 2
    if my_sum == my_sum2:
        print(my_sum, my_sum2, True)
    else:
        print(my_sum, my_sum2, False)


# 9. Среди натуральных чисел, которые были введены, найти наибольшее
# по сумме цифр. Вывести на экран это число и сумму его цифр.

max_sum = float('-inf')
max_num = float('-inf')
while True:
    n = input('enter number')
    if n.isdigit():
        sum = 0
        for i in n:
            sum = sum + int(i)

        if sum > max_sum:
            max_sum = sum
            max_num = int(n)
    else:
        break
print('number', max_num, 'summ', max_sum)
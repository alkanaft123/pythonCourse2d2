# 6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться, больше или меньше
# введенное пользователем число, чем то, что загадано. Если за
# 10 попыток число не отгадано, вывести ответ.

import random

n = random.randint(0, 100)
try_count = 10
resault = False
while try_count > 0:
    a = input('Guess number')
    if a.isdigit():
        a = int(a)
        if a == n:
            resault = True
            break
        elif n > a:
            print('More')
        else:
            print('Less')
    else:
        print('error type a')
    try_count-=1

if resault:
    print('win', '( count of tries', 10 - try_count + 1, ')')
else:
    print('lose')


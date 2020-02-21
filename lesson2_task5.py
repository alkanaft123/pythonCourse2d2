# 5. Вывести на экран коды и символы таблицы ASCII, начиная с
# символа под номером 32 и заканчивая 127-м включительно. Вывод выполнить
# в табличной форме: по десять пар "код-символ" в каждой строке.

count = 1
for i in range(96):
    mystr = str(i + 32)
    if count < 10:
        print('{:<5}'.format(mystr), '{:<5}'.format(chr(i + 32)), end='')
        count += 1
    else:
        print('{:<5}'.format(mystr), '{:<5}'.format(chr(i + 32)))
        count = 1

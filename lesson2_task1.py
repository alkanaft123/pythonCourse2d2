# Написать программу, которая будет складывать, вычитать,
# умножать или делить два числа. Числа и знак операции вводятся
# пользователем. После выполнения вычисления программа не завершается,
# а запрашивает новые данные для вычислений. Завершение программы должно
# выполняться при вводе символа '0' в качестве знака операции. Если
# пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
# программа должна сообщать об ошибке и снова запрашивать знак операции.
# Также она должна сообщать пользователю о невозможности деления на
# ноль, если он ввел его в качестве делителя.


while True:
    a = input('Enter A')
    a = int(a)

    b = input('Enter B')
    b = int(b)

    c = input('Enter operation')

    if c == '+':
        print(a + b)
    elif c == '-':
        print(a - b)
    elif c == '*':
        print(a * b)
    elif c == '/':
        if b == 0:
            print('error, b=0')
        else:
            print(a / b)
    elif c == '0':
        break
    else:
        print('error input')

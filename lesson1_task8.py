# task 8

# Определить, является ли год, который ввел пользователь, високосным или не високосным.

a = 2021
if (a % 400) == 0:
    print(True)
else:
    if (a%100) == 0:
        print(False)
    else:
        if (a%4) == 0:
            print(True)
        else:
            print(False)

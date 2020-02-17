# task 9

# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a = 1
b = 5
c = 3
if a != b and b != c and a != c:
    if b < a < c:
        print(a)
    elif a < b < c:
        print(b)
    else:
        print(c)
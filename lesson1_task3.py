# task 3

# По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки.

x1 = int(input('enter x1'))
y1 = int(input('enter y1'))
x2 = int(input('enter x2'))
y2 = int(input('enter y2'))

if x1 == x2:
    print(" x = ", x1)
elif y1 == y2:
    print(" y = ", y1)
else:
    k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2
    print(" y = %.2f*x + %.2f" % (k, b))

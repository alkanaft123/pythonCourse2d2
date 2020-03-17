from collections import namedtuple



db = []
n = int(input("Enter count of companies: "))

for i in range(n):
    comp = namedtuple('Company', 'name q0 q1 q2 q3 avrg')
    comp.name = input('Enter name of company: ')
    comp.q0 = int(input('q0: '))
    comp.q1 = int(input('q1: '))
    comp.q2 = int(input('q2: '))
    comp.q3 = int(input('q3: '))
    comp.avrg = (comp.q0 + comp.q1 + comp.q2 + comp.q3) / 4
    db.append(comp)


# main algorithm
avrg = 0
for el in db:
    avrg = avrg + el.q0 + el.q1 + el.q2 + el.q3
avrg = avrg / n / 4
print('Average sales:', avrg)

print('Companies with avrg sales MORE then common avrg sales')
for el in db:
    if el.avrg > avrg:
        print(el.name, el.avrg)

print('Companies with avrg sales LESS then common avrg sales')
for el in db:
    if el.avrg < avrg:
        print(el.name, el.avrg)
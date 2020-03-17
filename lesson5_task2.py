import collections

x = collections.deque('FA')
y = collections.deque('AC')

print(x, y)

my_sys = ('0', '1', '2', '3',
         '4', '5', '6',
         '7', '8', '9',
         'A', 'B', 'C',
         'D', 'E', 'F'
          )

def my_summ(x, y):
    if len(x) < len(y):
        x.extendleft('0' * (len(y) - len(x)))
    else:
        y.extendleft('0' * (len(x) - len(y)))

    buffer = 0
    final_summ = []
    for i in range(len(x) -1, -1, -1):
        sum_el = my_sys.index(x[i]) + my_sys.index(y[i]) + buffer
        buffer = 0
        if sum_el > 15:
            buffer = 1
            final_summ.insert(0, my_sys[sum_el - 16])
        else:
            buffer = 0
            final_summ.insert(0, my_sys[sum_el])
    if buffer > 0:
        final_summ.insert(0, '1')
    # print(final_summ)
    return collections.deque(final_summ)

def my_mull(x, y):
    if len(x) < len(y):
        x.extendleft('0' * (len(y) - len(x)))
    else:
        y.extendleft('0' * (len(x) - len(y)))

    final_mul = collections.deque('0')
    for el in y:
        for _ in range(int(my_sys.index(el))):
            final_mul = my_summ(final_mul, x)
        final_mul.extend('0')
    final_mul.pop()
    return final_mul


print('SUM =', my_summ(x, y))

print('MUL =', my_mull(x, y))
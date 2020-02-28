# Матрица 5x4 заполняется вводом с клавиатуры,
# кроме последних элементов строк. Программа должна вычислять сумму введенных
# элементов каждой строки и записывать ее в последнюю
# ячейку строки. В конце следует вывести полученную матрицу.

matrix = []
for i in range(0, 5):
    row = []
    for j in range(0, 4):
        row.append(int(input('enter n')))
    matrix.append(row)

print('original matrix:')
for row in matrix:
    print(row)

for row in matrix:
    my_sum = 0
    for el in row:
        my_sum+=el
    row.append(my_sum)

print('modificated matrix:')
for row in matrix:
    print(row)
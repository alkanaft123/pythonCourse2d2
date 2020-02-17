# task 1

# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

s = int(input('Enter number'))
output__sum = 0
output__mul = 1
s1 = s
output__sum = output__sum + s1 % 10
s1 = s1 // 10
output__sum = output__sum + s1 % 10
s1 = s1 // 10
output__sum = output__sum + s1
print('sum=', output__sum)

output__mul = output__mul * s % 10
s = s // 10
output__mul = output__mul * s % 10
s = s // 10
output__mul = output__mul * s
print('mul=', output__mul)
# task 6

# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

a = int(input('input a'))
print(chr(a + ord('a') - 1))
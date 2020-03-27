# # 1. Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N, состоящая
# # только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.
#
import random
import hashlib

def my_subs(my_str):
    lst_hash = []
    i=1
    while i < len(my_str):
        j=0
        while j < len(my_str):
            an_str = my_str[j:j+i]
            my_hash = hashlib.sha1(an_str.encode('utf-8')).hexdigest()
            if not my_hash in lst_hash:
                print(an_str)
                lst_hash.append(my_hash)
            j+=1
        i+=1
    return(len(lst_hash))

my_str = "".join([chr(random.randint(97,122)) for _ in range(20)])
# my_str = 'abcd'
print(my_str)
print(my_subs(my_str))
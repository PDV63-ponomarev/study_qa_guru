from decimal import Decimal 
# библиотека для более точного подсчета

# числа
a = 112
a = a + 234
a = a - 200
a = a ** 3  # степень
a = a * 10
a = a / 2

a = 0b0110101 # двоичное
a = 0o01234567 # восмиричное
a = 0x0123456789abcdef #шестнадцаритичное

a = 0.4
print(a)

a = 0.1 + 0.2
print(a) # 0.30000000000000004


print('~' * 10)


import math

print(math.pi)


print('~' * 10)


import random

random.seed('some word') #фиксирует рандомные числа

n = random.randint(0,10)
print(n)
n = random.randint(0,10)
print(n)
n = random.randint(0,10)
print(n)


print('~' * 10)


# округление
print(round(math.pi, 2))
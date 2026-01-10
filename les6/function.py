from operator import itemgetter
from pprint import pprint


# обьявление функции

# def my_func():
#     print('Функция')
#
# my_func()
#
# def sum_num(a: int, b: int): # предупреждает что нужны числа
#     print(a + b)
#
# sum_num(1, 4)
# sum_num(10, 20)
# sum_num('abd', 'text')


# Возврашение значений
# def sum_num(a: int, b: int):
#     return a + b

# n = sum_num(3, 4)
# print(n)

# именованые аргументы
# m = sum_num(b=4, a=5)
# print(m)

# аргументы по умолчанию
# def multiply_num(n, mult: int = 2):
#     print(n * mult)

# multiply_num(10)
# multiply_num(2, mult = 3)
# multiply_num(4,5)

# print(1,2,3,4,5, sep=' | ')


# Возврат нескольких значений
def return_tuple():
    return 1, 2, 3

# t1, t2, t3 = return_tuple()
# print(t1, t2, t3)
# t = return_tuple()
# print(t)

#ValueError: too many values to unpack (expected 2)
# t1, t2 = return_tuple()
# print(t1, t2)

# t1, *t2 = return_tuple()
# print(t1, t2)
#
# t1, t2, *t3 = return_tuple()
# print(t1, t2, t3)

# t1, _, _ = return_tuple() #Заглушки
# print(t1)
# t1, *_ = return_tuple() #Заглушки
# print(t1)

# переменное количество аргументов на примере print
# def custom_print(*args):
#     for arg in args:
#         print(arg)
#
#     print(args)
#     print(*args)
#
# custom_print(1,2,3,4,5)


# переменное кол-во именованных арг
# def custom_named_print(*args, **kwargs):
#     print(args, kwargs)
#     print(*args, **kwargs)
#
# custom_named_print(1,2,3,4,5, end = '!\n', sep = ' | ')


# область видимости переменных

# v = 123
# def func():
#     v = 456
#     print(v)
#
# print(v)
# func()
# print(v)



# функции тоже обьект

# p = print
# p(1,2,3)


users = [
    {'name': 'John', 'age': 32},
    {'name': 'Michael', 'age': 26},
    {'name': 'Sarah', 'age': 17},
    {'name': 'Bob', 'age': 22},
]

def get_age(user):
    # print(user)
    return user['age']

users.sort(key=get_age)
pprint(users)

print('~~~~~~~~~~~~~~~~')

users.sort(key=get_age,reverse=True)
pprint(users)

print('~~~~~~~~~~~~~~~~')

users.sort(key = lambda user: user['age'])
pprint(users)

print('~~~~~~~~~~~~~~~~')

users.sort(key = itemgetter('age'), reverse=True)
pprint(users)
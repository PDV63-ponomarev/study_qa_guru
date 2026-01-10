import random

# while - цикл с предусловием
# пока пользовать не наведет правильный номер....

# while True:
#     print('Im teapot!')


# reqired_number = 7
# user_num = random.randint(0, 10)
#
# while reqired_number != user_num:
#     user_num = random.randint(0, 10)
#     print(f'Пользователь ввел число: {user_num}')
#
#
iteration_count = 10
# i = 0
#
# while i < iteration_count:
#     print(f'Текущая итерация: {i}')
#     i += 1

# for i in range(iteration_count):
#     print(f'Текущая итерация {i}')

# for i in range(3, iteration_count, 2):
#     print(f'Текущая итерация {i}')

# print(list(range(10)))
# print(list(range(5,15)))
# print(list(range(5,15,2)))



# for. Итерируем списки и словари

users = [
    {'name': 'John', 'age': 32},
    {'name': 'Michael', 'age': 26},
    {'name': 'Sarah', 'age': 17},
    {'name': 'Bob', 'age': 22},
]

from pprint import pprint
#
# # for user in users:
# #     pprint(f"Пользователю {user['name']} {user['age']} лет")
#
#
# d = {"first": 1,
#      "second": 2,
#      "third": 3,}
#
# for item in d.keys():
#     pprint(item)
#
# for item in d.values():
#     pprint(item)
#
# for item in d.items():
#     pprint(item)
#
# for (key, value) in d.items():
#     print(f'Ключ: "{key}" Значение: "{value}"')
#

# break/continue/else

# for i in range(iteration_count):
#     if i % 2 == 0:
#         continue #пропустить данную итерацию
#         print('Никогда не выполнится')
#     if i > 7:
#         print('Цикл прерван')
#         break #прервать операцию
#
#     print(f'Нечетное число: {i}')
#
# for i in range(5):
#
#     if i % 2 == 0:
#         continue
#
#     for j in range(5):
#         if j == 3:
#             continue
#         if j == 4:
#             break
#         print(i, j)


# enumerate - возврагает пары (инекс, значение)

cities = ['Екатеринбург', 'Москва', 'Сочи']

# i = 1
# for citi in cities:
#     print(f'{citi} на {i} месте в чем-то')
#     i += 1

for i, city in enumerate(cities):
    print(f'{city} на {i + 1} месте в чем-то')
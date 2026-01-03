# словари

d = {
    'key': 'value',
     'another key': 'another value'
     }

user1 = {
    'name': 'Vasya',
    'age': 15,
    'id': 22,
    }

user2 = {
    'name': 'Petia',
    'age': 18,
    'id': 23,
    }

users = {
    25: user1,
    42: user2
    }

print(user1)
print(user1['name'])
print(user2['name'])

print('--------------------')

print(users[42]) #если индекса нет, будет ошибка

print(users.get(42)) #если индекса нет то None
print(users.get(1)) #если индекса нет то None

#если индекса нет покажет заданные параметры
print(users.get(1,{'user': 'default user'})) 

print('--------------------')

users[55] = {
    'name': 'OLEG',
    'age': 30,
    'id': 20,
    }

print(users)


print('--------------------')

from pprint import pprint


print(users.values())
print('~~')

print(users.keys())
print('~~')

pprint(list(users.items()))


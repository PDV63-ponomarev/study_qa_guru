# boolean - 3 состояния
from xmlrpc.client import boolean

b =  bool

t = True
f = False
n = None


# if / elif / else
# True == not False

if True:
    print("I'm doing")
if False:
    print("I'm never doing")


code = 200

if 200 <= code < 400:
    print('Проверка пройдена, хороший ответ')
elif 400 <= code < 600:
    print('Плохой код ответа')
else:
    print('Странный код ответа')


# пустые обьекты - false

user_list = []
if user_list == []:
    pass
# or
if user_list:
    pass

item_num = 0
if item_num == 0:
    pass
# or
if item_num:
    pass

item_count  = ''
if item_count == '':
    pass
# or
if item_count:
    pass

print('~~~~~~~~~~~~~~~')
print(bool(100))
print(bool(-100))
print(bool(0))
print('~~~~~~~~~~~~~~~')
print(bool('abc'))
print(bool(''))
print('~~~~~~~~~~~~~~~')
print(bool([]))
print(bool([1,2,3]))
print(bool([False]))

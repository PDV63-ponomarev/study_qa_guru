# строки

s = 'Hello world'
s = "Hello word"

s = 'Hello \'world'

s = "Hello 'word'"
s = '"Hello" world'

s= ''''Hello' "world" '''
s= """'Hello' "world" """
print('--------------------')

print(s)

print('--------------------')

s = '''
Hello
world
111
'''
print(s)

print('--------------------')

s = '''Hello
world
222'''
print(s)

print('--------------------')

s = 'Hello '\
    'world 333'
print(s)

print('--------------------')

s = ('Hello '
     'world 444')
print(s)

print('--------------------')

s = 'Hello \nworld 555'
print(s)

print('--------------------')

s = 'Hello \\nworld 666'
print(s)

print('--------------------')

s = r'Hello \nworld 777'
print(s)

print('--------------------')


email ='user@mail.com'
print(email[4])
print(email[-2])
print(email[0:5])
print(email[:5])
print(email[:10:2])
print(email[::-1])

print('--------------------')

print(email.split('@'))

print('--------------------')

assert email.endswith('.com')

print('--------------------')

a = 'Hello'
b = '_'
c = 'Word'
print(a + b + c)
print(a + ' ' + c)
print(a + ', ' + c + '!')

print('{a}, {c}'.format(a=a, c=c))
print(f'{a}, {c}')

print(f'{a}, {c.upper()}')

print(f'{a=}, {c=}')

print('%s, %s!' % (a,c))

print('--------------------')

url = 'https://github.com/PDV63-ponomarev/{}'
url_les=url.format('study_qa_guru')

print(url)
print(url_les)

print('--------------------')

s = '123'
n = 123

print(s==n)

print(s==str(n))

print(int(s)==n)


print('--------------------')



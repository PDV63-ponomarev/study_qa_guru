# списки

l = [1,2,3,
     'a','b','c',
     [4,5,6]]

print(l[0])
print(l[-1])
print(l[-1][0])

print(l[::-1])

print('--------------------')

l.append('some text')
l.extend(['elem', 'another'])

print(l)

print(len(l))

print('--------------------')

l.reverse()

print(l)

print('--------------------')

l[0] = 200

print(l)

print('--------------------')


# множества

s1 = {1,2,3,4,5,6}
s2 = {2,1,2,3,4,4}
print(s1, s2)

print('--------------------')

print(list(set([2,1,2,3,4,4])))

print('--------------------')


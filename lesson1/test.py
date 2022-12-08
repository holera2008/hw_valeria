a = True
b = False

age = 18

adult1 = age >= 18  # True
print(adult1)
adult2 = age < 18  # False
print(adult2)

a = 3
b = 5
c = a < b  # True
d = a > b  # False
g = a == b  # False
f = a != b  # True
print(c)
print(d)
print(g)
print(f)
h = input('Input something: ')
print(h)
print(type(h))
print(type(int(h)))
str_10 = ''  # 10
int_10 = bool(str_10)  # True
print(int_10)
print(int_10 + 10)
# Пуста строка приводиться до False
pi = float('3.14')
# True - 1
# False - 0

name = input('What is your name?: ')
print(f'Hello {name}')

age = input('How old are you?: ')

if int(age) >= 18:
    print('You are adult already')
else:
    print('You are infant yet')


# not end or

# and
# A    B    A and B
# 1    1       1
# 1    0       0
# 0    1       0
# 0    0       0
a = True and False
print(a)  # False

# or
# A    B    A or B
# 1    1       1
# 1    0       1
# 0    1       1
# 0    0       0
b = True or False
print(b)  # True

# not
# A   not A
# 1   0
# 0   1

c = not b
print(c)  # False

is_nice = False
state = 'nice' if is_nice else 'not nice'
print(state)

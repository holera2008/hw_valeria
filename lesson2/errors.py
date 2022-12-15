a = input('Input number: ')
try:
    a = int(a)
except ValueError:
    print(f'a == {a} is not a number')


age = input('How old are you?: ')
try:
    age = int(age)
    if age >= 18:
        print('You are adult')
    else:
        print('You are infant yet!')
except ValueError:
    print(f'{age} is not a number')

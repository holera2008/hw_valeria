def say_hello():
    print('Привіт, світ!')


# виклик функції
hello = say_hello
hello()


def print_max(a, b):
    if a > b:
        print(a, 'максимальне')
    elif a == b:
        print(f'{a} == {b}')
    else:
        print(b, 'максимально')


print_max(3, 4)  # пряма передача значень

x = 5
y = 7
print_max(x, y)  # передача змінних в якості аргументів


def plus(a, b):
    return a + b


print(plus(3, 4))

x = 50


def func():
    global x
    print('x ==', x)
    x = 2
    print('Заміна глобального x на', x)


func()
print('Значення х є', x)


def func(a=None, b=5, c=10):
    print('a ==', a, 'b ==', b, 'c ==', c)


func(25, c=24)
func(c=50, a=100)
func(c=50, b=100)

# (1, 4, 6, 10, 13)
# {'name': 'Oleksandr'}


def total(a=5, *numbers, **phone_book):
    print('a', a)
    for item in numbers:
        print(f'item == {item}')
    for k, v in phone_book.items():
        print(k, v)


total(10, 1, 2, 3, Jack=1123, Piter=2231, Oleksandr=1560)
# Jack=1123, Piter=2231, Oleksandr=1560 -> {'Jack': 1123,
#                                           'Piter': 2231,
#                                           'Oleksandr': 1560}


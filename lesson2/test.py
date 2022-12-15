fruit = 'apple'

for i in fruit:
    print(i)


a = 1
while a <= 5:
    print(a)
    a += 1

a = 0
while True:
    print(a)
    if a >= 20:
        break
    a += 1


while True:
    user_input = input('Введіть будь-яке слово, exit - щоб вийти: ')
    print(user_input)
    if user_input == 'exit':
        break

x = int(input('X: '))
y = int(input('Y: '))
while True:
    if x == 0:
        print("X can't be equal to zero")
        x = int(input('X: '))
    else:
        break

result = y / x
print(result)


a = 0
while a < 6:
    a += 1
    if a % 2:
        continue
    print(a)


while True:
    number = input('number == ')
    number = int(number)
    while True:
        print(number)
        number -= 1
        if number < 0:
            break
    user_input = input('Input exit that leave: ')
    if user_input == 'exit':
        break
    else:
        continue


name = input('Input your name: ')
age = int(input('Input your age: '))
driver_license = input('Do you have driver license?: ')

if driver_license == 'No':
    driver_license = False
elif driver_license == 'Yes':
    driver_license = True

if name and age >= 18 and driver_license:
    print(f'Human {name} can rent a car')
else:
    print("Human can't rent a car")


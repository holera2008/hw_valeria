# Напишіть функцію sum_range(start, end), яка сумує всі цілі числа від
# значення start до end включно. Якщо користувач задасть перше число більше ніж друге
# просто поміняйте їх місцями


def sum_range(start: int, end: int) -> int:
    sum1 = 0
    if start > end:
        x = end
        while x <= start:
            sum1 = sum1 + x
            x = x + 1
        return(sum1)
    elif end > start:
        x = start
        while x <= end:
            sum1 = sum1 + x
            x = x + 1
        return(sum1)
    else:
        return('числа однакові')


print(sum_range(10, 0))


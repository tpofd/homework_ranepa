# TODO здесь писать код

def sum_of_numbers(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

def count_numbers(n):
    c = 0
    while n > 0:
        c += 1
        n //= 10
    return c

n = int(input('Введите число: '))

sum = sum_of_numbers(n)
c = count_numbers(n)

print('Сумма цифр:', sum)
print('Кол-во цифр в числе:', c)
print('Разность суммы и кол-ва цифр:', sum - c)
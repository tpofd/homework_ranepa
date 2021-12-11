# TODO здесь писать код

def separation_whole(number):
    flag = True
    whole = ''
    fraction = ''
    for symbol in number:
        if symbol == '.':
            flag = False
        elif flag:
            whole += symbol
        else:
            fraction += symbol
    return int(whole)

def separation_fraction(number):
    flag = True
    whole = ''
    fraction = ''
    for symbol in number:
        if symbol == '.':
            flag = False
        elif flag:
            whole += symbol
        else:
            fraction += symbol
    return int(fraction)

def revers(n):
    count = 0
    while n > 0:
        count = count * 10 + n % 10
        n //= 10
    return str(count)

def bonding(revers_whole, revers_fraction):
    revers_num = revers_whole + "." + revers_fraction
    return str(revers_num)

def summ_mun(first_num, second_num):
    summ = float(first_num) + float(second_num)
    return summ

n1 = (input("Введите первое число: "))
n2 = (input("Введите второе число: "))

n1 = bonding((revers(separation_whole(n1))), revers(separation_fraction(n1)))
n2 = bonding((revers(separation_whole(n2))), revers(separation_fraction(n2)))

print('Первое число наоборот:', n1)
print('Второе число наоборот:', n2)
print('Сумма:', summ_mun(n1, n2))
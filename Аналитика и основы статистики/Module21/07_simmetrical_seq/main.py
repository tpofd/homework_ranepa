# TODO здесь писать код

lst = []
number = int(input('Кол-во чисел: '))
for i in range(number):
    lst.append(input('Число: '))

print('Последовательность:', *lst)
for i in range(len(lst)):
    if lst[i:] == lst[i:][::-1]:
        print('Нужно приписать чисел:', i)
        print('Сами числа:', *lst[:i][::-1])
        break
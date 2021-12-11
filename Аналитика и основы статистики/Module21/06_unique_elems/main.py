# TODO здесь писать код

a = input('Первый список чисел через пробел: ').split()
b = input('Второй список чисел через пробел: ').split()

a = list(map(int, a))
b = list(map(int, b))

a.extend(b)
a = list(set(a))

print('Новый первый список с уникальными элементами:', a)
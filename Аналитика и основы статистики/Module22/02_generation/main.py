# TODO здесь писать код

lst = [x % 5 if x % 2 else 1 for x in range(int(input('Введите длину списка: ')))]
print('Результат:', lst)
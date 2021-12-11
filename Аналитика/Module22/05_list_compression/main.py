# TODO здесь писать код

import random

lst = input('Список чисел через пробел: ').split()

lst = list(map(int, lst))

lst = [i for i in lst if i]
print('Результат:', lst)
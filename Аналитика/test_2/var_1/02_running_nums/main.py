# TODO здесь писать код

step = int(input('Сдвиг: '))
initial_list = [int(el) for el in input('Изначальный список цифрами через пробел: ').split()]
finish_list = []

finish_list = initial_list[step:] + initial_list[:step]

print('Сдвинутый список:', finish_list)
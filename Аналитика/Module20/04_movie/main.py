films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

# TODO здесь писать код

favourite = []
n = int(input('Введите количество любимых фильмов: '))

for i in range(n):
    movie = input('{0} фильм: '.format(i))
    while movie not in films:
        print('Нет такого фильма!')
        movie = input('Выберете другой фильм: ')
    else:
        favourite.append(movie)

print('Cписок любимых фильмов: ', favourite)
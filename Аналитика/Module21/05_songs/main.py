violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

# TODO здесь писать код

number = int(input('Сколько песен выбрать? '))
summ = 0

for i in range(number):
    song_time = input('Название {0} песни: '.format(i + 1))
    song_here = False

    for i in range(len(violator_songs)):
        if song_time in violator_songs[i]:
            summ += violator_songs[i][1]
            song_here = True
            break

    if song_here == False:
        print('К сожалению, такой песни нет в плейлисте.')

print('Общее время звучания песен: {0} минут'.format(round(summ, 2)))

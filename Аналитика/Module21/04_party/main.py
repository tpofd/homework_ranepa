guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

# TODO здесь писать код

while True:
    print('Сейчас на вечеринке {0} человек: {1}'.format(len(guests), guests))
    guest_event = input('Гость пришел или ушел? ').lower()

    if guest_event != 'пора спать':
        name = input('Имя гостя: ')
        if guest_event == 'пришел' and len(guests) <= 5:
            print('Привет,{0}!'.format(name))
            guests.append(name)
        elif guest_event == 'пришел' and len(guests) >= 6:
            print('Прости, {0}, но мест нет.'.format(name))
        elif guest_event == 'ушел':
            print('Пока, {0}!'.format(name))
            guests.remove(name)

    else:
        print('Вечеринка закончилась, все легли спать.')
        break

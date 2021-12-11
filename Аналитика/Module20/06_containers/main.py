# TODO здесь писать код

containers = []
number = 0

containers_numbers = int(input('Кол-во контейнеров: '))
for i in range(containers_numbers):
    container = int(input('Введите вес контейнера: '))
    containers.append(container)

new_container = int(input('Введите вес нового контейнера: '))
while new_container < containers[number]:
    number += 1

print('Номер, куда встанет новый контейнер:', number + 1)
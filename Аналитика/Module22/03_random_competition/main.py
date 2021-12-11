# TODO здесь писать код

import random

team1 = [round(random.uniform(5, 10), 2) for i in range(20)]
team2 = [round(random.uniform(5, 10), 2) for i in range(20)]

win = [team1[i] if team1[i] > team2[i] else team2[i] for i in range(20)]

print('Первая команда:', team1)
print('Вторая команда:', team2)
print('Победители тура:', win)
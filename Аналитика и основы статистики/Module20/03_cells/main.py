# TODO здесь писать код

n = int(input('Кол-во клеток: '))
l = []

for i in range(n):
    ln = int(input('Эффективность {0} клетки: '.format(i + 1)))
    l.append(ln)

print('Неподходящие значения:', end=' ')
for i in range(len(l)):
    if i > l[i]:
        print(l[i], end=' ')
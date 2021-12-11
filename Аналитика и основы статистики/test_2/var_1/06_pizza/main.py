# TODO здесь писать код

n = int(input('Введите кол-во заказов: '))
d = {}
for i in range(n):
    order = input('{0} заказ: '.format(i + 1))
    fio, pizza, amount = order.rsplit(maxsplit=3)
    amount = int(amount)
    if fio not in d:
        d[fio] = {pizza: amount}
    else:
        if pizza not in d[fio]:
            d[fio] |= {pizza: amount}
        else:
            d[fio][pizza] += amount
for fio, order in sorted(d.items()):
    print(f'{fio}:')
    for pizza, amount in sorted(order.items()):
        print('    ', pizza, amount)
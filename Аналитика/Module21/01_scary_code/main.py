a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]


a.extend(b)

number_of_five = a.count(5)
print('Кол-во цифр 5 при первом объединении:', number_of_five)

for i in range(number_of_five):
    a.remove(5)

a.extend(c)
number_of_three = a.count(3)
print('Кол-во цифр 3 при втором объединении:', number_of_three)
print('Итоговый список:', a)

# TODO переписать программу

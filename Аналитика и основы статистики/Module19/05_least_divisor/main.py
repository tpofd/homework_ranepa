# TODO здесь писать код

def min_divisor(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i
    return n

n = int(input('Введите число: '))
print('Наименьший делитель, отличный от единицы:', min_divisor(n))
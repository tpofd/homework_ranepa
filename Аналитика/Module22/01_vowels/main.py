# TODO здесь писать код

text = input('Введите текст: ').lower()
vowels = []

vowels_list = set('аеиоуюя')
for letter in text:
    if letter in vowels_list:
        vowels.append(letter)

print('Список гласных букв:', vowels)
print('Длина списка:', len(vowels))
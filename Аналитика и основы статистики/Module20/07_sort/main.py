# TODO здесь писать код

def selection_sort(arr):
    for i in range(len(arr)):
        minimum = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minimum]:
                minimum = j

        arr[minimum], arr[i] = arr[i], arr[minimum]

    return arr

str_array = input('Введите список чисел через пробел: ')
first_array = list(map(int, str_array.split()))

sorted_array = selection_sort(first_array)
print('Отсортированный список:', sorted_array)
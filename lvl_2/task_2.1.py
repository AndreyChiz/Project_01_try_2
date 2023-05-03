# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!

def minimum(arr):
    min_x = arr[0]
    for numb in arr:
        if numb < min_x:
            min_x = numb

    return min_x

print(minimum([-52, 56, 30, 29, -54, 0, -110]))



def maximum(arr):
    max_x = arr[0]
    for numb in arr:
        if numb > max_x:
            max_x = numb

    return max_x

print(maximum([-52, 56, 30, 29, -54, 0, -110]))
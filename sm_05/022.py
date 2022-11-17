# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.

def find_odd_elements(numbers):
    result = [val for idx, val in enumerate(numbers) if idx % 2]
    result = sum(result)
    print(result)


numbers1 = [1, 5, 2, 3, 4, 6, 1, 7]
numbers2 = [10, 5, 2, 3, 4, 6, 1, 7]
numbers3 = [-1, 5, -2, 8, 2, 6, 1, 7]
numbers4 = [10, 9, 8, 7]

find_odd_elements(numbers1)
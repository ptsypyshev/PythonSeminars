# 1. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

# ['строка 1', 'строка', 'строка 3', 'строка', '13']
# 1 --- Да
# 3 --- Да
# 2 --- Нет


def finder(lst, number):
    for elem in lst:
        if elem.find(str(number)) >= 0:
            return 'Да'
    return 'Нет'

lst = ['строка 1', 'строка', 'строка 3', 'строка', '13']
number = int(input('Введите число: '))
print(finder(lst, number))
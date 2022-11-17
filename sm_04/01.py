# 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

numbers = [int(i) for i in input('Введите числа: ').split()]
print(f'Max = {max(numbers)}, min = {min(numbers)}')
print('Max = {}, min = {}'.format(max(numbers), min(numbers)))
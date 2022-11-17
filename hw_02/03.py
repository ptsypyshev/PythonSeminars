# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Пять позиций хранятся в списке, который вы сами заполняете.

range_limit = int(input('Введите границу диапазона: '))
numbers = [i for i in range(-range_limit, range_limit + 1)]
indexes = [int(i) for i in input('Введите индексы: ').split()]
result = 1
for idx in indexes:
    result *= numbers[idx]
print(f'Произведение равно {result}')
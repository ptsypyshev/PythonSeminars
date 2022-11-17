# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def dec_difference(floats):
    max_dec = 0
    min_dec = 1
    for num in floats:
        dec = num - int(num)
        if dec == 0:
            continue
        if dec > max_dec:
            max_dec = dec
        if dec < min_dec:
            min_dec = dec
    return 0 if max_dec - min_dec == -1 else max_dec - min_dec

print(f'{dec_difference([1.1, 1.2, 3.1, 5, 10.01]):.2f}')
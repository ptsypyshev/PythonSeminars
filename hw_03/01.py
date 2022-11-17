# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#     Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def pair_mult(numbers):
    result = []
    i = 0
    while i < len(numbers) // 2 + 1:
        result.append(numbers[i] * numbers[-i - 1])
        i +=1
    if len(numbers) % 2 == 0:
        result.pop()
    return result

print(pair_mult([2, 3, 4, 5, 6]))
print(pair_mult([2, 3, 5, 6]))

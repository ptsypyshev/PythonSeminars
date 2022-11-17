# 1. Дан список чисел. 
# Создайте список, в который попадают числа, описываемые возрастающую 
# последовательность. 
# Порядок элементов менять нельзя.
#     *Пример:* 
#     [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.


def find_inc_seq(numbers):
    for i in range(len(numbers)):
        result = []
        for elem in numbers[i:]:
            if not result:
                result.append(elem)
                continue
            if elem > result[-1]:
                result.append(elem)
        if len(result) > 1:
            return result
    return 'No ways'


numbers1 = [1, 5, 2, 3, 4, 6, 1, 7]
numbers2 = [10, 5, 2, 3, 4, 6, 1, 7]
numbers3 = [-1, 5, -2, 8, 2, 6, 1, 7]
numbers4 = [10, 9, 8, 7]

print(find_inc_seq(numbers1))
print(find_inc_seq(numbers2))
print(find_inc_seq(numbers3))
print(find_inc_seq(numbers4))

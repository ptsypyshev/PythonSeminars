# Задание 1
# Найти Максимальный элемент в списке из 5 элементов. (Не используя встроенные функции max())
# *Пример*
# Ввод: 3 -6 10 23 -14
# Ответ: 23

# numbers = [int(i) for i in input().split()]
# max_num = numbers[0]
# for num in numbers:
#     if num > max_num:
#         max_num = num
# print(f'Max number is {max_num}')

print(max([int(i) for i in input().split()]))
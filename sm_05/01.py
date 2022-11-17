# 1) В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. 
# Найдите это число.
# Пример: 1 2 3 5 6 7
# Вывод: 4

def find_lost_number(numbers):
    for i in range(1, len(numbers)):
        if numbers[i] - 1 != numbers[i - 1]:
            return numbers[i] - 1


with open('01.txt', 'r') as f:
    numbers = [int(i) for i in f.readline().split()]
    print(find_lost_number(numbers))

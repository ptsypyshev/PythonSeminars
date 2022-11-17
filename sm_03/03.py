# 3. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел. Без модуля random
# Ввод 80 100

import time  

def my_randint(start, stop):
    numbers = [i for i in range(start, stop + 1)]
    print(numbers)
    time_stamp = time.time()
    print(time_stamp)
    rand_num = int((time_stamp - int(time_stamp)) * 1000)
    rand_index = rand_num % len(numbers)
    return numbers[rand_index]

print(my_randint(int(input()), int(input())))
# print(my_randint(0, 1))
# print(my_randint(1, 1000))
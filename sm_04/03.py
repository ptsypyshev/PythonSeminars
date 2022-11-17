# 3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
# 	Ввод: 3 4
# 	Вывод: 12
	
# 	Ввод: 2 6
# 	Вывод: 6

def find_nok(num1, num2):
    for i in range(max(num1, num2), num1 * num2 + 1):
        if i % num1 == 0 and i % num2 == 0:
            return i
    return None

num1, num2 = [int(i) for i in input('Введите числа: ').split()]
print(f'Наименьшее общее кратное = {find_nok(num1, num2)}')
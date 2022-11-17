# 3) Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0, 56 -> 11

def sum_of_digits(num):
    return sum([int(i) for i in str(num) if i.isdigit()])


print(sum_of_digits(6782))
print(sum_of_digits(0.56))

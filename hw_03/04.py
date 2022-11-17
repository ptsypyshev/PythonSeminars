# Задайте число N. Составьте список чисел Фибоначчи, N - количество чисел в списке
def fib(num):
    if num in (0, 1):
        return num
    return fib(num - 1) + fib(num - 2)

print([fib(i) for i in range(int(input('Введите количество чисел Фибоначчи: ')))])
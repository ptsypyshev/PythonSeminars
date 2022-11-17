# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0
# Ввод: A, B, C
# 		D = B^2 - 4*A*C

# 		x = -D/(2*A)
    		
# 		x1 = (-b + sqrt(D)) / 2 * a
# 		x2 = (-b - sqrt(D)) / 2 * a
from math import sqrt


def find_roots(a, b, c):
    D = b ** 2 - 4 * a * c
    if D > 0:
        x1 = (-b + sqrt(D)) / (2 * a)
        x2 = (-b - sqrt(D)) / (2 * a)
        return x1, x2
    if D == 0:
        x = -b / (2 * a)
        return (x, )
    return None

a = int(input('Введите А: '))
b = int(input('Введите B: '))
c = int(input('Введите C: '))

result = find_roots(a, b, c)

if not result:
    print('Нет корней')
elif len(result) == 2:
    print(f'Корни = {result[0]} и {result[1]}')
else:
    print(f'Корeнь = {result[0]}')



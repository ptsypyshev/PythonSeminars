from math import sqrt


point_a_x, point_a_y = [int(i) for i in input('Введите координаты точки А (через пробел): ').split()]
point_b_x, point_b_y = [int(i) for i in input('Введите координаты точки B (через пробел): ').split()]
result = sqrt((point_a_y - point_b_y) ** 2 + (point_a_x - point_b_x) ** 2)
print(f'Расстояние между точками А и B равно {result:.2f}')
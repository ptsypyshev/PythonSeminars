# Пользователь вводит число, Вам необходимо вывести число Пи с той точностью знаков после запятой, сколько указал пользователь(БЕЗ ИСПОЛЬЗОВАНИЯ МОДУЛЕЙ/БИБЛИОТЕК)

from math import pi

accuracy = int(input('Введите точность для числа Пи: '))
print(f'Пи = {str(pi)[:accuracy + 2]}') if accuracy else print('Пи = 3')
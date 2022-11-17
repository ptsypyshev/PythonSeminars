quarter = int(input('Введите номер четверти: '))
if quarter == 1:
    print('x в диапазоне [0, inf], y в диапазоне [0, inf]')
elif quarter == 2:
    print('x в диапазоне [-inf, 0], y в диапазоне [0, inf]')
elif quarter == 3:
    print('x в диапазоне [-inf, 0], y в диапазоне [-inf, 0]')
elif quarter == 4:
    print('x в диапазоне [0, inf], y в диапазоне [-inf, 0]')
else:
    print(f'Введен некорректный номер четверти: {quarter}')
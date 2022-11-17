num = float(input())
float_part = num - int(num)
if int(num) == num:
    print('нет')
else:
    print(int(float_part* 10))
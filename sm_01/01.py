num1, num2 = input().split(',')
if int(num1) ** 2 == int(num2) or int(num2) ** 2 == int(num1):
    print('да')
else:
    print('нет')
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def dec_to_bin(number):
    result = []
    while number > 0:
        result.append(str(number % 2))
        number //= 2
    return ''.join(result[::-1])

print(dec_to_bin(45))
print(dec_to_bin(3))
print(dec_to_bin(2))
print(dec_to_bin(int(input('Введите свое число для перевода в Bin: '))))
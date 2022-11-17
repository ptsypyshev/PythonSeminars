# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def rle_encode(data):
    count = 0
    char = data[0]
    result = ''
    for elem in data:
        if elem != char:
            result += f'{count}{char}'
            char = elem
            count = 0
        count += 1
    else:
        result += f'{count}{char}'
    return result


def rle_decode(data):
    count = 0
    result = ''
    for elem in data:
        try:
            count = int(elem)
        except ValueError:
            result += elem * count
    return result


if __name__ == "__main__":
    print(rle_encode("aaabbbbccbbb"))
    print(rle_decode("3a4b2c3b"))

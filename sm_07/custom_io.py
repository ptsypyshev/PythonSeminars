INPUT_MSG = "Введите выражение без пробелов: "


def get_operations():
    return input(INPUT_MSG)


def parse(operation):
    lst = []
    tmp = ''
    for char in operation:
        if not char.isdigit():
            lst.append(float(tmp))
            lst.append(char)
            tmp = ''
        else:
            tmp += char
    else:
        lst.append(float(tmp))
    return lst

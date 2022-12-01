def parse(operation: str) -> list:
    '''Парсинг введенной строки в список'''
    lst = []
    tmp = ''
    for char in operation:
        if char == ' ':
            continue
        elif not char.isdigit():
            lst.append(float(tmp))
            lst.append(char)
            tmp = ''
        else:
            tmp += char
    else:
        lst.append(float(tmp))
    return lst


def calc(lst):
    '''Вычисление выражения из списка'''
    result = 0
    for elem in lst:
        if elem in ("*", "/"):
            index = lst.index(elem)
            if elem == "*":
                result = lst[index - 1] * lst[index + 1]
            else:
                result = lst[index - 1] / lst[index + 1]
            lst = lst[:index - 1] + [result] + lst[index + 2:]
    for elem in lst:
        if elem in ("+", "-"):
            index = lst.index(elem)
            if elem == "+":
                result = lst[index - 1] + lst[index + 1]
            else:
                result = lst[index - 1] - lst[index + 1]
            lst = lst[:index - 1] + [result] + lst[index + 2:]
    return result

from custom_io import get_operations, parse
from custom_log import Logger

LOG_FILE = "calc.log"


def calc(lst):
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


def run():
    logger = Logger(LOG_FILE)
    operations = get_operations()
    logger.log(f"Get input {operations}")
    parsed_lst = parse(operations)
    try:
        result = calc(parsed_lst)
        result_str = f"Результат = {result}"
        print(result_str)
        logger.log(result_str)
    except ZeroDivisionError as e:
        print("На ноль делить нельзя!")
        logger.log(e)

# 1. Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
#     *Пример:*
#     2+2 => 4;
#     1+2*3 => 7;
#     1-2*3 => -5;
#     * Добавьте возможность использования скобок, меняющих приоритет операций.
#         *Пример:*
#         1+2*3 => 7;
#         (1+2)*3 => 9;
def calc(s: str):
    nums = []
    tmp = ''

    for elem in s:
        if not elem.isdigit():
            nums.append(int(tmp))
            nums.append(elem)
            tmp = ''
        else:
            tmp += elem
    else:
        nums.append(int(tmp))

    while "*" in nums:
        idx = nums.index("*")
        nums[idx - 1] *= nums.pop(idx + 1)
        nums.pop(idx)
    while "/" in nums:
        idx = nums.index("/")
        nums[idx - 1] /= nums.pop(idx + 1)
        nums.pop(idx)
    while "-" in nums:
        idx = nums.index("-")
        nums[idx - 1] -= nums.pop(idx + 1)
        nums.pop(idx)
    while "+" in nums:
        idx = nums.index("+")
        nums[idx - 1] += nums.pop(idx + 1)
        nums.pop(idx)
    return nums[0]


if __name__ == "__main__":
    print(calc(input()))

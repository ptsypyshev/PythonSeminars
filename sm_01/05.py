def checker(num):
    if (num % 5 == 0 and num % 10 == 0) or num %15 == 0:
        if num % 30 == 0:
            return False
        else:
            return True
    return False

num = int(input())
print(checker(num))

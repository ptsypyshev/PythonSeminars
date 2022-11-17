# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def prime_numbers(limit):
    sieve = [0 if i in (0, 1) else i for i in range(limit + 1)]
    step = 2
    while step ** 2 <= limit:
        if sieve[step] != 0:
            for x in range(step ** 2, limit + 1, step):
                sieve[x] = 0
        step += 1

    result = set(sieve)
    result.remove(0)
    return sorted(result)


def factorize(number):
    result = []
    for prime in prime_numbers(number):
        while number % prime == 0:
            result.append(prime)
            number = number // prime
    return result


print('N =', ' * '.join(str(i) for i in factorize(int(input('Введите N: ')))))

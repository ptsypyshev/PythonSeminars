# from itertools import permutations


# combinations = (
#     (0, 0, 0),
#     (0, 0, 1),
#     (0, 1, 0),
#     (0, 1, 1),
#     (1, 0, 0),
#     (1, 0, 1),
#     (1, 1, 0),
#     (1, 1, 1)
# )

# combinations = permutations([0, 1], 3)
# print(combinations)

# for combination in list(combinations):
#     print(combination)
#     x, y, z = combination[0], combination[1], combination[2]
#     print(f'Результат проверки для {x}, {y} и {z} будет', not(x or y or z) == (not(x) and not(y) and not(z)))

# Как я понимаю, чтоя данного выражения результат всегда будет True

# A Python program to print all 
# permutations of given length 
# from itertools import permutations
# perm = permutations([0, 0, 0, 1, 1, 1], 3) 
# for i in set(perm): 
#     print (i) 

from itertools import product
values = (0, 1)
perms = product(values, repeat=3)
for step in list(perms):
    print(step)
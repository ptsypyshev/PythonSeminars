# Дан список
# Получить список уникальных элементов
def get_unique(lst):
    hashmap = {}
    for elem in lst:
        hashmap[elem] = hashmap.get(elem, 0) + 1
    return [key for key, val in hashmap.items() if val == 1]


print(get_unique([1, 2, 3, 4, 1, 3, 1]))

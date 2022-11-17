# 2) Дан список, вывести отдельно буквы и цифры, пользуясь filter.
# [12,'sadf',5643] ---> ['sadf'] ,[12,5643]
# Все задачи решать с помощью использования
# лямбд, filter, map, zip, enumerate, List Comprehension

def filter_alphas(lst):
    alphas = list(filter(lambda x: isinstance(x, str), lst))
    digits = list(filter(lambda x: isinstance(x, (int, float)), lst))
    return alphas, digits


print(filter_alphas([12, 'sadf', 5643]))

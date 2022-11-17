# Задание 3
# Петя и Катя - брат и сестра. Петя - студент, а Катя - школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числ а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение Р 
# Помогите Кате отгадать задуманные Петей числа.
# *Пример*
# Ввод: 4 4
# Вывод: 2 2
# *Пример*
# Ввод: 5 6
# Вывод: 2 3

def num_finder(sum, mult):
    for i in range(1, sum+1):
        for j in range(1, sum+1):
            if i + j == sum and i * j == mult:
                return i, j
    return None

sum, mult = [int(i) for i in input().split()]
result = num_finder(sum, mult)
print(f'Числа: {result[0]} {result[1]}') if result != None else print("Числа не найдены")
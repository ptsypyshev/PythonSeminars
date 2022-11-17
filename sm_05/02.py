substr = 'абв'

with open('02.txt', 'r', encoding='utf-8') as f:
    for word in f.read().split():
        if word.find(substr) == -1:
            print(word, end=' ')

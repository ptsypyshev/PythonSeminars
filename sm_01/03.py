n = int(input())
lst = []
for i in range(-n, n + 1):
    lst.append(i)
print(*lst, sep=", ")
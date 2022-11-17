# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

def get_elements(filename):
    elements_dict = {}
    with open(filename, 'r') as f:
        line = f.readline().strip(" = 0")
        elements = line.split("+")        
        for elem in elements:
            try:
                factor, degree = [int(i) for i in elem.split('*x^')]
                elements_dict[degree] = factor
            except ValueError:
                if 'x' in elem:
                    elements_dict[1] = int(elem.split('*')[0])
                else:
                    elements_dict[0] = int(elem)
    return elements_dict

first = get_elements('first.txt')
second = get_elements('second.txt')

for i in range(max(len(first), len(second)) - 1, -1, -1):
    factor = first.get(i, 0) + second.get(i, 0)
    if factor == 0:
        continue
    elif factor == 1:
        factor = ''
    else:
        factor = f'{factor}*x^{i} +' if i != 0 else f'{factor} = 0'
    print(factor, end=' ')

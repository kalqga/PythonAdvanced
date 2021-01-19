n = int(input())

matrix = []
asd = False

for row in range(n):
    current_row = []
    for ch in input():
        current_row.append(ch)
    matrix.append(current_row)

searched = input()

for i in range(n):
    for el in range(n):
        if searched == matrix[i][el]:
            print(f'({i}, {el})')
            asd = False
            break
        else:
            asd = True

if asd:
    print(f'{searched} does not occur in the matrix')


### 60/100
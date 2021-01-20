n = int(input())

matrix = []
is_found = False

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
            is_found = True
            break
        else:
            is_found = False
    if is_found:
        break

if not is_found:
    print(f'{searched} does not occur in the matrix')


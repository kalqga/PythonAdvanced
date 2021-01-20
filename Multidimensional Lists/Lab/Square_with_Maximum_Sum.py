rows_count, columns_count = list(map(int, input().split(', ')))

matrix = []
MAX_SQUARE = 0
suma = 0
max_matrix = []

for rows in range(rows_count):
    row = list(map(int, input().split(', ')))
    matrix.append(row)

for e in range(rows_count-1):
    for i in range(columns_count-1):
        suma = matrix[e][i] + matrix[e][i+1] + matrix[e+1][i] + matrix[e+1][i+1]
        if suma > MAX_SQUARE:
            MAX_SQUARE = suma
            max_matrix = []
            max_matrix.append(list(map(int, (matrix[e][i], matrix[e][i+1]))))
            max_matrix.append(list(map(int, (matrix[e+1][i], matrix[e+1][i+1]))))

print(f"{max_matrix[0][0]} {max_matrix[0][1]}")
print(f"{max_matrix[1][0]} {max_matrix[1][1]}")
print(MAX_SQUARE)

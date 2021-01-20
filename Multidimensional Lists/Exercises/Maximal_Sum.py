row_count, column_count = list(map(int, input().split()))

matrix = []
MAX_SQUARE = 0
max_matrix = []

for rows in range(row_count):
    row = list(map(int, input().split()))
    matrix.append(row)

for e in range(row_count-2):
    for i in range(column_count-2):
        suma = matrix[e][i] + matrix[e][i+1] + matrix[e][i+2] + matrix[e+1][i] + matrix[e+1][i+1] + matrix[e+1][i+2] +\
               matrix[e+2][i] + matrix[e+2][i+1] + matrix[e+2][i+2]
        if suma > MAX_SQUARE:
            MAX_SQUARE = suma
            max_matrix = []
            max_matrix.append(list(map(int, (matrix[e][i], matrix[e][i+1], matrix[e][i+2]))))
            max_matrix.append(list(map(int, (matrix[e+1][i], matrix[e+1][i+1], matrix[e+1][i+2]))))
            max_matrix.append(list(map(int, (matrix[e + 2][i], matrix[e + 2][i + 1], matrix[e + 2][i + 2]))))

print(f"Sum = {MAX_SQUARE}")
print(f"{max_matrix[0][0]} {max_matrix[0][1]} {max_matrix[0][2]}")
print(f"{max_matrix[1][0]} {max_matrix[1][1]} {max_matrix[1][2]}")
print(f"{max_matrix[2][0]} {max_matrix[2][1]} {max_matrix[2][2]}")

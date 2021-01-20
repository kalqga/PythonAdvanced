row_count, column_count = list(map(int, input().split()))

matrix = []
count = 0

for rows in range(row_count):
    row = list(map(str, input().split()))
    matrix.append(row)

for e in range(row_count - 1):
    for i in range(column_count - 1):
        if matrix[e][i] == matrix[e][i + 1] == matrix[e + 1][i] == matrix[e + 1][i + 1]:
            count += 1

print(count)

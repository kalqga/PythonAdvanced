(rows_count, columns_count) = list(map(int, input().split(', ')))

matrix = []


for row in range(rows_count):
    nums = list(map(int, input().split()))
    matrix.append(nums)

for column in range(columns_count):
    suma = 0
    for i in range(rows_count):
        suma += matrix[i][column]
    print(suma)


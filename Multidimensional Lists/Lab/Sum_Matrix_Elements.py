def read_matrix():
    (rows_count, columns_count) = list(map(int, input().split(', ')))
    matrix = []
    suma = 0
    for row_index in range(rows_count):
        row = list(map(int, input().split(', ')))
        matrix.append(row)
        for i in range(len(row)):
            suma += row[i]
    print(suma)
    return matrix


print(read_matrix())

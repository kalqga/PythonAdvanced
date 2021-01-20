rows_count, columns_count = list(map(int, input().split()))

snake = [el for el in input()]

matrix = []
index_snake = 0

for rows in range(rows_count):
    matrix.append([0 for el in range(columns_count)])

for rows in range(rows_count):
    for columns in range(columns_count):
        matrix[rows][columns] = snake[index_snake]
        index_snake += 1
        if index_snake == len(snake):
            index_snake = 0

for row_index in range(rows_count):
    if row_index % 2 == 1:
        matrix[row_index].reverse()
    print(''.join(matrix[row_index]))

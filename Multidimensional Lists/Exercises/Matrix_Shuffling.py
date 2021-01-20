rows_count, columns_count = list(map(int, input().split()))

matrix = []
is_valid = True

for rows in range(rows_count):
    row = list(map(str, input().split()))
    matrix.append(row)


while True:
    data = input().split()

    if data[0] == 'END':
        break
    elif data[0] == 'swap' and len(data) == 5:
        row1 = int(data[1])
        col1 = int(data[2])
        row2 = int(data[3])
        col2 = int(data[4])

        if (row1 and row2) in range(rows_count) and (col1 and col2) in range(columns_count):

            matrix[row1][col1], matrix[row2][col2] = \
                matrix[row2][col2], matrix[row1][col1]

            [print(*row, sep=' ') for row in matrix]
        else:
            print('Invalid input!')
    else:
        print('Invalid input!')

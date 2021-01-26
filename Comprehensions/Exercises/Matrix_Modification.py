n = int(input())

matrix = [(list(map(int, input().split()))) for _ in range(n)]


while True:
    data = input()
    if data == 'END':
        break

    command, row, column, value = data.split()
    row = int(row)
    column = int(column)
    value = int(value)

    if 0 <= row < n and 0 <= column < n:
        if command == 'Add':
            matrix[row][column] += value
        elif command == 'Subtract':
            matrix[row][column] -= value
    else:
        print('Invalid coordinates')

[print(*row, sep=' ') for row in matrix]

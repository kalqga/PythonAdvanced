size_of_square_matrix = int(input())

matrix = []

for _ in range(size_of_square_matrix):
    row = list(map(int, input().split()))
    matrix.append(row)

data = input().split()

for el in data:
    command = el.split(',')
    row = int(command[0])
    col = int(command[1])
    bomb = matrix[row][col]

    if bomb > 0:
        try:
            k = row - 1
            l = col - 1
            if matrix[k][l] > 0 and k >= 0 and l >= 0:
                matrix[k][l] -= bomb
        except:
            IndexError
        try:
            k = row - 1
            l = col
            if matrix[k][l] > 0 and k >= 0 and l >= 0:
                matrix[k][l] -= bomb
        except:
            IndexError
        try:
            k = row - 1
            l = col + 1
            if matrix[k][l] > 0 and k >= 0 and l >= 0:
                matrix[k][l] -= bomb
        except:
            IndexError
        try:
            k = row
            l = col - 1
            if matrix[k][l] > 0 and k >= 0 and l >= 0:
                matrix[k][l] -= bomb
        except:
            IndexError
        try:
            k = row
            l = col + 1
            if matrix[k][l] > 0 and k >= 0 and l >= 0:
                matrix[k][l] -= bomb
        except:
            IndexError
        try:
            k = row + 1
            l = col - 1
            if matrix[k][l] > 0 and k >= 0 and l >= 0:
                matrix[k][l] -= bomb
        except:
            IndexError
        try:
            k = row + 1
            l = col
            if matrix[k][l] > 0 and k >= 0 and l >= 0:
                matrix[k][l] -= bomb
        except:
            IndexError
        try:
            k = row + 1
            l = col + 1
            if matrix[k][l] > 0 and k >= 0 and l >= 0:
                matrix[k][l] -= bomb
        except:
            IndexError

        matrix[row][col] = 0

alive = [x for row in matrix for x in row if x > 0]

print(f"Alive cells: {len(alive)}")
print(f"Sum: {sum(alive)}")

for el in matrix:
    print(' '.join(map(str, el)))

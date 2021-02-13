def valid_index(row, col):
    if row in range(n) and col in range(n):
        return True
    return False


def move_down(current_row, current_col, word):
    new_row = current_row + 1
    new_col = current_col
    if valid_index(new_row, new_col):
        if matrix[new_row][new_col] == '-':
            matrix[new_row][new_col], matrix[current_row][current_col] = matrix[current_row][current_col], matrix[new_row][new_col]
        else:
            current_element = matrix[new_row][new_col]
            word += current_element
            matrix[new_row][new_col] = 'P'
            matrix[current_row][current_col] = '-'
        return new_row, new_col, word
    else:
        return current_row, current_col, word[:-1]


def move_up(current_row, current_col, word):
    new_row = current_row - 1
    new_col = current_col
    if valid_index(new_row, new_col):
        if matrix[new_row][new_col] == '-':
            matrix[new_row][new_col], matrix[current_row][current_col] = matrix[current_row][current_col], matrix[new_row][new_col]
        else:
            current_element = matrix[new_row][new_col]
            word += current_element
            matrix[new_row][new_col] = 'P'
            matrix[current_row][current_col] = '-'
        return new_row, new_col, word
    else:
        return current_row, current_col, word[:-1]


def move_left(current_row, current_col, word):
    new_row = current_row
    new_col = current_col - 1
    if valid_index(new_row, new_col):
        if matrix[new_row][new_col] == '-':
            matrix[new_row][new_col], matrix[current_row][current_col] = matrix[current_row][current_col], matrix[new_row][new_col]
        else:
            current_element = matrix[new_row][new_col]
            word += current_element
            matrix[new_row][new_col] = 'P'
            matrix[current_row][current_col] = '-'
        return new_row, new_col, word
    else:
        return current_row, current_col, word[:-1]


def move_right(current_row, current_col, word):
    new_row = current_row
    new_col = current_col + 1
    if valid_index(new_row, new_col):
        if matrix[new_row][new_col] == '-':
            matrix[new_row][new_col], matrix[current_row][current_col] = matrix[current_row][current_col], matrix[new_row][new_col]
        else:
            current_element = matrix[new_row][new_col]
            word += current_element
            matrix[new_row][new_col] = 'P'
            matrix[current_row][current_col] = '-'
        return new_row, new_col, word
    else:
        return current_row, current_col, word[:-1]


initial_string = input()
n = int(input())

matrix = []
p_row_index = None
p_col_index = None

for row_index in range(n):
    row_ = list(input())
    if 'P' in row_:
        p_row_index = row_index
        p_col_index = row_.index('P')
    matrix.append(row_)

n_commands = int(input())

for _ in range(n_commands):
    command = input()

    if command == 'up':
        p_row_index, p_col_index, initial_string = move_up(p_row_index, p_col_index, initial_string)
    elif command == 'down':
        p_row_index, p_col_index, initial_string = move_down(p_row_index, p_col_index, initial_string)
    elif command == 'left':
        p_row_index, p_col_index, initial_string = move_left(p_row_index, p_col_index, initial_string)
    elif command == 'right':
        p_row_index, p_col_index, initial_string = move_right(p_row_index, p_col_index, initial_string)

print(initial_string)
for r in range(n):
    print(''.join(matrix[r]))

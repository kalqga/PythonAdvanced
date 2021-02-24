from math import floor


def is_valid_index(row, col):
    if row in range(size_of_field) and col in range(size_of_field):
        return True
    return False


def move_up(current_row, current_col, coins, moves, game_over):
    new_row = current_row - 1
    new_col = current_col
    if is_valid_index(new_row, new_col):
        if matrix[new_row][new_col] == 'X':
            game_over = True
            return current_row, current_col, coins, moves, game_over
        else:
            coins += int(matrix[new_row][new_col])
            matrix[new_row][new_col] = 'P'
            matrix[current_row][current_col] = '0'
            moves.append([new_row, new_col])
        return new_row, new_col, coins, moves, game_over
    else:
        game_over = True
        return current_row, current_col, coins, moves, game_over


def move_down(current_row, current_col, coins, moves, game_over):
    new_row = current_row + 1
    new_col = current_col
    if is_valid_index(new_row, new_col):
        if matrix[new_row][new_col] == 'X':
            game_over = True
            return current_row, current_col, coins, moves, game_over
        else:
            coins += int(matrix[new_row][new_col])
            matrix[new_row][new_col] = 'P'
            matrix[current_row][current_col] = '0'
            moves.append([new_row, new_col])
        return new_row, new_col, coins, moves, game_over
    else:
        game_over = True
        return current_row, current_col, coins, moves, game_over


def move_right(current_row, current_col, coins, moves, game_over):
    new_row = current_row
    new_col = current_col + 1
    if is_valid_index(new_row, new_col):
        if matrix[new_row][new_col] == 'X':
            game_over = True
            return current_row, current_col, coins, moves, game_over
        else:
            coins += int(matrix[new_row][new_col])
            matrix[new_row][new_col] = 'P'
            matrix[current_row][current_col] = '0'
            moves.append([new_row, new_col])
        return new_row, new_col, coins, moves, game_over
    else:
        game_over = True
        return current_row, current_col, coins, moves, game_over


def move_left(current_row, current_col, coins, moves, game_over):
    new_row = current_row
    new_col = current_col - 1
    if is_valid_index(new_row, new_col):
        if matrix[new_row][new_col] == 'X':
            game_over = True
            return current_row, current_col, coins, moves, game_over
        else:
            coins += int(matrix[new_row][new_col])
            matrix[new_row][new_col] = 'P'
            matrix[current_row][current_col] = '0'
            moves.append([new_row, new_col])
        return new_row, new_col, coins, moves, game_over
    else:
        game_over = True
        return current_row, current_col, coins, moves, game_over




size_of_field = int(input())

coins = 0
game_over = False
win = False
matrix = []
moves = []
p_row_index = None
p_col_index = None

for row_index in range(size_of_field):
    row_ = list(input().split())
    if 'P' in row_:
        p_row_index = row_index
        p_col_index = row_.index('P')
    matrix.append(row_)


while True:
    command = input()

    if command == 'up':
        p_row_index, p_col_index, coins, moves, game_over = move_up(p_row_index, p_col_index, coins, moves, game_over)
        if game_over:
            break
        elif coins >= 100:
            win = True
            break
    elif command == 'down':
        p_row_index, p_col_index, coins, moves, game_over = move_down(p_row_index, p_col_index, coins, moves, game_over)
        if game_over:
            break
        elif coins >= 100:
            win = True
            break
    elif command == 'left':
        p_row_index, p_col_index, coins, moves, game_over = move_left(p_row_index, p_col_index, coins, moves, game_over)
        if game_over:
            break
        elif coins >= 100:
            win = True
            break
    elif command == 'right':
        p_row_index, p_col_index, coins, moves, game_over = move_right(p_row_index, p_col_index, coins, moves, game_over)
        if game_over:
            break
        elif coins >= 100:
            win = True
            break

if game_over:
    print(f"Game over! You've collected {floor(coins/2)} coins.")
    print("Your path:")
    for el in moves:
        print(el)
elif win:
    print(f"You won! You've collected {coins} coins.")
    print("Your path:")
    for el in moves:
        print(el)

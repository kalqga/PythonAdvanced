def read_board():
    matrix = []
    for _ in range(8):
        matrix.append(input().split())
    return matrix


def find_king_position(board):
    for row_index in range(8):
        for col_index in range(8):
            if board[row_index][col_index] == 'K':
                return (row_index, col_index)


def in_range(value, max_value):
    return 0 <= value < max_value


def search_with_deltas(board, king, deltas):
    (king_row_index, king_column_index) = king
    (delta_row, delta_column) = deltas

    while in_range(king_row_index, 8) and in_range(king_column_index, 8):
        if board[king_row_index][king_column_index] == 'Q':
            return [king_row_index, king_column_index]

        king_row_index += delta_row
        king_column_index += delta_column


def get_capturing_queens(board, king):
    deltas = [
        (0, -1),
        (-1, -1),
        (-1, 0),
        (-1, +1),
        (0, +1),
        (+1, +1),
        (+1, 0),
        (+1, -1),
    ]

    queens = [
        search_with_deltas(board, king, delta)
        for delta in deltas
    ]
    return [queen for queen in queens if queen]


def print_result(queens):
    if queens:
        for el in queens:
            print(el)
    else:
        print('The king is safe!')


board = read_board()
king = find_king_position(board)
queens = get_capturing_queens(board, king)
print_result(queens)

n = int(input())

matrix = [list(map(int, input().split(', '))) for row in range(n)]
first_diag = [matrix[row][row] for row in range(n)]
sec_diag = [matrix[row][-row - 1] for row in range(n)]
print("First diagonal: " + ', '.join(map(str, first_diag)) + '. Sum:', sum(first_diag))
print("Second diagonal: " + ', '.join(map(str, sec_diag)) + '. Sum:', sum(sec_diag))

import math

n = int(input())

matrix = []
first_diagonal = 0
second_diagonal = 0
total = 0

for rows in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

    first_diagonal += matrix[rows][rows]

    second_diagonal += matrix[rows][-(rows+1)]


total = first_diagonal - second_diagonal
print(f"{math.fabs(total):.0f}")

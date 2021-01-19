n = int(input())

matrix = []
suma = 0

for row in range(n):
    matrix.append(list(map(int, input().split())))
    suma += matrix[row][row]

print(suma)

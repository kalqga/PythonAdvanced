n = int(input())

matrix = [[int(j) for j in input().split(', ')] for i in range(n)]
flat = [x for row in matrix for x in row]
print(flat)

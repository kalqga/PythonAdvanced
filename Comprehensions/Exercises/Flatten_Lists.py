string = input().split('|')
matrix = [[i.split()] for i in string]

flat = [x for row in range(0, len(matrix))[::-1] for x in matrix[row]]

asd = [print(el, end=' ') for ch in flat for el in ch]

first = input().split(', ')
second = input().split(', ')

x = zip(first, second)

dic = {print(f"{a} -> {b}") for a, b in tuple(x)}

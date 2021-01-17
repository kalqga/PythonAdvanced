n = int(input())

a = set()

for _ in range(n):
    data = input().split()
    for el in data:
        a.add(el)

for ch in a:
    print(ch)

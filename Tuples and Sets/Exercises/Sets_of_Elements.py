n, m = [int(el) for el in input().split()]

a = set()
b = set()

for _ in range(n):
    a.add(input())

for _ in range(m):
    b.add((input()))

c = a & b
for el in c:
    print(el)

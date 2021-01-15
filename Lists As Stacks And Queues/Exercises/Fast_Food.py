from collections import deque

q = deque()
asd = False
food_quantity = int(input())
orders = input().split()

for el in orders:
    q.append(int(el))

print(max(q))

while len(q) > 0:

    if food_quantity >= q[0]:
        food_quantity -= q.popleft()
    else:
        asd = True
        break

if asd:
    q = list(map(str, q))
    print(f"Orders left: {' '.join(q)}")
else:
    print("Orders complete")

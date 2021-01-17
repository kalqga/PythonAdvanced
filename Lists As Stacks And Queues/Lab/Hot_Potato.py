from collections import deque

kids = input().split()
tosses = int(input())

q = deque(kids)

counter = 0

while len(q) > 1:
    counter += 1
    current_kid = q.popleft()
    if counter == tosses:
        print(f'Removed {current_kid}')
        counter = 0
    else:
        q.append(current_kid)

print(f'Last is {q[0]}')


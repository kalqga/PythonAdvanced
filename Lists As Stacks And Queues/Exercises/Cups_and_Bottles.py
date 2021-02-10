from collections import deque

cups_capacity = deque(int(el) for el in input().split())
bottles_capacity = [int(el) for el in input().split()]

wasted_water = 0

while True:

    if not cups_capacity or not bottles_capacity:
        break

    bottle = bottles_capacity.pop()
    cup = cups_capacity.popleft()
    total = bottle - cup

    if total >= 0:
        wasted_water += total
    elif total < 0:
        cups_capacity.appendleft(abs(total))


if not cups_capacity:
    print(f"Bottles: {' '.join(map(str, bottles_capacity))}")
    print(f"Wasted litters of water: {wasted_water}")
elif not bottles_capacity:
    print(f"Cups: {' '.join(map(str, cups_capacity))}")
    print(f"Wasted litters of water: {wasted_water}")

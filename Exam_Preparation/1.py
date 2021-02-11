from collections import deque

males = list(map(int, input().split()))
females = deque(map(int, input().split()))

men = False
waman = False

matches = 0


while True:
    if len(males) == 0 and len(females) == 0:
        men = True
        waman = True
        break
    elif len(males) == 0:
        men = True
        break
    elif len(females) == 0:
        waman = True
        break

    male = males[-1]
    female = females[0]

    if male <= 0:
        males.pop()
    elif female <= 0:
        females.popleft()

    elif male % 25 == 0:
        males.pop()
        males.pop()

    elif female % 25 == 0:
        females.popleft()
        females.popleft()

    elif male == female:
        matches += 1
        males.pop()
        females.popleft()

    elif male != female:
        males[-1] -= 2
        females.popleft()

print(f"Matches: {matches}")
if men:
    print("Males left: none")
else:
    print(f"Males left: {', '.join(map(str, reversed(males)))}")
if waman:
    print("Females left: none")
else:
    print(f"Females left: {', '.join(map(str, females))}")

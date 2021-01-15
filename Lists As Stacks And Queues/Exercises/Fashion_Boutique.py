clothes = [int(el) for el in input().split()]

rack_capacity = int(input())
current_cap = 0
counter = 0

while clothes:

    while current_cap < rack_capacity and clothes:
        if current_cap + clothes[-1] > rack_capacity:
            break
        current_cap += clothes.pop()
    if current_cap:
        counter += 1
        current_cap = 0

print(counter)

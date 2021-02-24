from collections import deque

firework_effects = deque([int(el) for el in input().split(', ')])
explosive_power = [int(el) for el in input().split(', ')]

palm_fireworks = 0
willow_fireworks = 0
crossette_fireworks = 0

is_perfect_show = False

while firework_effects and explosive_power:

    current_effect = firework_effects[0]
    current_explosive = explosive_power[-1]
    sum_of_both = current_effect + current_explosive

    if current_effect > 0 and current_explosive > 0:

        if sum_of_both % 3 == 0 and sum_of_both % 5 != 0:
            palm_fireworks += 1
            firework_effects.popleft()
            explosive_power.pop()

        elif sum_of_both % 5 == 0 and sum_of_both % 3 != 0:
            willow_fireworks += 1
            firework_effects.popleft()
            explosive_power.pop()

        elif sum_of_both % 3 == 0 and sum_of_both % 5 == 0:
            crossette_fireworks += 1
            firework_effects.popleft()
            explosive_power.pop()

        else:
            firework_effects.popleft()
            current_effect -= 1
            if current_effect > 0:
                firework_effects.append(current_effect)

    elif current_effect <= 0:
        firework_effects.popleft()
    elif current_explosive <= 0:
        explosive_power.pop()

    if palm_fireworks >= 3 and willow_fireworks >= 3 and crossette_fireworks >= 3:
        is_perfect_show = True
        break

if is_perfect_show:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can’t make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join(map(str, firework_effects))}")
if explosive_power:
    print(f"Explosive Power left: {', '.join(map(str, explosive_power))}")
print(f"Palm Fireworks: {palm_fireworks}")
print(f"Willow Fireworks: {willow_fireworks}")
print(f"Crossette Fireworks: {crossette_fireworks}")

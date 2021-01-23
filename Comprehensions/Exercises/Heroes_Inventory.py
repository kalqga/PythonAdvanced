names = [name for name in input().split(', ')]

names_inventory = {name: [] for name in names}
names_cost = {name: [] for name in names}

while True:
    line = input()
    if line == 'End':
        break
    name, inventory, cost = line.split('-')
    if inventory not in names_inventory[name]:
        names_inventory[name].append(inventory)
        names_cost[name].append(int(cost))

[print(f'{name} -> Items: {len(values)}, Cost: {sum(names_cost[name])}') for name, values in names_inventory.items()]
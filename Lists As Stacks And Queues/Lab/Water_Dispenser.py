from collections import deque

water_quantity = int(input())

q = deque()

while True:
    command = input()
    if command == 'Start':
        break
    q.append(command)

while True:
    command = input().split()
    if command[0] == 'End':
        print(f'{water_quantity} liters left')
        break
    elif command[0] == 'refill':
        water_quantity += int(command[1])
    elif water_quantity >= int(command[0]):
        water_quantity -= int(command[0])
        print(f'{q.popleft()} got water')
    elif water_quantity < int(command[0]):
        print(f'{q.popleft()} must wait')

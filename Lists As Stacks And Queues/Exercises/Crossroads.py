from collections import deque

green_light_time = int(input())
free_window_time = int(input())

cars_queue = deque()
cars_passed = deque()
crash = False

total_passing = green_light_time + free_window_time
current_passing = total_passing
current_green = green_light_time

while True:

    command = input()

    if command == 'END':
        break

    elif command == 'green':
        current_green = green_light_time
        current_passing = total_passing

        while len(cars_queue) > 0:
            car = cars_queue.popleft()

            if current_green >= len(car):
                current_green -= len(car)
                current_passing -= len(car)
                cars_passed.append(car)
            elif current_green > 0 and len(car) <= current_passing:
                cars_passed.append(car)
                current_green = 0
                current_passing -= len(car)
            elif current_green > 0 and len(car) > current_passing:
                crash = True
                print("A crash happened!")
                print(f"{car} was hit at {car[-(len(car)-current_passing)]}.")
                break

    elif crash:
        break

    else:
        cars_queue.append(command)

if not crash:
    print("Everyone is safe.")
    print(f"{len(cars_passed)} total cars passed the crossroads.")

#71points
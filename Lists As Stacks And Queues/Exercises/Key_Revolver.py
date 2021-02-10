from collections import deque

price_of_each_bullet = int(input())
gun_capacity = int(input())
bullets = [int(el) for el in input().split()]
new_bullets = len(bullets)
locks = deque(int(el) for el in input().split())
value_of_intelligence = int(input())
bullet = False
lock = False

current_capacity = gun_capacity

while True:

    if not locks:
        lock = True
        break
    elif not bullets and locks:
        bullet = True
        break

    while current_capacity > 0:
        if not bullets or not locks:
            break
        current_bullet = bullets.pop()
        current_lock = locks[0]

        if current_bullet <= current_lock:
            print("Bang!")
            locks.popleft()
        else:
            print("Ping!")

        current_capacity -= 1

    if current_capacity < 1 and bullets:
        print("Reloading!")
    current_capacity = gun_capacity

money_earned = value_of_intelligence - (price_of_each_bullet * (new_bullets - len(bullets)))

if bullet:
    print(f"Couldn't get through. Locks left: {len(locks)}")
elif lock:
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")

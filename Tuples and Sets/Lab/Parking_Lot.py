n = int(input())
a = set()
for _ in range(n):
    command, number = input().split(', ')
    if command == 'IN':
        a.add(number)
    else:
        a.remove(number)
if len(a) == 0:
    print('Parking Lot is Empty')
else:
    for el in a:
        print(el)

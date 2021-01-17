number_of_guests = int(input())
a = set()
for _ in range(number_of_guests):
    res_num = input()
    a.add(res_num)

while True:
    command = input()
    if command == 'END':
        break
    elif command in a:
        a.remove(command)
vip = []
regular = []

for el in a:
    if el[0].isdigit():
        vip.append(el)
    else:
        regular.append(el)

print(len(a))
for e in sorted(vip):
    print(e)
for l in sorted(regular):
    print(l)

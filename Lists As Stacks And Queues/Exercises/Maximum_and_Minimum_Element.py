n = int(input())

s = []

for i in range(0, n):

    command = input().split()

    if command[0] == '1':
        s.append(int(command[1]))
    elif command[0] == '2':
        if s:
            s.pop()
    elif command[0] == '3':
        if s:
            print(max(s))
    elif command[0] == '4':
        if s:
            print(min(s))

s = list(map(str, s))
print(', '.join(s[::-1]))

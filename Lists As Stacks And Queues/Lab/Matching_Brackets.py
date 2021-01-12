data = input()

s = []

for i in range(len(data)):
    el = data[i]
    if el == '(':
        s.append(i)
    elif el == ')':
        j = s.pop()
        print(data[j:i + 1])

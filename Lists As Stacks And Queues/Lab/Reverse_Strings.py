string = input()

stack = []

for el in string:
    stack.append(el)

result = ''
while stack:
    result += stack.pop()

print(result)

brakets = list(input())
s = []

for braket in brakets:
    if braket == '{' or braket == '[' or braket == '(':
        s.append(braket)
    else:
        if s:
            if braket == '}' and s.pop() == '{':
                pass
            elif braket == ']' and s.pop() == '[':
                pass
            elif braket == ')' and s.pop() == '(':
                pass
            else:
                break
        else:
            print(f'NO')
            quit()

if not s:
    print(f'YES')
else:
    print(f'NO')
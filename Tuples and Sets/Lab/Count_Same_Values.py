tt = tuple(map(float, input().split()))

dic = {}
for el in tt:
    dic[el] = tt.count(el)

for key, value in dic.items():
    print(f'{key} - {value} times')

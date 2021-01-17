n = int(input())

dic = {}
asd = []
dsa = []

for i in range(n):
    data = input().split('-')

    a = data[0].split(',')
    dic[i] = list()
    for ch in range(int(a[0]), int(a[1])+1):
        asd.append(ch)
    dic[i].append(asd)
    b = data[1].split(',')
    for el in range(int(b[0]), int(b[1])+1):
        dsa.append(el)
    dic[i].append(dsa)
    asd = []
    dsa = []


new = {}

for key, value in dic.items():
    a = set(value[0])
    b = set(value[1])
    c = a & b
    new[key] = c
max_le = 0
for k, v in new.items():
    if len(v) > max_le:
        max_le = len(v)
        asd = []
        for elements in v:
            asd.append(elements)

#maxle = max(len(x) for x in asd)
print(f'Longest intersection is {asd} with length {max_le}')

#ad = list(map(str, v))
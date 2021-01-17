string = input()

dic = {}

for ch in string:
    dic[ch] = string.count(ch)

sorted_result = sorted(dic.items(), key=lambda x: x[0])

for el in sorted_result:
    print(f'{el[0]}: {el[1]} time/s')

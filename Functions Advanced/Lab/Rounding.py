def rounding(data):
    return [round(el) for el in data]


input_data = list(map(float, input().split()))
print(rounding(input_data))

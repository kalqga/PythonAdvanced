def absolute_values(data):
    return [abs(el) for el in data]


input_data = list(map(float, input().split()))

print(absolute_values(input_data))

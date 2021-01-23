numbers = [int(num) for num in input().split(', ')]

positive = [el for el in numbers if el >= 0]
negative = [el for el in numbers if el < 0]
even = [el for el in numbers if el % 2 == 0]
odd = [el for el in numbers if el % 2 == 1 or el == 1]

print("Positive:", ', '.join(map(str, positive)))
print("Negative:", ', '.join(map(str, negative)))
print("Even:", ', '.join(map(str, even)))
print("Odd:", ', '.join(map(str, odd)))

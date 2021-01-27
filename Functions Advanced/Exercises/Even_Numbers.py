def even(num):
    return list(filter(lambda x: x%2 == 0, num))


numbers = map(int, input().split())
print(even(numbers))

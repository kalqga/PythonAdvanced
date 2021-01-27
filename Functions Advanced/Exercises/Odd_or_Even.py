def sum_printing(command, nums):
    if command == 'Odd':
        a = sum(filter(lambda x: x % 2 != 0, nums))
        return a * len(nums)
    elif command == 'Even':
        a = sum(filter(lambda x: x % 2 == 0, nums))
        return a * len(nums)


com = input()
numbers = list(map(int, input().split()))
print(sum_printing(com, numbers))

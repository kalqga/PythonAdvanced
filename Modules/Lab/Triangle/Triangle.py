def print_triangle(n):
    nums = []
    for i in range(1, n + 1):
        nums.append(str(i))
        print(" ".join(nums))
    for i in range(n, 1, -1):
        nums.pop()
        print(" ".join(nums))
    return nums

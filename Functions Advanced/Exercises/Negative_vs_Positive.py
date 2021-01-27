def sum_negatives(num):
    return sum(filter(lambda x: x < 0, num))


def sum_positives(num):
    return sum(filter(lambda x: x > 0, num))


def stronger(num):
    print(sum_negatives(num))
    print(sum_positives(num))
    if sum_positives(num) > abs(sum_negatives(num)):
        return "The positives are stronger than the negatives"
    else:
        return "The negatives are stronger than the positives"


numbers = list(map(int, input().split()))

print(stronger(numbers))

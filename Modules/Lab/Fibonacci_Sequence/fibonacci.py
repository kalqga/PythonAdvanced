seq = [0, 1]


def create(count):
    global seq
    seq = [0, 1]
    if count == 0:
        return []
    elif count == 1:
        return [0, 1]
    else:
        for i in range(2, count):
            seq.append(seq[-1] + seq[-2])
    return seq


def locate(number):
    if number in seq:
        return f"The number - {number} is at index {seq.index(number)}"
    else:
        return f"The number - {number} is not in the sequence"



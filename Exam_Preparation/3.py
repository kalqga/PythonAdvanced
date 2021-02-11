def get_magic_triangle(n):
    triangle = [1]

    new = []

    for i in range(n):
        if i == 0:
            new.append(triangle)
        else:
            b = triangle.copy()
            b.insert(0, 0)
            b.append(0)
            d = []
            for j in range(0, len(b) - 1):
                d.append(b[j] + b[j + 1])
            new.append(d)
            triangle = d

    return new


get_magic_triangle(5)

def median(a: int, b: int, c: int) -> int:

    numbers = [a, b, c]

    numbers.sort()

    return numbers[1]


print(median(25, 11, 33))
print(median(1, 1, 2))


def median2(a: int, b: int, c: int) -> int:
    if a >= b >= c or c >= b >= a:
        return b
    elif b >= a >= c or c >= a >= b:
        return a
    else:
        return c


print(median2(25, 11, 33))
print(median2(1, 1, 2))

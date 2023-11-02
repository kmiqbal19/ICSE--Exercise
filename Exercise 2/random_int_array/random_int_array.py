import random


def create_random(n: int) -> list[int]:
    result = []
    for _ in range(n):
        result.append(random.randint(5, 99))
    return result


def to_string(a: list[int]) -> str:
    result = '['
    for i in range(len(a)):
        result += str(a[i])
        if i < len(a) - 1:
            result += ','
    result += ']'
    return result


def pos_min(a: list[int]) -> int:
    if not a:
        return -1
    min_val = a[0]
    min_val_index = 0
    for num in range(1, len(a)):
        if a[num] < min_val:
            min_val = a[num]
            min_val_index = num
    return min_val_index


def swap(a: list[int]) -> None:
    if len(a) < 2:
        return  
    a[0], a[-1] = a[-1], a[0]
    return 

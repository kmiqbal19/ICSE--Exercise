import random;

def create_random (n : int) -> list[int]:
    result = []
    for _ in range(n):
        result.append(random.randint(5, 99))
    return result
# create_random(5)

def to_string (a : list[int]) -> str:
    result = '['
    for i in range(len(a)):
        result += str(a[i])
        if i < len(a) - 1:
            result += ','
    result += ']'
    # print(type(result))
    return result
# print(to_string([1,2,3,4]))

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
# print(pos_min([3,5,7,2,3,56,2,6]) )       

def swap(a: list[int]) -> None:
    if len(a) < 2:
        return  
    a[0], a[-1] = a[-1], a[0]
# print(swap([1,2,3,4]))
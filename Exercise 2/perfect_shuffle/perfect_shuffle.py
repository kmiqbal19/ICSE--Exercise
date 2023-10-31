# Task 1
def interleave (a : list[int], b: list[int]) -> list[int]:
    if len(a) == 0 or len(b) == 0:
        return 'Not possible to suffle' 
    result = []
    for i in range(len(a)):
        result.append(a[i])
        result.append(b[i])
    return result
# print(interleave([1,2,3], [1,2,3]))

# Task 2
def perfect_shuffle (a : list[int]) -> list[int]:
    length_of_arr = len(a)
    divisor = length_of_arr // 2
    first_half = a[:divisor]
    second_half = a[divisor:]
    # print(first_half, second_half)
    return interleave(first_half, second_half)

# print(perfect_shuffle([1,2,3,4,1,2,3]))

def shuffle_number(n: int) -> int:
    if n % 2 != 0:
        raise ValueError("Input must be an even number")
    original_order = list(range(1, n + 1))
    current_order = list(original_order)
    num_shuffles = 0

    while True:
        num_shuffles += 1
        current_order = perfect_shuffle(current_order)

        if current_order == original_order:
            break

    return num_shuffles

# print(shuffle_number(52))
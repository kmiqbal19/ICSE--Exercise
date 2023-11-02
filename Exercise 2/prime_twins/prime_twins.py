def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False

    return True


def prime_twins(n: int) -> list[tuple[int, int]]:
    twin_pairs: list[tuple[int, int]] = []
    if n == 0:
        return []
    p = 2
    while len(twin_pairs) < n:
        if is_prime(p) and is_prime(p + 2):
            twin_pairs.append((p, p + 2))
        p += 1
    return twin_pairs

    
def prime_triplets(n: int) -> list[tuple[int, int, int]]:
    triplet_list: list[tuple[int, int, int]] = []
    if n == 0:
        return []
    p = 2  
    while len(triplet_list) < n:
        if is_prime(p):
            if is_prime(p + 2) and is_prime(p + 6):
                triplet_list.append((p, p + 2, p + 6))
            elif is_prime(p + 4) and is_prime(p + 6):
                triplet_list.append((p, p + 4, p + 6))
        p += 1
    return triplet_list

# print(prime_triplets(20))
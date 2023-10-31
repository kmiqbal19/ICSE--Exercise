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


def next_prime(n: int) -> int:
    if n <= 1:
        return 2 

    if is_prime(n):
        return n  

    if n % 2 == 0:
        n += 1  

    while True:
        if is_prime(n):
            return n
        n += 2  


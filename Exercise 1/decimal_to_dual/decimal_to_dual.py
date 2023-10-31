def transform_to_dual(dec: int) -> str:
    if dec <= 0:
        raise ValueError("Input must be a positive integer")

    binary_str = ""

    while dec > 0:
        binary_str = str(dec % 2) + binary_str
        dec //= 2

    return binary_str


print(transform_to_dual(13))  
print(transform_to_dual(7))   
print(transform_to_dual(10))  
from random import seed

seed(0)


def h2(x: int) -> int:
    return x << 5


class HashLinQuadDouble:
    def __init__(self, n: int) -> None:
        # Zero indicates an empty slot
        self.table = [0 for _ in range(n)]

    def _linear_probing(self, index, attempt):
        return (index + attempt) % len(self.table)

    def _quadratic_probing(self, index, attempt):
        return (index + attempt**2) % len(self.table)

    def _double_hashing(self, index, attempt, h2):
        return (index + attempt * h2) % len(self.table)

    def add_lin(self, obj: int) -> int:
        collisions = 0
        index = obj % len(self.table)
        attempt = 0
        while self.table[index] != 0:
            collisions += 1
            attempt += 1
            index = self._linear_probing(obj, attempt)
        self.table[index] = obj
        return collisions

    def add_quad(self, obj: int) -> int:
        collisions = 0
        index = obj % len(self.table)
        attempt = 0
        while self.table[index] != 0:
            collisions += 1
            attempt += 1
            index = self._quadratic_probing(obj, attempt)
        self.table[index] = obj
        return collisions

    def add_double_hashing(self, obj: int) -> int:
        collisions = 0
        index = obj % len(self.table)
        attempt = 0
        while self.table[index] != 0:
            collisions += 1
            attempt += 1
            index = self._double_hashing(obj, attempt, h2(obj))
        self.table[index] = obj
        return collisions


if __name__ == "__main__":
    n = 1249  # capacity of the hash table

    hash_table_lin = HashLinQuadDouble(n)
    hash_table_quad = HashLinQuadDouble(n)
    hash_table_double = HashLinQuadDouble(n)

    total_collisions_lin = 0
    total_collisions_quad = 0
    total_collisions_double = 0

    for num in range(1, 1001):  # generate 1000 random numbers (all > 0)
        total_collisions_lin += hash_table_lin.add_lin(num)
        total_collisions_quad += hash_table_quad.add_quad(num)
        total_collisions_double += hash_table_double.add_double_hashing(num)

    print("Linear Probing Collisions:", total_collisions_lin)
    print("Quadratic Probing Collisions:", total_collisions_quad)
    print("Double Hashing Collisions:", total_collisions_double)

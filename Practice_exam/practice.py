def binary_search (array: list[int] , find_value: int):
    def _find(a: list[int], x: int, left: int, right: int):
        if left > right:
            return -1
        middle_val : int = (left + right) // 2
        if a[middle_val] == x:
            return middle_val
        if a[middle_val] > x:
            return _find(a, x, left, middle_val + 1)
        else:
            return _find(a, x, middle_val - 1, right)
        
    return _find(array, find_value, 0, len(array) - 1)


def binary_search_iteration (array: list[int] , find_value: int):
    left, right = 0 , len(array) - 1
    while left <= right:
        mid_val = (left + right ) // 2
        if array[mid_val] == find_value:
           return mid_val
        if array[mid_val] > find_value:
            right = mid_val - 1
        else:
            left = mid_val + 1
    return -1

print(binary_search([2,5,8,9,36,45,89,98] , 36))
print(binary_search_iteration([2,5,8,9,36,45,89,98] , 89))
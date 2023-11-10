from typing import List


def selection_sort(array: List[int]) -> List[int]:
    """Sorts `array` with selectionsort inplace."""
    n = len(array)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if array[j] < array[min_idx]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
    return array


arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print("Sorted array:", arr)

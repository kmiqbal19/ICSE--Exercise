def quick_sort(array):
    _quick_sort(array, 0, len(array) - 1)


def _quick_sort(array, low, high):
    if low < high:
        # Partition the array and get the pivot index
        pivot_index = partition(array, low, high)

        # Recursively sort the subarrays
        _quick_sort(array, low, pivot_index - 1)
        _quick_sort(array, pivot_index + 1, high)


def partition(array, low, high):
    # Choose the rightmost element as the pivot
    pivot = array[high]

    # Initialize the index of the smaller element
    i = low - 1

    # Traverse the array and rearrange elements
    for j in range(low, high):
        if array[j] <= pivot:
            # Swap array[i] and array[j]
            i += 1
            array[i], array[j] = array[j], array[i]

    # Swap array[i+1] and the pivot
    array[i + 1], array[high] = array[high], array[i + 1]

    # Return the pivot index
    return i + 1


# Example usage:
my_array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
quick_sort(my_array)
print(my_array)

def merge_sort(array):
    if len(array) <= 1:
        return array

    # Divide: Split the array into two halves
    mid = len(array) // 2
    left_half = array[:mid]
    right_half = array[mid:]

    # Recursively apply merge_sort to each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge: Combine the sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    result = []
    i = j = 0

    # Merge the two halves in sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements from left and right (if any)
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Example usage:
original_array = [5, 3, 2, 7, 6, 9, 1, 8, 4, 10]
sorted_array = merge_sort(original_array.copy())
print("Original Array:", original_array)
print("Sorted Array:", sorted_array)

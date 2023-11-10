def bubble_sort(array: list) -> None:
    n = len(array)
    for i in range(n):
        # Flag to detect any swap during a pass
        swapped = False
        
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                # Swap if the element is greater than the next one
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        
        # If no two elements were swapped in the inner loop, the array is sorted
        if not swapped:
            break

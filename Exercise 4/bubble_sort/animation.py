import matplotlib.pyplot as plt
from bubble_sort import bubble_sort

def plot_bubble_sort(array):
    iterations = []

    for i in range(len(array)):
        iterations.append(array[:i + 1])
        bubble_sort(array[:i + 1])

    # Plotting the steps of bubble sort
    plt.figure(figsize=(10, 6))

    for i in range(len(iterations)):
        plt.subplot(121)
        plt.bar(range(len(iterations[i])), iterations[i])
        plt.title('Bubble Sort at Different Time Steps')

    plt.subplot(122)
    for i in range(len(iterations)):
        plt.cla()
        plt.bar(range(len(iterations[i])), iterations[i])
        plt.title('Bubble Sort Animation')
        plt.pause(0.1)

    plt.show()

arr = [64, 25, 12, 22, 11]
plot_bubble_sort(arr)

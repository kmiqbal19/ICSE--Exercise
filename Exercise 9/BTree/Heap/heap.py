from typing import TypeVar, List

T = TypeVar('T')


class MaxHeap:
    def __init__(self, arr: List[T]):
        self.heap = arr.copy()
        self.build_heap()

    def build_heap(self):
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self.sink(i)

    def get_heap(self) -> List[T]:
        return self.heap.copy()

    def __len__(self) -> int:
        return len(self.heap)

    def is_empty(self) -> bool:
        return len(self.heap) == 0

    def float(self, n: int):
        while n > 0 and self.heap[(n - 1) // 2] < self.heap[n]:
            self.heap[(n - 1) // 2], self.heap[n] = self.heap[n], self.heap[(n - 1) // 2]
            n = (n - 1) // 2

    def insert(self, obj: T):
        self.heap.append(obj)
        self.float(len(self.heap) - 1)

    def sink(self, n: int):
        size = len(self.heap)
        while 2 * n + 1 < size:
            child = 2 * n + 1
            if child + 1 < size and self.heap[child] < self.heap[child + 1]:
                child += 1
            if self.heap[n] < self.heap[child]:
                self.heap[n], self.heap[child] = self.heap[child], self.heap[n]
                n = child
            else:
                break

    def remove(self) -> T:
        if not self.is_empty():
            root = self.heap[0]
            self.heap[0] = self.heap[-1]
            self.heap.pop()
            self.sink(0)
            return root
        else:
            raise IndexError("Heap is empty")


initial_sequence = ['X', 'T', 'O', 'G', 'S', 'M', 'N', 'A', 'E', 'R', 'A', 'I']
max_heap = MaxHeap(initial_sequence)

print("Initial Max Heap:", max_heap.get_heap())
print("Length of Heap:", len(max_heap))
print("Is Heap Empty?", max_heap.is_empty())

max_heap.insert('U')
print("Max Heap after insertion:", max_heap.get_heap())

removed_element = max_heap.remove()
print("Removed Element:", removed_element)
print("Max Heap after removal:", max_heap.get_heap())

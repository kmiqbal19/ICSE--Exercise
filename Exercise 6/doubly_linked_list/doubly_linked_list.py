class DoublyLinkedNode:
    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self._head = DoublyLinkedNode()
        self._tail = DoublyLinkedNode()
        self._head.next = self._tail
        self._tail.prev = self._head

    def __len__(self):
        count = 0
        current = self._head.next
        while current != self._tail:
            count += 1
            current = current.next
        return count

    def is_empty(self):
        return len(self) == 0

    def add_first(self, item):
        new_node = DoublyLinkedNode(item, self._head, self._head.next)
        self._head.next.prev = new_node
        self._head.next = new_node

    def get_first(self):
        if self.is_empty():
            return None
        return self._head.next.value

    def remove_first(self):
        if self.is_empty():
            return None
        removed_value = self._head.next.value
        self._head.next = self._head.next.next
        self._head.next.prev = self._head
        return removed_value

    def add_last(self, item):
        new_node = DoublyLinkedNode(item, self._tail.prev, self._tail)
        self._tail.prev.next = new_node
        self._tail.prev = new_node

    def get_last(self):
        if self.is_empty():
            return None
        return self._tail.prev.value

    def remove_last(self):
        if self.is_empty():
            return None
        removed_value = self._tail.prev.value
        self._tail.prev = self._tail.prev.prev
        self._tail.prev.next = self._tail
        return removed_value

    def at(self, i):
        if i < 0 or i >= len(self):
            raise IndexError("Index out of range")
        current = self._head.next
        for _ in range(i):
            current = current.next
        return current.value

    def __str__(self):
        values = []
        current = self._head.next
        while current != self._tail:
            values.append(str(current.value))
            current = current.next
        return " <-> ".join(values)


# Test the DoublyLinkedList
dll = DoublyLinkedList()
dll.add_first(1)
dll.add_last(2)
dll.add_last(3)

print("Doubly Linked List:", dll)
print("Length:", len(dll))
print("Is empty?", dll.is_empty())
print("First element:", dll.get_first())
print("Last element:", dll.get_last())

dll.remove_first()
dll.remove_last()

print("After removals:", dll)
print("Length:", len(dll))

# Test indexing
print("Element at index 0:", dll.at(0))

# Update the test to check for the index before accessing it
if len(dll) > 1:
    print("Element at index 1:", dll.at(1))
else:
    print("Index 1 out of range, the list has less than 2 elements.")


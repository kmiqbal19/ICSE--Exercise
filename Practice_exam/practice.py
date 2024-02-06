# BINARY SEARCH WITH RECURSION


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

# BINARY SEARCH WITH ITERATION
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


'''
# IMPLEMENT LINKED_LIST DATA STRUCTURE


class Node:
    def __init__(self, data: str = None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data:str):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)
        return
    def prepend(self, data:str):
        new_head = Node(data)
        new_head.next = self.head
        self.head = new_head
    def delete(self, data: str):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current =self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
        return
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(elements)
        return elements
    
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(5)
ll.append(89)
ll.append(1000)
ll.append(158165)
ll.delete(5)
ll.prepend(888888)
ll.display()
'''

# IMPLEMENT LINKED LIST DATA STRUCTURE LIKE CLASS


class LinkedNode:
    def __init__(self, item: any =None, next: any= None):
        self._item = item
        self._next = next
    def get_item(self) -> any:
        return self._item
    def get_next(self) -> any:
        return self._next
    def set_item(self, item: any) -> None:
        self._item = item
    def set_next(self, next: Any) -> None:
        self._next = next


class LinkedList:
    def __init__(self):
        self._head = LinkedNode()
        self._tail = self._head
        self.size = 0
        
    def is_empty(self):
        return self.size == 0
    
    def get_first(self):
        if self.is_empty():
            return None
        else:
            return self._head.get_item()
    
    def get_last(self):
        if self.is_empty():
            return None
        else:
            return self._tail.get_item()
    def add_first(self, new_item):
        new_linked_node = LinkedNode(item=new_item, next=self._head)
        self._head= new_linked_node
        if self.is_empty():
            self._tail = self._head
        self.size += 1
    def remove_first(self):
        if self.is_empty():
            return None
        out = self._head.get_item()
        self._head = self._head.get_next()
        self.size -= 1
        if self.is_empty():
            self._tail = None
        return out
    def add_last(self, item:any):
        new_node = LinkedNode(item= item)
        if self.is_empty():
            self._head = new_node
        else:
            self._tail.set_next(new_node)
        self._tail = new_node
        self._size += 1









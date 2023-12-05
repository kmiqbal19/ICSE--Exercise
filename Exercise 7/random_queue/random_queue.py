import random


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def size(self):
        return len(self.items)


class RandomQueue(Queue):
    def sample(self):
        if not self.is_empty():
            return random.choice(self.items)


# Example usage:
random_queue = RandomQueue()


# Add items to the queue
random_queue.enqueue("item1")
random_queue.enqueue("item2")
random_queue.enqueue("item3")


# Check if the queue is empty
print(random_queue.is_empty())  # False


# Sample a random item from the queue
sampled_item = random_queue.sample()
print(f"Sampled Item: {sampled_item}")


# Dequeue an item from the queue
dequeued_item = random_queue.dequeue()
print(f"Dequeued Item: {dequeued_item}")


# Check the size of the queue
print(f"Queue Size: {random_queue.size()}")

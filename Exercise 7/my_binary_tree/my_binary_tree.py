from typing import List
from random import random, randint
from pprint import pprint

def sigmoid(x):
    return 1 / (1 + 2.71828 ** -x)

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def visualize(self):
        # Implementation for visualizing the tree (you can adapt this)
        pass

def tree_to_dict(tree):
    if not tree:
        return None
    return {
        'value': tree.value,
        'left': tree_to_dict(tree.left),
        'right': tree_to_dict(tree.right)
    }

class MyBinaryTree(BinaryTree):
    def __init__(self, value):
        super().__init__(value)

    def set_left(self, left_child):
        self.left = left_child

    def set_right(self, right_child):
        self.right = right_child

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_item(self):
        return self.value

    def height(self) -> int:
        if self is None:
            return 0
        left_height = self.left.height() if self.left else 0
        right_height = self.right.height() if self.right else 0
        return max(left_height, right_height) + 1

    def max_sum(self) -> int:
        def helper(node):
            if node is None:
                return 0, 0

            left_ending_here, left_overall = helper(node.left)
            right_ending_here, right_overall = helper(node.right)

            # Calculate the maximum sum ending at the current node
            max_ending_here = max(left_ending_here + node.value, right_ending_here + node.value, 0)

            # Calculate the maximum sum overall
            max_overall = max(left_overall, right_overall, max_ending_here)

            print(f"Node Value: {node.value}, Max Ending Here: {max_ending_here}, Max Overall: {max_overall}")

            return max_ending_here, max_overall

        _, max_sum_overall = helper(self)
        return max_sum_overall

    def max_path(self) -> int:
        def helper(node):
            if node is None:
                return 0
            left = helper(node.left)
            right = helper(node.right)
            return max(left, right) + node.value

        return helper(self)

    def max_width(self) -> int:
        if not self:
            return 0

        queue = [self]
        max_width = 1

        while queue:
            level_size = len(queue)
            max_width = max(max_width, level_size)

            for _ in range(level_size):
                node = queue.pop(0)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return max_width

def binary_tree_height(tree):
    if not tree:
        return 0

    left_height = binary_tree_height(tree.left)
    right_height = binary_tree_height(tree.right)

    return max(left_height, right_height) + 1

def binary_tree_max_sum(tree):
    if not tree:
        return 0

    left_sum = binary_tree_max_sum(tree.left)
    right_sum = binary_tree_max_sum(tree.right)

    return max(left_sum, right_sum) + tree.value

def generate(tree, probability, level):
    print(f"Level: {level}, Probability: {probability}")
    print("Tree structure before adding children:")
    pprint(tree_to_dict(tree), width=1, sort_dicts=False)

    if random() < probability * 2 * sigmoid(-level / 6):
        left = MyBinaryTree(randint(0, 100))
        tree.set_left(left)
        print("Tree structure after adding left child:")
        pprint(tree_to_dict(tree), width=1, sort_dicts=False)
        generate(tree.get_left(), probability, level + 1)

    if random() < probability * 2 * sigmoid(-level / 3):
        right = MyBinaryTree(randint(0, 100))
        tree.set_right(right)
        print("Tree structure after adding right child:")
        pprint(tree_to_dict(tree), width=1, sort_dicts=False)
        generate(tree.get_right(), probability, level + 1)

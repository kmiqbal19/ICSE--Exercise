# Tree Structures Q&A

## 1. What is a tree? Use the words: node, parent, child
A tree is a hierarchical data structure composed of nodes. Each node in a tree has a parent-child relationship with other nodes. A node with no parent is called the root, and nodes with no children are called leaf nodes.

## 2. What is a leaf node?
A leaf node is a node in a tree that has no children, i.e., it is a node without any descendants.

## 3. What is a root node?
The root node is the topmost node in a tree, and it has no parent. It serves as the starting point for traversing the tree.

## 4. What is the height of a tree?
The height of a tree is the length of the longest path from the root to a leaf. It represents the depth of the tree.

## 5. What is a path in a tree?
A path in a tree is a sequence of nodes where each adjacent pair in the sequence is connected by an edge. The path begins at a node and ends at another node.

## 6. What are common applications of trees?
Common applications of trees include representing hierarchical structures (file systems, organization charts), storing data for quick search and retrieval (binary search trees), expression parsing (expression trees), and network routing algorithms.

## 7. What is a binary tree?
A binary tree is a type of tree in which each node has at most two children, referred to as the left child and the right child.

## 8. What is a search tree?
A search tree is a binary tree data structure in which the nodes are arranged such that the left subtree of a node contains only nodes with values less than the node, and the right subtree contains only nodes with values greater than the node. It facilitates efficient search operations.

## 9. What is a balanced search tree?
A balanced search tree is a search tree in which the heights of the left and right subtrees of any node differ by at most one, ensuring that the tree remains balanced and maintains efficient search times.

## Traversal of the Given Tree:
      10
     / \
    /   \
   /     \
  5      15
 / \     /
2   9   13
   /   / \
  6   /   \
     12   14
## Preorder Traversal
10, 5, 2, 9, 6, 15, 13, 12, 14
## Inorder Traversal
2, 5, 6, 9, 10, 12, 13, 14, 15
## Postorder Traversal
2, 6, 9, 5, 12, 14, 13, 15, 10
## Level-order Traversal
10, 5, 15, 2, 9, 13, 6, 12, 14



      -8
     / \
    /   \
   /     \
  4      1
 / \     /  \
6   -1   5   7
/ \  / \  /\  /\
10   
/\
# Create a Tree Node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Create nodes
root = Node(19)
root.left = Node(34)
root.right = Node(51)
root.left.left = Node(78)
root.left.right = Node(87)


# Print the tree nodes
print("Root:", root.data)
print("Left child:", root.left.data)
print("Right child:", root.right.data)
print("Left child's left child:", root.left.left.data)
print("Left child's right child:", root.left.right.data)
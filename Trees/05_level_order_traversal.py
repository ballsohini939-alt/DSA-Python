from collections import deque
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Create the tree
root = Node(18)
root.left = Node(45)
root.right = Node(77)
root.left.left = Node(93)
root.left.right = Node(59)


# Level Order Traversal
queue = deque()
queue.append(root)
print("Level Order Traversal:")
while len(queue) > 0:
    current = queue.popleft()
    print(current.data)
    if current.left is not None:
        queue.append(current.left)
    if current.right is not None:
        queue.append(current.right)
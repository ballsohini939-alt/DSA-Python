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


# Preorder Traversal
# Root → Left → Right
def preorder(root):
    if root is None:
        return
    print(root.data)
    preorder(root.left)
    preorder(root.right)
print("Preorder Traversal:")
preorder(root)
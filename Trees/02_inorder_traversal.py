class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Create the tree
root = Node(15)
root.left = Node(27)
root.right = Node(57)
root.left.left = Node(76)
root.left.right = Node(81)
# Inorder Traversal
# Left → Root → Right
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data)
    inorder(root.right)
print("Inorder Traversal:")
inorder(root)
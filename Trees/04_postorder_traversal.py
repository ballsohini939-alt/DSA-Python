class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Create the tree
root = Node(18)
root.left = Node(91)
root.right = Node(37)
root.left.left = Node(72)
root.left.right = Node(50)


# Postorder Traversal
# Left → Right → Root
def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data)
print("Postorder Traversal:")
postorder(root)
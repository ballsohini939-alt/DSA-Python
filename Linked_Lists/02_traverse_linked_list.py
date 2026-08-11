# Create a Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create nodes
first = Node(12)
second = Node(32)
third = Node(89)
fourth = Node(58)


# Connect nodes
first.next = second
second.next = third
third.next = fourth


# Traverse the linked list
current = first
while current is not None:
    print(current.data)
    current = current.next
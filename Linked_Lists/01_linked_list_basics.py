# Create a Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create nodes
first = Node(18)
second = Node(67)
third = Node(30)


# Connect the nodes
first.next = second
second.next = third


# Print the nodes
print(first.data)
print(first.next.data)
print(first.next.next.data)
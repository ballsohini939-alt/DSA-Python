class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create the original list
first = Node(10)
second = Node(20)
third = Node(30)
first.next = second
second.next = third


# Insert at the beginning
new_node = Node(5)
new_node.next = first
first = new_node


# Insert at the end
last_node = Node(40)
current = first
while current.next is not None:
    current = current.next
current.next = last_node


# Print the linked list
current = first
while current is not None:
    print(current.data)
    current = current.next
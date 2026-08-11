class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create the linked list
first = Node(10)
second = Node(20)
third = Node(30)
fourth = Node(40)
first.next = second
second.next = third
third.next = fourth


# Value we want to delete
value = 30
# Delete the node
current = first
if current.data == value:
    first = current.next
else:
    while current.next is not None:
        if current.next.data == value:
            current.next = current.next.next
            break
        current = current.next


# Print the linked list
current = first
while current is not None:
    print(current.data)
    current = current.next
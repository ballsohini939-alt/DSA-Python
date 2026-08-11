class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create the linked list
first = Node(60)
second = Node(28)
third = Node(31)
fourth = Node(99)
first.next = second
second.next = third
third.next = fourth


# Value to search
value = 30
current = first
found = False
while current is not None:
    if current.data == value:
        found = True
        break
    current = current.next


# Display result
if found:
    print("Element found")
else:
    print("Element not found")
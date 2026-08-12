queue = []

# Enqueue elements
queue.append(12)
queue.append(34)
queue.append(76)
print("Queue:", queue)


# Dequeue the first element
removed = queue.pop(0)
print("Removed:", removed)
print("Queue after dequeue:", queue)


# Add another element
queue.append(98)
print("Final queue:", queue)
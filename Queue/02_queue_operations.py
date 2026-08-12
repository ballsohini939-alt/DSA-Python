queue = []

# Enqueue
queue.append(45)
queue.append(87)
queue.append(63)
print("Queue:", queue)


# Front
if len(queue) > 0:
    print("Front element:", queue[0])
else:
    print("Queue is empty")


# Rear
if len(queue) > 0:
    print("Rear element:", queue[-1])
else:
    print("Queue is empty")


# Dequeue
if len(queue) > 0:
    removed = queue.pop(0)
    print("Removed:", removed)

print("Queue after dequeue:", queue)


# Check if empty
if len(queue) == 0:
    print("Queue is empty")
else:
    print("Queue is not empty")
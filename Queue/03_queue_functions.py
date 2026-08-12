queue = []

# Enqueue an element
def enqueue(value):
    queue.append(value)
    print(value, "added to queue")


# Dequeue an element
def dequeue():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        removed = queue.pop(0)
        print(removed, "removed from queue")


# Show the front element
def front():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        print("Front element:", queue[0])


# Display the queue
def display():
    print("Queue:", queue)


# Use the functions
enqueue(33)
enqueue(76)
enqueue(91)
display()
front()
dequeue()
display()
front()
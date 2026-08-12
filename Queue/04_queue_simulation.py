queue = []

# People join the queue
queue.append("Person 1")
queue.append("Person 2")
queue.append("Person 3")
queue.append("Person 4")
print("People waiting:", queue)


# Serve people one by one
while len(queue) > 0:
    person = queue.pop(0)
    print("Serving:", person)
print("Queue is empty")
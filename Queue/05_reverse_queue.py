queue = [10, 20, 30, 40]
stack = []


# Move Queue elements into Stack
while len(queue) > 0:
    stack.append(queue.pop(0))


# Move Stack elements back into Queue
while len(stack) > 0:
    queue.append(stack.pop())
print("Reversed queue:", queue)
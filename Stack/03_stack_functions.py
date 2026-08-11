text = "SHARMISTHA"
stack = []


# Push an element
def push(value):
    stack.append(value)
    print(value, "added to stack")


# Pop an element
def pop_element():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        removed = stack.pop()
        print(removed, "removed from stack")


# Peek at the top element
def peek():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Top element:", stack[-1])


# Display the stack
def display():
    print("Stack:", stack)


# Use the functions
push(10)
push(20)
push(30)
display()
peek()
pop_element()
display()
peek()
text = "SHARMISTHA"
stack = []


# Push each character into the stack
for character in text:
    stack.append(character)


# Pop characters to create reversed string
reversed_text = ""
while len(stack) > 0:
    reversed_text = reversed_text + stack.pop()
print("Original string:", text)
print("Reversed string:", reversed_text)
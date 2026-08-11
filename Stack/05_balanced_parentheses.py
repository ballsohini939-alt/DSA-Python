text = "((()))"
stack = []
balanced = True
for character in text:
    if character == "(":
        stack.append(character)
    elif character == ")":
        if len(stack) == 0:
            balanced = False
            break
        stack.pop()
if len(stack) != 0:
    balanced = False
if balanced:
    print("Parentheses are balanced")
else:
    print("Parentheses are not balanced")
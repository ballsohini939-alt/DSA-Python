def is_palindrome(text, start, end):
    # Base case
    if start >= end:
        return True
    # If characters are different
    if text[start] != text[end]:
        return False
    # Check the remaining characters
    return is_palindrome(text, start + 1, end - 1)
text = "malayalam"
if is_palindrome(text, 0, len(text) - 1):
    print("Palindrome")
else:
    print("Not a palindrome")
# 1. Reverse a String
text = "Sohini"
reversed_text = ""
for character in text:
    reversed_text = character + reversed_text
print("Reversed string:", reversed_text)


# 2. Convert to Uppercase
text = "hello python"
print("Uppercase:", text.upper())


# 3. Convert to Lowercase
text = "HELLO PYTHON"
print("Lowercase:", text.lower())


# 4. Remove Spaces

text = "Hello Python World"
no_spaces = ""
for character in text:
    if character != " ":
        no_spaces = no_spaces + character
print("Without spaces:", no_spaces)


# 5. Count a Particular Character

text = "programming"
target = "m"
count = 0
for character in text:
    if character == target:
        count = count + 1
print("Frequency of", target, ":", count)


# 6. Check Palindrome

text = "racecar"
reversed_text = ""
for character in text:
    reversed_text = character + reversed_text
if text == reversed_text:
    print("Palindrome")
else:
    print("Not a palindrome")
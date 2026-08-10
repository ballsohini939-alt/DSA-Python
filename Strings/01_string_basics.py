# 1. Print a String
text = "Hello Python"
print("String:", text)


# 2. Find Length of String
print("Length:", len(text))


# 3. Print Each Character
for character in text:
    print(character)


# 4. Count Vowels
vowels = 0
for character in text.lower():
    if character in "aeiou":
        vowels = vowels + 1
print("Vowels:", vowels)


# 5. Count Consonants

consonants = 0
for character in text.lower():
    if character.isalpha() and character not in "aeiou":
        consonants = consonants + 1
print("Consonants:", consonants)


# 6. Count Spaces
spaces = 0
for character in text:
    if character == " ":
        spaces = spaces + 1
print("Spaces:", spaces)
# 1. Find Duplicate Characters
text = "programming"
duplicates = []
for character in text:
    if text.count(character) > 1 and character not in duplicates:
        duplicates.append(character)
print("Duplicate characters:", duplicates)


# 2. Find First Non-Repeating Character
text = "aabbcde"
for character in text:
    if text.count(character) == 1:
        print("First non-repeating character:", character)
        break
# 1. Count Frequency of Each Character
text = "banana"
characters = []
for character in text:
    if character not in characters:
        characters.append(character)
for character in characters:
    count = 0
    for letter in text:
        if letter == character:
            count = count + 1
    print(character, ":", count)


# 2. Find the Most Frequent Character
text = "Sohini"
most_frequent = ""
highest_count = 0
for character in text:
    count = 0
    for letter in text:
        if letter == character:
            count = count + 1
    if count > highest_count:
        highest_count = count
        most_frequent = character
print("Most frequent character:", most_frequent)
print("Frequency:", highest_count)
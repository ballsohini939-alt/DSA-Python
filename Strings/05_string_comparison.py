# 1. Compare Two Strings
text1 = "hello"
text2 = "hello"
if text1 == text2:
    print("Strings are equal")
else:
    print("Strings are not equal")


# 2. Check Anagram
text1 = "listen"
text2 = "silent"
if sorted(text1) == sorted(text2):
    print("Strings are anagrams")
else:
    print("Strings are not anagrams")


# 3. Count Words
sentence = "Python is easy to learn"
words = sentence.split()
print("Number of words:", len(words))


# 4. Find Longest Word
sentence = "Python programming is interesting"
words = sentence.split()
longest = words[0]
for word in words:
    if len(word) > len(longest):
        longest = word
print("Longest word:", longest)
numbers = [90, -5, 20, -8, 0, 15, -37]
positive = 0
negative = 0
for number in numbers:
    if number > 0:
        positive = positive + 1
    elif number < 0:
        negative = negative + 1
print("Positive numbers:", positive)
print("Negative numbers:", negative)
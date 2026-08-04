numbers = [13, 25, 87, 40, 15, 47, 12]
count = 0
for number in numbers:
    if number % 2 != 0:
        count = count + 1

print("Odd numbers:", count)

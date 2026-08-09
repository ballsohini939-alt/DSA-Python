numbers = [60, 20, 90, 30, 10, 20, 90, 40, 90]
target = 90
count = 0
for number in numbers:
    if number == target:
        count = count + 1
print("Frequency:", count)
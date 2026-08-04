numbers = [10, 25, 7, 95, 67, 8, 37]
count = 0
for number in numbers:
    if number % 2 == 0:
        count = count + 1

print("Even numbers:", count)
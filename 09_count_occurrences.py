numbers = [10, 20, 10, 30, 10, 40 , 89 , 97, 89]
target = 89
count = 0
for number in numbers:
    if number == target:
        count = count + 1
print(target, "occurs", count, "times")

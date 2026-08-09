# 1. Linear Search

numbers = [10, 25, 7, 40, 15]
target = 40
found = False
for number in numbers:
    if number == target:
        found = True
        break
if found:
    print("Element found")
else:
    print("Element not found")


# 2. Linear Search with Position
numbers = [30, 25, 97, 40, 75]
target = 40
position = -1
for i in range(len(numbers)):
    if numbers[i] == target:
        position = i
        break
if position != -1:
    print("Element found at index:", position)
else:
    print("Element not found")


# 3. First Repeating Element
numbers = [10, 30, 30, 20, 40, 10, 67, 99, 67]
seen = []
for number in numbers:
    if number in seen:
        print("First repeating element:", number)
        break
    else:
        seen.append(number)


# 4. First Non-Repeating Element
numbers = [10, 20, 30, 20, 40, 10]
for number in numbers:
    if numbers.count(number) == 1:
        print("First non-repeating element:", number)
        break


# 5. Missing Number
numbers = [1, 2, 3, 5]
n = 5
total = 0
for number in numbers:
    total = total + number
expected_sum = 0
for i in range(1, n + 1):
    expected_sum = expected_sum + i
missing = expected_sum - total
print("Missing number:", missing)
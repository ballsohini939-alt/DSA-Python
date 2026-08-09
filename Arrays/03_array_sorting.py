# 1. Bubble Sort
numbers = [5, 2, 8, 1, 3]
for i in range(len(numbers)):
    for j in range(len(numbers) - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
print("Bubble Sort:", numbers)


# 2. Selection Sort
numbers = [5, 2, 8, 1, 3]
for i in range(len(numbers)):
    smallest = i
    for j in range(i + 1, len(numbers)):
        if numbers[j] < numbers[smallest]:
            smallest = j
    numbers[i], numbers[smallest] = numbers[smallest], numbers[i]
print("Selection Sort:", numbers)


# 3. Insertion Sort
numbers = [5, 2, 8, 1, 3]
for i in range(1, len(numbers)):
    current = numbers[i]
    j = i - 1
    while j >= 0 and numbers[j] > current:
        numbers[j + 1] = numbers[j]
        j = j - 1
    numbers[j + 1] = current
print("Insertion Sort:", numbers)
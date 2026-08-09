# 1. Reverse an Array
numbers = [10, 20, 30, 40, 50]
reversed_array = []
for i in range(len(numbers) - 1, -1, -1):
    reversed_array.append(numbers[i])
print("Reversed array:", reversed_array)


# 2. Check if Array is Sorted
numbers = [17, 89, 78, 43, 51]
sorted_array = True
for i in range(len(numbers) - 1):
    if numbers[i] > numbers[i + 1]:
        sorted_array = False
        break
if sorted_array:
    print("Array is sorted")
else:
    print("Array is not sorted")


# 3. Find Duplicates

numbers = [16, 89, 78, 37, 89, 43, 16, 51]
duplicates = []
for number in numbers:
    if numbers.count(number) > 1 and number not in duplicates:
        duplicates.append(number)
print("Duplicate elements:", duplicates)


# 4. Remove Duplicates
numbers = [16, 89, 16, 30, 89, 40]
unique_numbers = []
for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)
print("Array after removing duplicates:", unique_numbers)


# 5. Move Zeros to the End
numbers = [0, 5, 0, 3, 8, 0, 2]
non_zero = []
zero_count = 0
for number in numbers:
    if number == 0:
        zero_count = zero_count + 1
    else:
        non_zero.append(number)
for i in range(zero_count):
    non_zero.append(0)
print("Zeros moved to end:", non_zero)


# 6. Rotate Array to the Right
numbers = [1, 2, 3, 4, 5]
last = numbers[-1]
for i in range(len(numbers) - 1, 0, -1):
    numbers[i] = numbers[i - 1]
numbers[0] = last
print("Rotated array:", numbers)
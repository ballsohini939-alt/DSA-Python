numbers = [13, 28, 79, 40, 15, 6, -5, 13, 28, 90, 15, 6, -5, 13]

# 1. Find the Largest Number
largest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number
print("Largest number:", largest)


# 2. Find the Smallest Number
smallest = numbers[0]
for number in numbers:
    if number < smallest:
        smallest = number
print("Smallest number:", smallest)


# 3. Find the Sum of Array
total = 0
for number in numbers:
    total = total + number
print("Sum:", total)


# 4. Count Even Numbers
even_count = 0
for number in numbers:
    if number % 2 == 0:
        even_count = even_count + 1
print("Even numbers:", even_count)


# 5. Count Odd Numbers
odd_count = 0
for number in numbers:
    if number % 2 != 0:
        odd_count = odd_count + 1
print("Odd numbers:", odd_count)


# 6. Find Average
average = total / len(numbers)
print("Average:", average)


# 7. Find Maximum Difference
difference = largest - smallest
print("Maximum difference:", difference)


# 8. Find Second Largest
largest = numbers[0]
second_largest = numbers[0]
for number in numbers:
    if number > largest:
        second_largest = largest
        largest = number
    elif number > second_largest and number != largest:
        second_largest = number
print("Second largest:", second_largest)


# 9. Find Second Smallest
smallest = numbers[0]
second_smallest = numbers[0]
for number in numbers:
    if number < smallest:
        second_smallest = smallest
        smallest = number
    elif number < second_smallest and number != smallest:
        second_smallest = number
print("Second smallest:", second_smallest)


# 10. Count Positive and Negative Numbers
positive = 0
negative = 0
for number in numbers:
    if number > 0:
        positive = positive + 1
    elif number < 0:
        negative = negative + 1
print("Positive numbers:", positive)
print("Negative numbers:", negative)


# 11. Find Frequency of an Element
target = 13
count = 0
for number in numbers:
    if number == target:
        count = count + 1
print("Frequency of", target, ":", count)
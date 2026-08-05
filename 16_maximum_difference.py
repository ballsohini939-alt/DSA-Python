numbers = [10, 25, 7, 80, 15]
largest = numbers[0]
smallest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number
    if number < smallest:
        smallest = number
difference = largest - smallest

print("Maximum difference:", difference)
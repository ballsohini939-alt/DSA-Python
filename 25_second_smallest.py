numbers = [19, 25, 97, 40, 75]
smallest = numbers[0]
second = numbers[0]
for number in numbers:
    if number < smallest:
        second = smallest
        smallest = number
    elif number < second and number != smallest:
        second = number
print("Second smallest:", second)
numbers = [14, 25, 87, 40, 55]
largest = numbers[0]
second = numbers[0]
for number in numbers:
    if number > largest:
        second = largest
        largest = number
    elif number > second and number != largest:
        second = number
print("Second largest:", second)
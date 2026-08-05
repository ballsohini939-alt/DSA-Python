numbers = [0, 17, 0, 20, 30 , 93]
position = 0
for i in range(len(numbers)):
    if numbers[i] != 0:
        numbers[position], numbers[i] = numbers[i], numbers[position]
        position = position + 1

print("Array after moving zeros:", numbers)
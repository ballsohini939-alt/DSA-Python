numbers = [30, 25, 97, 40, 75]
target = 75
position = -1
for i in range(len(numbers)):
    if numbers[i] == target:
        position = i
        break
if position != -1:
    print("Element found at index:", position)
else:
    print("Element not found")
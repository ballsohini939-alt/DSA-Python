numbers = [30, 20, 10, 50, 40]
sorted = True
for i in range(len(numbers) - 1):
    if numbers[i] > numbers[i + 1]:
        sorted = False
if sorted:
    print("Array is sorted")
else:
    print("Array is not sorted")
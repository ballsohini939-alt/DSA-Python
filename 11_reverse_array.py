numbers = [10, 2, 37, 61, 53]
left = 0
right = len(numbers) - 1
while left < right:
    numbers[left], numbers[right] = numbers[right], numbers[left]
    left = left + 1
    right = right - 1
print("Reversed array:", numbers)
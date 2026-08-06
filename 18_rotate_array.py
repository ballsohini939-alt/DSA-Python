numbers = [10, 20, 30, 40, 50]
last = numbers[-1]
numbers.remove(last)
numbers.insert(0, last)
print("Rotated array:", numbers)
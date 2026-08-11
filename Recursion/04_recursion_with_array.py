# 1. Print Array Elements Using Recursion
def print_array(numbers, index):
    if index == len(numbers):
        return
    print(numbers[index])
    print_array(numbers, index + 1)
numbers = [10, 20, 30, 40, 50]
print("Array elements:")
print_array(numbers, 0)


# 2. Find Sum of Array Using Recursion
def array_sum(numbers, index):
    if index == len(numbers):
        return 0
    return numbers[index] + array_sum(numbers, index + 1)
print("Array sum:", array_sum(numbers, 0))


# 3. Find Largest Element Using Recursion
def find_largest(numbers, index):
    if index == len(numbers) - 1:
        return numbers[index]
    largest = find_largest(numbers, index + 1)
    if numbers[index] > largest:
        return numbers[index]
    else:
        return largest
print("Largest element:", find_largest(numbers, 0))
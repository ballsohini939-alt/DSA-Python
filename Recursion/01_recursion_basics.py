# 1. Print numbers from 5 to 1
def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)
countdown(5)


# 2. Print numbers from 1 to 5
def print_numbers(n):
    if n == 0:
        return
    print_numbers(n - 1)
    print(n)
print_numbers(5)


# 3. Find Sum of Numbers from 1 to N
def find_sum(n):
    if n == 0:
        return 0
    return n + find_sum(n - 1)
print("Sum:", find_sum(5))


# 4. Find Factorial

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
print("Factorial:", factorial(5))
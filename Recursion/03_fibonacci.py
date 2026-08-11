def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
# Print first 7 Fibonacci numbers
for i in range(7):
    print(fibonacci(i), end=" ")
# 1. Find Power of a Number
def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)
print("Power:", power(25, 3))


# 2. Find Sum of Digits
def digit_sum(n):
    if n == 0:
        return 0
    return (n % 10) + digit_sum(n // 10)
print("Sum of digits:", digit_sum(1937))


# 3. Reverse a Number
def reverse_number(n, reversed_number=0):
    if n == 0:
        return reversed_number
    digit = n % 10
    reversed_number = reversed_number * 10 + digit
    return reverse_number(n // 10, reversed_number)
print("Reversed number:", reverse_number(9378))
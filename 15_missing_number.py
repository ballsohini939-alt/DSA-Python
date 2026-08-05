numbers = [81, 82, 84, 85]
total = 0
for number in numbers:
    total = total + number
expected_sum = 0
for i in range(81, 86):
    expected_sum = expected_sum + i
missing = expected_sum - total
print("Missing number:", missing)
numbers = [10, 20, 35, 20, 41, 11 , 99 , 35]
unique = []
for number in numbers:
    if number not in unique:
        unique.append(number)
print("Array without duplicates:", unique)
numbers = [10, 20, 35, 20, 41, 11 , 99 , 35]
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            print("Duplicate:", numbers[i])
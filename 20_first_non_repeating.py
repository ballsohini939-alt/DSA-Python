numbers = [19, 21, 30, 2, 40, 19, 67, 99, 67]
for number in numbers:
    if numbers.count(number) == 1:
        print("First non-repeating element:", number)
        break
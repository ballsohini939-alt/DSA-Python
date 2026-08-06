numbers = [10, 30, 30, 20, 40, 10, 67, 99, 67]
seen = []
for number in numbers:
    if number in seen:
        print("First repeating element:", number)
        break
    else:
        seen.append(number)
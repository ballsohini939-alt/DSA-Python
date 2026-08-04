numbers = [10, 25, 7, 40, 15]

target = 40

found = False

for number in numbers:
    if number == target:
        found = True
        break

if found:
    print("Element found")
else:
    print("Element not found")
    
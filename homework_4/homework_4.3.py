with open("file_with_numbers.txt", "r") as file:
    numbers = list(map(float, file.read().split()))

square_number = []

for number in numbers:
    square_number.append(number ** 2)

with open("file_with_numbers.txt", "w") as file:
    for number in square_number:
        file.write(str(number) + " ")
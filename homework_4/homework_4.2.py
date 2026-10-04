with open("file_with_numbers.txt", "r") as file:
    numbers = list(map(int, file.read().split()))

even_numbers = []
odd_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

with open("even.txt", "w") as file:
    for number in even_numbers:
        file.write(str(number) + " ")

with open("odd.txt", "w") as file:
    for number in odd_numbers:
        file.write(str(number) + " ")
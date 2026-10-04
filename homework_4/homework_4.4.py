with open("even.txt", "rb") as file:
    file1 = file.read()

with open("odd.txt", "rb") as file:
    file2 = file.read()

print(f"Содержимое even.txt до замены: {file1}")
print(f"Содержимое odd.txt до замены: {file2}")

with open("even.txt", "wb") as file:
    file.write(file2)

with open("odd.txt", "wb") as file:
    file.write(file1)

print(f"Содержимое even.txt после замены: {file2}")
print(f"Содержимое odd.txt после замены: {file1}")

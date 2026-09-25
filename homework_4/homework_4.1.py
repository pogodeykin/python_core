with open("file_with_numbers.txt", "r") as file:
    numbers = file.read().split()

if len(numbers) < 3:
    print("Ошибка: в файле меньше трёх чисел")
else:
    print(f'Первый элемент файла:{numbers[0]}')
    print(f'Второй элемент файла:{numbers[1]}')
    print(f'Предпоследний элемент файла:{numbers[-2]}')
    print(f'Последний элемент файла:{numbers[-1]}')

secret_number = 37
attempts = 0
while True:
        current_number = int(input("Введите число: "))
        attempts += 1
        if current_number < secret_number:
            print(f"Введённое число {current_number} меньше секретного")
        elif current_number > secret_number:
            print(f"Введённое число {current_number} больше секретного")
        else:
            print(f"Вы угадали! Количество попыток: {attempts}")
            break

import test_data


def main():
    count = int(input("Введите количество тестовых пользователей: "))

    if count < 0:
        print("Количество пользователей не может быть отрицательным.")
        return

    users = []
    for i in range(count):
        user = test_data.generate_user()
        users.append(user)

    print("\nСписок тестовых пользователей:")

    for user in users:
        print(user)

    statistics = {
        "ACTIVE": 0,
        "BLOCKED": 0,
        "INACTIVE": 0
    }

    for user in users:
        statistics[user["status"]] += 1

    print("\nСтатистика по статусам:")

    for status, amount in statistics.items():
        print(f"{status}: {amount}")


main()

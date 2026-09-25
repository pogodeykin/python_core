import random

tests = [
    "test_login",
    "test_logout",
    "test_registration",
    "test_profile",
    "test_payment",
    "test_search"
]
statuses = ["PASS", "FAIL", "SKIP"]
count = int(input("Введите количество запускаемых тестов: "))
if count < 0:
    print("Ошибка: количество тестов не может быть отрицательным.")

elif count == 0:
    print("Ошибка: необходимо выбрать хотя бы один тест.")

elif count > len(tests):
    print("Ошибка: запрошено больше тестов, чем есть в списке.")
else:
    selected_tests = random.sample(tests, count)

    report = []

    for test in selected_tests:
        status = random.choice(statuses)
        report.append(f"{test}: {status}")

    print("\nОтчёт о запуске тестов:")

    for result in report:
        print(result)

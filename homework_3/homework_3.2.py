test_cases = ["Login", "Registration", "Checkout", "Logout"]
statuses = ["PASS", "FAIL", "PASS", "SKIP"]


def print_report(test_cases, statuses):
    success_tests = 0
    failure_tests = 0
    skips_tests = 0

    for test_case, status in zip(test_cases, statuses):
        print(f"{test_case} — {status}")

        if status == "PASS":
            success_tests += 1
        elif status == "FAIL":
            failure_tests += 1
        elif status == "SKIP":
            skips_tests += 1

    print(f"Успешных тестов: {success_tests}")
    print(f"Неуспешных тестов: {failure_tests}")
    print(f"Пропущено тестов: {skips_tests}")

    if failure_tests > 0:
        print("Тестовый запуск неуспешный")
    else:
        print("Тестовый запуск успешный")


print_report(test_cases, statuses)

from functools import reduce

tests = [
    {"name": "test_login", "status": "PASS", "time": 1.2},
    {"name": "test_logout", "status": "FAIL", "time": 0.8},
    {"name": "test_registration", "status": "PASS", "time": 2.1},
    {"name": "test_payment", "status": "SKIP", "time": 0.0},
    {"name": "test_search", "status": "FAIL", "time": 1.5},
]

status_counts = {
    "PASS": sum(test["status"] == "PASS" for test in tests),
    "FAIL": sum(test["status"] == "FAIL" for test in tests),
    "SKIP": sum(test["status"] == "SKIP" for test in tests),
}

failed_tests = filter(
    lambda test: test["status"] == "FAIL",
    tests
)

failed_names = list(
    map(lambda test: test["name"], failed_tests)
)

passed_names = [
    test["name"]
    for test in tests
    if test["status"] == "PASS"
]

total_time = reduce(
    lambda total, test: total + test["time"],
    tests,
    0
)

print("Количество тестов:")
print(f"PASS: {status_counts['PASS']}")
print(f"FAIL: {status_counts['FAIL']}")
print(f"SKIP: {status_counts['SKIP']}")

print("\nНазвания упавших тестов:")
print(failed_names)

print("\nНазвания успешно пройденных тестов:")
print(passed_names)

print(f"\nОбщее время выполнения: {total_time:.1f} секунд")

def get_test_statistics(results):
    statistics = {
        "PASS": 0,
        "FAIL": 0,
        "SKIP": 0
    }

    for result in results:
        if result in statistics:
            statistics[result] += 1

    return statistics


results = input('Введите результаты тестов в одну строку:').upper().split()

statistics = get_test_statistics(results)
count_tests = len(results)

if count_tests > 0:
    success_percent = statistics["PASS"] / count_tests * 100
else:
    success_percent = 0

print(f"Всего тестов: {count_tests}")
print(f"PASS: {statistics['PASS']}")
print(f"FAIL: {statistics['FAIL']}")
print(f"SKIP: {statistics['SKIP']}")
print(f"Успешно: {success_percent}%")

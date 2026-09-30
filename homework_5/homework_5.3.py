def run_test(retry_count, timeout):
    if not 0 <= retry_count <= 5:
        raise ValueError("Количество повторных запусков должно быть в диапазоне от 0 до 5")

    if timeout <= 0:
        raise ValueError("Таймаут должен быть положительным числом")

    print(
        f"Тест запущен: повторных запусков — {retry_count}, "
        f"таймаут — {timeout} секунд"
    )


test_data = [
    (3, 10),
    (2, -5),
    (7, 10)
]

for retry_count, timeout in test_data:
    try:
        run_test(retry_count, timeout)
    except ValueError as error:
        print(f"Ошибка: {error}")

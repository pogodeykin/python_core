class InvalidTestStatusError(Exception):
    pass


def check_test_status(status):
    statuses = {"PASS", "FAIL", "SKIP"}

    if status not in statuses:
        raise InvalidTestStatusError(
            f"Некорректный статус теста: {status}"
        )

    return f"Статус {status} допустим"


test_statuses = ["PASS", "FAIL", "SKIP", "ACTIVE", "DENIED"]

for status in test_statuses:
    try:
        result = check_test_status(status)
        print(result)
    except InvalidTestStatusError as error:
        print(f"Ошибка: {error}")

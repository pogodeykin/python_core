import json
from functools import reduce

INPUT_FILE = "tests.json"
OUTPUT_FILE = "report.json"

VALID_STATUSES = {"PASS", "FAIL", "SKIP"}


def load_tests(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)

    except FileNotFoundError:
        raise ValueError(f"Файл '{filename}' не найден")

    except json.JSONDecodeError:
        raise ValueError(
            f"Файл '{filename}' содержит некорректный JSON"
        )

    if isinstance(data, dict):
        data = data.get("tests")

    if not isinstance(data, list):
        raise ValueError(
            "Неправильная структура данных: "
            "ожидается список тестов"
        )

    for number, test in enumerate(data, start=1):

        if not isinstance(test, dict):
            raise ValueError(
                f"Тест №{number} должен быть объектом"
            )

        required_fields = {"name", "status", "time"}
        missing_fields = required_fields - set(test.keys())

        if missing_fields:
            raise ValueError(
                f"В тесте №{number} отсутствуют поля: "
                f"{', '.join(missing_fields)}"
            )

        if not isinstance(test["name"], str):
            raise ValueError(
                f"Поле 'name' в тесте №{number} "
                "должно быть строкой"
            )

        if test["status"] not in VALID_STATUSES:
            raise ValueError(
                f"Некорректный статус в тесте №{number}: "
                f"{test['status']}. "
                f"Допустимые значения: {VALID_STATUSES}"
            )

        if (
                not isinstance(test["time"], (int, float))
                or isinstance(test["time"], bool)
                or test["time"] < 0
        ):
            raise ValueError(
                f"Поле 'time' в тесте №{number} "
                "должно быть неотрицательным числом"
            )

    return data


def create_report(tests):
    # lambda и filter().

    failed_tests = list(
        filter(
            lambda test: test["status"] == "FAIL",
            tests
        )
    )

    passed_tests = list(
        filter(
            lambda test: test["status"] == "PASS",
            tests
        )
    )

    skipped_tests = list(
        filter(
            lambda test: test["status"] == "SKIP",
            tests
        )
    )

    total_time = reduce(
        lambda total, test: total + test["time"],
        tests,
        0
    )

    longest_test = max(
        tests,
        key=lambda test: test["time"],
        default=None
    )

    report = {
        "total_tests": len(tests),

        "status_counts": {
            "PASS": len(passed_tests),
            "FAIL": len(failed_tests),
            "SKIP": len(skipped_tests)
        },

        "failed_tests": [
            test["name"]
            for test in failed_tests
        ],

        "longest_test": (
            {
                "name": longest_test["name"],
                "status": longest_test["status"],
                "time": longest_test["time"]
            }
            if longest_test is not None
            else None
        ),

        "total_time": round(total_time, 3)
    }

    return report


def save_report(report, filename):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(
                report,
                file,
                ensure_ascii=False,
                indent=4
            )

    except OSError as error:
        raise ValueError(
            f"Не удалось сохранить отчёт: {error}"
        )


def main():
    try:
        tests = load_tests(INPUT_FILE)
        report = create_report(tests)
        save_report(report, OUTPUT_FILE)

        print(
            f"Отчёт успешно сохранён в файл '{OUTPUT_FILE}'"
        )

    except ValueError as error:
        print(f"Ошибка: {error}")


if __name__ == "__main__":
    main()

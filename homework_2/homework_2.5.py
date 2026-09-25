count = int(input('Введите количество автотестов: '))
attempts = 0
PASSED = 0
FAILED = 0
SKIPPED = 0
for _ in range(count):
    status = input('Введите результат теста(PASS,FAIL,SKIP): ').strip().upper()
    if status == 'PASS':
        PASSED += 1
    elif status == 'FAIL':
        FAILED += 1
    elif status == 'SKIP':
        SKIPPED += 1
    else:
        continue
print("PASS:", PASSED, "\nFAIL:", FAILED, "\nSKIP:", SKIPPED)
if FAILED > 0:
    print("Обнаружены упавшие тесты")
else:
    print("Все пройденные тесты успешно выполнены")

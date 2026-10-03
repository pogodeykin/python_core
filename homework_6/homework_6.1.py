def count_pass_with_recours(results):
    if not results:
        return 0

    first = 1 if results[0] == "PASS" else 0
    return first + count_pass_with_recours(results[1:])


tests = ["PASS", "FAIL", "SKIP", "PASS", "PASS", "FAIL", "FAIL", "SKIP", "PASS", "PASS", "FAIL"]

print(count_pass_with_recours(tests))

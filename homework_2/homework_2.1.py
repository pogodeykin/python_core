for i in range(1, 31):  # последовательность от 1 до 30,правая граница range не включается
    if (i % 5 == 0 | i % 3 == 0):
        print("BugTest")
    elif (i % 5 == 0):
        print("Test")
    elif (i % 3 == 0):
        print("Bug")
    else:
        print(i)

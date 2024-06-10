def fibonacci(control):
    number1 = 0
    number2 = 1
    for _ in range(control):
        series = number1 + number2
        number2 = number1
        number1 = series


print(fibonacci(11))

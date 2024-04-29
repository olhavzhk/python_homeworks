def make_operation(arithmetic_operator, *numbers):
    for number in numbers:
        if not isinstance(number, (int, float)):
            print("Please provide only numbers.")
            return None
    result = 0
    if arithmetic_operator == '+':
        result = sum(numbers)
    elif arithmetic_operator == '-':
        result = numbers[0] - sum(numbers[1:])
    elif arithmetic_operator == '*':
        result = 1
        for i in numbers:
            result *= i
    else:
        print("Invalid operator. Please use '+', '-', or '*'.")
    return result


operation_result = make_operation('*', 1, 3, 4)
print(operation_result)

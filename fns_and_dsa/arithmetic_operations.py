##Author: Fiyin
## this script, define a function that performs
## basic arithmetic operations. This function, 
## perform_operation such as addition, subtraction
## multiplication and division


def perform_operation(num1, num2, operation):
    result = 0
    match operation:
        case "add":
            result = num1 + num2
            print(f"Result: {result}")
        case "subtract":
            result = num1 - num2
            print(f"Result: {result}")
        case "multiply":
            result = num1 * num2
            print(f"Result: {result}")
        case "divide":
            if num1 == 0:
                print("Cannot divide by zero")
            elif num2 == 0:
                print("Cannot divide by zero")
            else:
                result = num1 / num2
                print(f"Result: {result}")

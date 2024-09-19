##Author: Fiyinfolu
##This calculator will prompt the user to enter two numbers and
#  select an operation (addition, subtraction, multiplication, or division).
#  The script will then perform the selected operation using a Match Case 
# statement and display the result

num1 = int(input("Enter the first number:"))

num2 = int(input("Enter the second number:"))

operation = str(input("Choose the operation (+, -, *, /):"))

match operation:
    case "+":
        sum = num1 + num2
        print(f"The result is {sum}")
    case "-":
        subtract = num1 - num2
        print(f"The result is {subtract}")
    case "*":
        multiply = num1 * num2
        print(f"The result is {multiply}")
    case "/":
        if num2 == 0:
            print("Cannot divide by zero")
        else: 
            divide = num1 / num2
            print(f"The result is {divide}")
    case _:
        print("Wrong input, please try again")


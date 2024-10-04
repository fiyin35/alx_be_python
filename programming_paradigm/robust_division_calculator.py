## Author: Fiyinfolu
##


def safe_divide(numerator, denominator):
    try:
        divide = float(numerator) / float(denominator)
        print(f"The result of the division is {divide}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return ""
    except ValueError:
        print("Error: Please enter numeric values only.")
        return ""
    except Exception as e:
        print(e)
        return ""
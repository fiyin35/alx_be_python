# Author: Fiyinfolu
# This script will define functions to convert temperatures
# between Celsius and Fahrenheit, demonstrating the use of 
# global variables to store conversion factors that are 
# accessible within functions.
# convert_to_celsius accept temperature in fahrenheit and convert to celsius
# convert_to_fahrenheit accept temperature in celsius and convert to fahrenheit
# main function prompt the user to enter the temperature to convert and select whether
# is in celsius or fahrenheit



FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    celsius = (float(fahrenheit) - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius


def convert_to_fahrenheit(celsius):
    fahrenheit = float(celsius) * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return fahrenheit

def main():
    temp = input("Enter the temperature to convert: ")
    temp_format = input("Is this temperature in Celsius or Fahrenheit? (C/F):").capitalize()
    match temp_format:
        case "C":
            if temp.isdigit() == False:
                print("Invalid temperature. Please enter a numeric value.")
            else:
                celsius_tempt = convert_to_fahrenheit(temp)
                print(f"{temp}°{temp_format} is {celsius_tempt}°F")   
        case "F":
            if temp.isdigit() == False:
                print("Invalid temperature. Please enter a numeric value.")
            else:
                fahrenheit_tempt = convert_to_celsius(temp)
                print(f"{temp}°{temp_format} is {fahrenheit_tempt}°C")
        case _:
            print("Please enter a valid input, Celsius or Fahrenheit? (C/F)")

if __name__ == '__main__':
    main()

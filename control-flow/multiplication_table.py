##Author: Fiyinfolu
## This script will ask the user to enter a number, 
## then use a for loop to print the multiplication
## table for that number from 1 to 10.

number = int(input("Enter a number to see its multiplication table"))
result = 0
for item in range(1, 11):
    result = number * item
    print(f"{number} * {item} = {result}")



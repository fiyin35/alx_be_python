## Author: fiyinfolu
## accept input from the user
## use the input to calculate the
## projected savings and print it
monthly_income = int(input("Enter your monthly income:"))
monthly_expenses = int(input("Enter your total monthly expenses:"))
interest_rate = 0.05
annual = 12

monthly_savings = monthly_income - monthly_expenses
print(f"Your monthly savings are ${monthly_savings}.")

projected_savings = monthly_savings * annual + (monthly_savings * interest_rate)
print(f"Projected savings after one year, with interest, is: ${projected_savings}")
# Author: Fiyinfolu
# A python script to display the current date and time
# in this format “YYYY-MM-DD HH:MM:SS”
# the variable current_date holds the current date and time
# while display_current_datetime function formatted it to display “YYYY-MM-DD HH:MM:SS”
# calculate_future_date function prompt user to enter the number of days
# to add to the current date and display the future date

from datetime import datetime, timedelta

current_date = datetime.now()

def display_current_datetime():
    return current_date.strftime("%Y-%m-%d %H:%M:%S")

current_datetime = display_current_datetime()
print(f"Current date and time: {current_datetime}")


def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = current_date + timedelta(days=number_of_days)
    return future_date.strftime("%Y-%m-%d")

display_future_date = calculate_future_date()
print(f"Future date: {display_future_date}")

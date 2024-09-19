## Author: Fiyinfolu
## a simplified Python script 
## that uses conditional statements,
## Match Case, and loops to remind 
## the user about a single, priority
## task for the day based on time 
## sensitivity.

task = input("Enter your task:")

time_bound = input("Is it time-bound? (Yes/No):").lower()

priority = input("Priority (high/medium/low):").lower()


match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: {task} is a {priority} priority task that requires immediate attention today")
        elif time_bound == "no":
             print(f"Reminder: {task} is a {priority} priority task that requires your attention as soon as possible")
    case "medium":
        if time_bound == True:
            print(f"Attention: {task} is a {priority} priority task that requires your attention today")
        elif time_bound == "no":
            print(f"Attention: {task} is a {priority} priority task that requires your attention")
    case "low":
        if time_bound == True:
            print(f"Note: {task} is a {priority} priority task that requires your attention today, consider completing it as soon as you're free")
        elif time_bound == "no":
            print(f"Note: {task} is a {priority} priority task. Consider completing it when you have free time.")
    case _:
        print("Wrong input")
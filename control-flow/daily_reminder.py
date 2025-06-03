# A script that remind users about a single, priority task for the day based on time sensitivity

task = input("Enter your task:").title()
time_bound = input("Is it time-bound? (yes/no):").lower()
priority = input("Priority (high/medium/low):").lower()

# A match statement to send a customized remider based on the priority level
match priority:
    case "high":
        print(f"Reminder: {task} is a {priority} priority task", end="")
    case "medium":
        print(f"Reminder: {task} is a medium priority task", end="")
    case "low":
        print(f"Reminder: {task} is a low priority task", end="")
    case _:
        print("Invalid priority level entered")

# An if/else statement to modify the reminder based on if it's timebound or not
if time_bound == "yes":
    print(f" that requires immediate attention today!")
elif time_bound == "no":
   print(". Consider completing it when you have free time.")
else:
    print("Invalid input for time-bound")

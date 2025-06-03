# A script that remind users about a single, priority task for the day based on time sensitivity

task = input("Enter your task:").title()
time_bound = input("Is it time-bound? (yes/no):").lower()
priority = input("Priority (high/medium/low):").lower()

match priority:
    case "high":
        reminder = f"Reminder: {task} is a {priority} priority task"
    case "medium":
        reminder = f"Reminder: {task} is a medium priority task"
    case "low":
        reminder = f"Reminder: {task} is a low priority task"
    case _:
        print("Invalid priority level entered")

if time_bound == "yes":
    reminder += "that requires immediate attention today"
elif time_bound == "no":
    reminder += ". Consider completing it when you have free time."
else:
    print("Invalid input for time-bound")

print(reminder)



# print(f"{task} {reminder}{time_reminder}")
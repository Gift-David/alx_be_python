# A script that remind users about a single, priority task for the day based on time sensitivity

task = input("Enter your task description: ").lower()
priority = input("Task's priority (high, medium, low): ").lower()
time_bound = input("Is it time-bound? (yes or no): ").lower()

match priority:
    case "high":
        reminder ="is a high priority task"
    case "medium":
        reminder ="is a medium priority task"
    case "low":
        reminder ="is a low priority task"
    case _:
        print("Invalid priority level entered")

if time_bound == "yes":
    time_reminder = "that requires immediate attention today"
elif time_bound == "no":
    time_reminder = ". Consider completing it when you have free time."
else:
    print("Invalid input for time-bound")

print(f"{task} {reminder}{time_reminder}")
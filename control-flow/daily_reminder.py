# 
task = str(input("Enter yout task: ")).lower()
priority = str(input("Priority (high/medium/low): ")).lower()
time_bound = str(input("Is it time-bound? (yes/no: ")).lower()

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
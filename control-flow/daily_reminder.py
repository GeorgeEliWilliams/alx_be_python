# daily_reminder.py

# Prompt for user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Build the base reminder message using match-case
match priority:
    case "high":
        base_msg = f"'{task}' is a high priority task"
    case "medium":
        base_msg = f"'{task}' is a medium priority task"
    case "low":
        base_msg = f"'{task}' is a low priority task"
    case _:
        base_msg = f"'{task}' has an unspecified priority level"

# Add time sensitivity info and format the final reminder
if time_bound == "yes":
    final_msg = f"Reminder: {base_msg} that requires immediate attention today!"
else:
    final_msg = f"Note: {base_msg}. Consider completing it when you have free time."

# Loop: print reminder and ask if user wants to see it again
while True:
    print("\n" + final_msg)
    repeat = input("Would you like to see the reminder again? (yes/no): ").lower()
    if repeat != "yes":
        break

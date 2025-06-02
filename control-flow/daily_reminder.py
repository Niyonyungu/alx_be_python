# daily_reminder.py

# Get user inputs
task = input("Enter your task for today: ")
priority = input("What is the priority level? (high/medium/low): ").lower()
time_bound = input("Is this task time-bound? (yes/no): ").lower()

# Customized reminder based on priority and time sensitivity
match priority:
    case "high":
        message = f"🔴 HIGH PRIORITY: Don't forget to {task}."
    case "medium":
        message = f"🟠 MEDIUM PRIORITY: Try to complete {task} today."
    case "low":
        message = f"🟢 LOW PRIORITY: You can do {task} when you have free time."
    case _:
        message = f"⚠️ Unknown priority level for the task: {task}."

# Add urgency if the task is time-bound
if time_bound == "yes":
    message += " This task requires immediate attention today!"

# Print the final reminder
print("\n🔔 Daily Reminder 🔔")
print(message)
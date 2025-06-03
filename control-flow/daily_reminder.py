# daily_reminder.py

# Get user inputs
Task = input("Enter your task: ")
Priority = input("Priority (high/medium/low): ").lower()
Time_Bound = input("Is it time-bound? (yes/no): ").lower()

# Customized reminder based on Priority and time sensitivity
match Priority:
    case "high":
        message = f"HIGH Priority: Don't forget to {Task}."
    case "medium":
        message = f"MEDIUM Priority: Try to complete {Task} today."
    case "low":
        message = f"LOW Priority: You can do {Task} when you have free time."
    case _:
        message = f"Unknown Priority level for the Task: {Task}."

# Add urgency if the Task is time-bound
if Time_Bound == "yes":
    message += " This Task requires immediate attention today!"

# Print the final reminder
print("\n🔔 Daily Reminder 🔔")
print(f"Reminder: {message}")
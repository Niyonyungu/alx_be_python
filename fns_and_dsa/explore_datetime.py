
from datetime import datetime, timedelta

def display_current_datetime():
    """Function to display the current date and time"""
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date

def calculate_future_date():
    """Function to calculate a future date based on user input"""
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days)
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"Date after {days} days will be: {formatted_future_date}")
        return future_date
    except ValueError:
        print("Please enter a valid integer for the number of days.")
        return None

if __name__ == "__main__":
    # Part 1: Display current date and time
    display_current_datetime()
    
    # Part 2: Calculate future date
    calculate_future_date()
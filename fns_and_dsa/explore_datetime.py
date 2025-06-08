# explore_datetime.py

from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

# Part 2: Calculate a Future Date
def calculate_future_date():
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        future_date = datetime.now() + timedelta(days=days)
        print("Future date:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Run the functions
display_current_datetime()
calculate_future_date()

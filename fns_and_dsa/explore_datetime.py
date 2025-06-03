# 
from datetime import datetime
from datetime import timedelta

def display_current_datetime():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(current_date)

def calculate_future_date():
    number_of_days = int(input("Enter a number of days: "))
    future_date = datetime.now() + timedelta(days=number_of_days)
    print(future_date)

display_current_datetime()
calculate_future_date()
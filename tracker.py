import csv
import os
from datetime import datetime, timedelta
from tkinter import ttk, messagebox

def week_start():
    """Function to get the 5 day working week that monitors are available and can be booked for
    ,Should reset at to a new week at 18:00 on the last day of the week."""
    current_time = current_time or datetime.now()
    monday = current_time - timedelta(days=current_time.weekday())
    
    # If it's Friday (weekday == 4) and past 18:00, advance to next week
    if current_time.weekday() == 4 and current_time.time() >= datetime.strptime("18:00", "%H:%M").time():
        monday += timedelta(days=7)

    return monday.date()

def get_csv_as_dict(file_path):
    with open(file_path, newline='') as f:
        return list(csv.DictReader(f))

def create_bookings():
    if not os.path.exists("bookings.csv"):
        return []
    bookings = []
    with open("bookings.csv", newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['booking_time'] = datetime.strptime(row['booking_time'], "%Y-%m-%d %H:%M")
            row['week_start'] = datetime.strptime(row['week_start'], "%Y-%m-%d").date()
            bookings.append(row)
    return bookings

def booking_allowed():
    pass

def save_booking():
    pass

def update_today_booking():
    pass

def booking():
    pass

def search_monitor():
    pass
 
    
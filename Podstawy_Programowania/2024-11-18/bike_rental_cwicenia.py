import json
from datetime import datetime
import os
import smtplib

# DIR STRUCTURE
DATA_DIR = "data"
RENTALS_FILE = f"{DATA_DIR}/rentals.json"
DAILY_REPORT_DIR = f"{DATA_DIR}/daily_reports"
Price_Per_Time = 10
Price_After_Time = 5

def calculate_cost(rental_duration:int)->int:
    '''Calculate the cost of bike rental'''
    if rental_duration <= 1:
        return Price_Per_Time
    return Price_Per_Time + (rental_duration - 1) * Price_After_Time

def save_rental(rental):
    rentals = load_json(RENTALS_FILE)
    rentals.append(rental)
    save_json(RENTALS_FILE, rentals)
    print(f"Rental for {rental['customer_name']} has been saved.")

def save_json(file_path, data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4) #indent is number of space (wcięcia)

def rent_bike(customer_name, rental_duration):
    rentals = load_json(RENTALS_FILE)
    start_time = datetime.now().isoformat()
    rental = {
        "customer_name": customer_name,
        "start_time": start_time,
        "rental_duration": rental_duration  # Duration in minutes
    }
    rentals.append(rental)
    save_json(RENTALS_FILE, rentals)
    print(f"Rental started for {customer_name} at {start_time}, duration: {rental_duration} minutes.")


def ensure_directory_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def load_json(file_path)->list:
    ''' Load all rentals from rentals json'''   

    if not os.path.exists(file_path):
        # If the file doesn't exist, return an empty list
        return []
    
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, ValueError):
        # If the file is empty or contains invalid JSON, return an empty list
        print(f"Warning: {file_path} is empty or contains invalid JSON. Returning an empty list.")
        return []

def cancel_rental(customer_name:str):
    rentals = load_json(RENTALS_FILE)
    update = [(r for r in rentals if r["customer_name"] != customer_name)]
    
    if len(rentals) == len(update):
        print(f"No rental found for {customer_name}")
        return
    
    with open(RENTALS_FILE, "w") as file:
        json.dumb(update, file, indent=4)
        print(f"Rental to {customer_name} has been canceled.")


def load_rentals():
    rentals = load_json(RENTALS_FILE)
    return rentals


def send_rental_invoice_email(customer_email, rental_details):
    # This is a placeholder. To actually send an email, we need to configure an SMTP server.
    print(f"Sending invoice email to {customer_email} for the rental details:")
    print(f"Rental Details: {rental_details}")


def generate_daily_report():
    ensure_directory_exists(DAILY_REPORT_DIR)
    
    today = datetime.now().date() # .date() for time without hours.
    report_file = f"{DAILY_REPORT_DIR}/daily_report_{today}.json"
    
    rentals = load_rentals()
    daily_report = [rental for rental in rentals if rental["start_time"].startswith(str(today))]
    
    if not daily_report:
        print("No rentals found for today.")
        return
    
    save_json(report_file, daily_report)
    print(f"Daily report for {today} has been generated.")
    
    for rental in daily_report:
        rental_duration = rental["rental_duration"]
        cost = calculate_cost(rental_duration)
        print(f"Customer: {rental['customer_name']}, Duration: {rental_duration} minutes, Cost: ${cost}")


def main():
    ensure_directory_exists(DATA_DIR)
    ensure_directory_exists(DAILY_REPORT_DIR)

    while True:
        print("\n--- Bike Rental System ---")
        print("1. Rent a Bike")
        print("2. Cancel a Rental")
        print("3. Generate Daily Report")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            customer_name = input("Enter customer name: ")
            rental_duration = int(input("Enter rental duration (in minutes): "))
            rent_bike(customer_name, rental_duration)
        elif choice == "2":
            customer_name = input("Enter customer name: ")
            cancel_rental(customer_name)
        elif choice == "3":
            generate_daily_report()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

---

# **Documentation for Bike Rental System**
## **Introduction**
The Bike Rental System is a Python-based program designed to manage bike rentals efficiently. It supports functions such as:
- Renting a bike.
- Canceling a rental.
- Generating daily reports of rentals.
- Calculating rental costs based on duration.

The program uses JSON files for storing rental data and ensures directories and files are properly initialized. It also includes a placeholder for sending rental invoices via email.

---

## **Setup**
To set up the Bike Rental System, please follow the [Installation and Environment Setup Guide](../installation_and_setup_eng.md).  
This guide contains detailed instructions for installing Python and setting up a virtual environment.

---

## **Program Structure**

### **1. File and Directory Management**
- **Data Directory (`data`)**: Stores the program's JSON files.
  - `rentals.json`: Maintains rental information.
  - `daily_reports/`: Contains daily rental reports.
  
### **2. JSON Utilities**
#### **`load_json(file_path)`**
- Reads data from a JSON file.
- If the file is missing or invalid, returns an empty list.

#### **`save_json(file_path, data)`**
- Writes data to a JSON file in a structured format.

#### **`ensure_directory_exists(directory)`**
- Ensures the specified directory exists. If it does not, it creates the directory.

---

### **3. Rental Functions**

#### **`rent_bike(customer_name, rental_duration)`**
- Starts a rental for a customer.
- Adds the rental details (name, start time, duration) to `rentals.json`.

#### **`cancel_rental(customer_name)`**
- Cancels an active rental for the specified customer by removing their record from `rentals.json`.

#### **`calculate_cost(rental_duration)`**
- Calculates the cost of a rental based on the time:
  - **First hour**: $10.
  - **Additional hours**: $5/hour.

---

### **4. Reporting Functions**

#### **`generate_daily_report()`**
- Generates a JSON report of all rentals for the current day.
- Outputs the report to `daily_reports/daily_report_<date>.json`.

#### **`send_rental_invoice_email(customer_email, rental_details)`**
- Placeholder for sending invoices via email. 
- Prints the invoice details to the console.

---

## **Program Usage**

### **Running the Program**
1. Save the code to a file, e.g., `bike_rental.py`.
2. Run the program:
    ```bash
    python bike_rental.py
    ```

### **Menu Options**
1. **Rent a Bike**
    - Input customer name and rental duration.
2. **Cancel a Rental**
    - Remove a rental by specifying the customer name.
3. **Generate Daily Report**
    - Outputs the day's rentals and their costs.
4. **Exit**
    - Quits the program.

---

## **JSON File Structure**
### `rentals.json`
```json
[
    {
        "customer_name": "John Doe",
        "start_time": "2024-12-29T12:00:00",
        "rental_duration": 2
    },
    ...
]
```

### Daily Report Example (`daily_report_<date>.json`)
```json
[
    {
        "customer_name": "John Doe",
        "start_time": "2024-12-29T12:00:00",
        "rental_duration": 2
    }
]
```

---

## **Best Practices**
1. Use a **virtual environment** to manage dependencies.
2. Ensure directories (`data`, `daily_reports`) exist by running the program once.
3. Avoid modifying JSON files manually to prevent corruption.
4. Use valid customer names (avoid special characters).

---

## **Future Enhancements**
1. Integrate an email service for sending invoices.
2. Add a GUI for better user experience.
3. Implement error handling for invalid inputs.

---

## **Authors**
- [Stani1999](https://github.com/Stani1999)

---

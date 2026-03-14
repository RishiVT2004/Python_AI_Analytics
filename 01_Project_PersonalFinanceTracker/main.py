# this file is used to organize flow of the project

# matplotlib -> visualizes graph (Will be used later for plotting)
# pandas -> easily categorizes and searches data in csv


import pandas as pd
import csv
from datetime import datetime # helps to handle dates easily (converting strings to date objects)
from data_entry_user import get_amount, get_category, get_date, get_description

# We use a Class to group all functions and variables related to our CSV file together.
class CSV: 
    # Class attributes: These act as global settings for the class.
    CSV_FILE = "finance_data.csv"
    Columns = ["date", "amount", "category", "description"]
    date_format = "%d-%m-%Y"

    @classmethod # @classmethod means this function belongs to the class itself, not a specific object.
    def initialize_csv(data): 
        """Checks if our data file exists. If it doesn't, it creates a new empty one with headers."""
        try:    
            # Try to read the file. If it exists, great! We do nothing and move on.
            pd.read_csv(data.CSV_FILE)
        except FileNotFoundError: 
            # If pandas throws a FileNotFoundError, it means we need to create the file.
            # We create an empty pandas DataFrame (a 2D table) using our column names.
            df = pd.DataFrame(columns=data.Columns)
            # Save this empty table to our computer as a CSV. index=False means we don't save row numbers.
            df.to_csv(data.CSV_FILE, index=False)
            
    @classmethod
    def add_entry(data, date, amount, category, description): 
        """Takes the user's input and saves it as a new row in the CSV file."""
        # Package the individual pieces of data into a single Python dictionary.
        new_entry = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        } 
        
        # 'with open' is a safe way to handle files. It automatically closes the file when we are done.
        # "a" stands for 'append'. It adds new data to the bottom without erasing the old data.
        with open(data.CSV_FILE, "a", newline="") as csv_file:
            # DictWriter looks at our dictionary keys and matches them to the CSV columns.
            csv_writer = csv.DictWriter(csv_file, fieldnames=data.Columns)
            csv_writer.writerow(new_entry) # Writes the actual row to the file.
        print("Entry Added Successfully")
        
    @classmethod
    def get_transaction(data, start_dt, end_dt):
        """Searches for transactions between two dates, prints them, and calculates Profit/Loss."""
        # Load the whole CSV into a pandas DataFrame (makes it easy to search and filter)
        df = pd.read_csv(data.CSV_FILE)
        
        # Right now, dates are just text. We tell pandas to convert that text into actual 'datetime' objects.
        df["date"] = pd.to_datetime(df["date"], format=CSV.date_format)
        
        # We also convert the text the user typed in (start_dt and end_dt) into 'datetime' objects.
        start_dt = datetime.strptime(start_dt, CSV.date_format)
        end_dt = datetime.strptime(end_dt, CSV.date_format)
            
        # A 'mask' is a filter. It checks every row: "Is the date >= start AND <= end?"
        mask = (df["date"] >= start_dt) & (df["date"] <= end_dt)
        # Apply the filter. Now 'filtered_df' only holds the rows that passed the test.
        filtered_df = df.loc[mask]
            
        # Check if our filtered table is completely empty (no transactions found)
        if filtered_df.empty: 
            print(f"No Transactions between {start_dt} -- {end_dt}")
        else: 
            print(f"Transactions between {start_dt} -- {end_dt} are : \n")
            
            # Print the table. We use a 'formatter' to convert the dates back to readable text formats.
            print(f"{filtered_df.to_string(index=False, formatters={'date': lambda x: x.strftime(CSV.date_format)})}\n")
                
            # Filter the table AGAIN to find only Expenses ("E"), then add up the 'amount' column.
            total_expense = filtered_df[filtered_df["category"] == "E"]["amount"].sum()
            # Do the same for Income ("I").
            total_income = filtered_df[filtered_df["category"] == "I"]["amount"].sum()
            
            # Display a summary formatted to 2 decimal places (e.g., 150.50).
            print(f"Summary\nTotal Expense : {total_expense:.2f}\nTotal Income : {total_income:.2f}\nP&L : {total_income-total_expense:.2f}")
                
            return filtered_df # Returns this data so we can eventually plot a graph with it
            
def add_data():
    """A helper function to gather user input and send it to our CSV class."""
    # Ensure the file exists before we try adding anything to it
    CSV.initialize_csv()
    
    # Prompt the user for their transaction details using functions from data_entry_user.py
    date = get_date("Enter date of transaction, or just enter for today's data : ", allow_default=True)
    amnt = get_amount()
    cat = get_category()
    desc = get_description()
    
    # Send all those collected inputs to our add_entry function
    CSV.add_entry(date, amnt, cat, desc)

def main(): 
    """The main menu loop of the program. Keeps running until the user decides to exit."""
    # 'while True:' creates an infinite loop. It keeps asking the user what they want to do.
    while True: 
        print("\n1. Add a new Transaction\n2. Find Transaction Summary Between a date range\n3. Exit")
        choice = int(input("Enter your choice (1-3) : "))
        
        # Branching logic based on user input
        if choice == 1: 
            add_data()
            
        elif choice == 2: 
            start_date = get_date("Enter Start Date (dd-mm-yyyy) : ")
            end_date = get_date("Enter End Date (dd-mm-yyyy) : ")
            df = CSV.get_transaction(start_date, end_date)
            
        elif choice == 3: 
            print("Exiting the Program...")
            break # 'break' shatters the 'while True' loop, finally letting the program end.
            
        else: 
            print("Invalid Request...Try Again")
            
# --- THIS IS THE ENTRY POINT OF THE SCRIPT ---
# This special if-statement checks if you are running this specific file directly.
# If you run `python main.py`, __name__ becomes "__main__", and it runs main().
# If you import this file into another project, __name__ will be "main", and it WON'T run main() automatically.
if __name__ == "__main__": 
    main()

'''    
# Old testing code, commented out because our main() loop handles this dynamically now!
CSV.get_transaction("01-01-2026","10-01-2026")
add_data()
'''
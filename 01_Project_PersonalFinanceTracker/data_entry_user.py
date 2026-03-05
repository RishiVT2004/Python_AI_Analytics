# This file acts as an input and validation layer for the program.
# It collects data from the user (date, amount, category, description)
# and ensures the values are valid before returning them to the main program.

from datetime import datetime

# Standard date format used throughout the program.
date_format = "%d-%m-%Y"
# Allowed transaction categories.
Categories = ["I","E"]


# ---------------------------------------------------------------
# get_date()
#
# Purpose:
# Ask the user for a date and validate that it matches the required
# format (dd-mm-yyyy).
#
# Parameters:
# date_prompt  -> The message shown to the user when asking for the date.
# allow_default -> Controls whether the user can skip entering a date.
#
# Behavior:
# - If allow_default is True and the user presses Enter without typing
#   anything, the function automatically returns today's date.
# - If the user enters a date, the function checks whether it matches
#   the format defined in date_format.
# - datetime.strptime() converts the string input into a datetime object
#   to verify that the format is correct.
# - If the format is invalid, an error message is shown and the function
#   calls itself again to ask for the date until a valid one is entered.
#
# Return:
# A valid date string in dd-mm-yyyy format.
# ---------------------------------------------------------------
def get_date(date_prompt,allow_default=False) : 
    date_string = input(date_prompt)

    if allow_default and not date_string : 
        return datetime.today().strftime(date_format)
        # strftime converts a datetime object → formatted string

    try : 
        # strptime converts the input string → datetime object
        # If the string doesn't match the expected format,
        # Python raises a ValueError.
        valid_date = datetime.strptime(date_string,date_format)
    except :
        print("invalid date format!!! , ender in dd-mm-yyyy form")
        return get_date(date_prompt,allow_default)
    


# ---------------------------------------------------------------
# get_amount()
#
# Purpose:
# Ask the user for a transaction amount and ensure it is valid.
#
# Behavior:
# - Takes input from the user and converts it into a float.
# - Ensures the amount is greater than 0.
# - If the user enters a non-numeric value or a negative/zero amount,
#   a ValueError is raised.
# - When an error occurs, the function prints the error message
#   and asks the user again (using recursion).
#
# Return:
# A valid positive float value representing the transaction amount.
# ---------------------------------------------------------------
def get_amount() :
    try : 
        amnt = float(input("Enter the amount : "))
        if amnt <= 0 : 
            raise ValueError("Amount can't be 0 or negetive")
        return amnt
    except ValueError as E :
        print(E)
        return get_amount()
    

def get_category() : 
    category = input("Enter Transaction Category : \n'I' for Income\n'E' for Expense\n").upper()
    if category in Categories : 
        return category

    print("Invalid Category")
    return get_category()


def get_description() : 
    desc = input("Enter a Description : ")
    return desc
# this file acts as a file which collects data from user and validates it 

from datetime import datetime
date_format = "%d-%m-%Y"
Categories = ["I","E"]
# date_prompt is what user input, reason is that we my have dates in various different places we may ask date for a different reason
# allow_default : The allow_default flag is a safety switch. It’s useful if there are times in your program where a date is mandatory and other times where it’s optional.
# When allow_default = True , The user can skip entering a date, When allow_default = False,The user must enter a date.
def get_date(date_prompt,allow_default=False) : 
    date_string = input(date_prompt)

    if allow_default and not date_string : 
        return datetime.today().strftime(date_format)
        # strftime converts a date object → formatted string
    '''
    strptime is opposit of strftime,It converts the input string → date object.(stored in valid_date)
    if valid_date is correct format we continue or else flow goes to except block
    '''
    try : 
        valid_date = datetime.strptime(date_string,date_format)
    except :
        print("invalid date format!!! , ender in dd-mm-yyyy form")
        return get_date(date_prompt,allow_default)
    
        
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
    category = input("Enter Transaction Category : \n'I' for Income\n'E' for Expense").upper()
    if category in Categories : 
        return category

    print("Invalid Category")
    return get_category()

def get_description() : 
    desc = input("Enter a Description")
    return desc
# this file is used to organize flow of the project

# matplotlib -> visualizes graph 
# pandas -> easily categories and searches data in csv


import pandas as pd
import csv
from datetime import datetime # helps to handle dates
from data_entry_user import get_amount,get_category,get_date,get_description

class CSV : 
    CSV_FILE = "finance_data.csv"
    Columns = ["date","amount","category","description"]
    
    @classmethod # has access to the class but not any instance of class
    def initialize_csv(data) : 
        try:    
            pd.read_csv(data.CSV_FILE)
        except FileNotFoundError : 
            df = pd.DataFrame(columns=data.Columns)
            # df is a dataframe , an object in panda which is used to access different row/column from a csv
            df.to_csv(data.CSV_FILE,index=False)
            "uses the data object to save the csv file in the environment , index = False means no sorting"
            
    @classmethod
    def add_entry(data,date,amount,category,description) : 
        new_entry = {
            "date" : date,
            "amount" : amount,
            "category" : category,
            "description" : description
        } # python dictionary to write into csv file 
        
        # here we open the CSV_FILE as variable csv_file , "a" means we are appending to the very end of csv file 
        # newline = "" means we don't want to add a new line character at the end of file
        with open(data.CSV_FILE,"a",newline="") as csv_file :
            csv_writer = csv.DictWriter(csv_file,fieldnames=data.Columns)
            csv_writer.writerow(new_entry)
        print("Entry Added Successfully")
        
        @classmethod
        def get_transaction_range(data,start_dt,end_dt):
            df = pd.read_csv(data.CSV_FILE)
            
            
def add_data():
    CSV.initialize_csv()
    date = get_date("Enter date of transaction , or just enter for today's data : ",allow_default=True)
    amnt = get_amount()
    cat = get_category()
    desc = get_description()
    CSV.add_entry(date,amnt,cat,desc)
    
add_data()
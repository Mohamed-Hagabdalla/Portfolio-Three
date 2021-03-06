# Entire structure of the code obtained from the Source code, accompanied by Code Institute walkthrough videos

import gspread
from google.oauth2.service_account import Credentials

# SCOPE lists the APIs the program should access in order to run
# SCOPE variable value will not change so it is known as a constant
# constant variables are written in capitals in Python
# easier for developers to identify variables that shouldn't be changed
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('phone_shop')

def get_sales_data():
    """
    Get sales figures input from the user.
    Run a wile loop to collect a valid string of data from the user
    via the terminal, which must be a string of 6 numbers, seperated by commas.
    This loop will keep requesting data until the data is valid.
    """
    while True:
        print("Enter sales data from the last market.")
        print("Data should be six numbers, seperated by commas.")
        print("Example: 1,2,3,4,5,6\n")  # '\n' =  extra line of space   

        data_string = input("Enter your data here:\n")
        
        #split breaks up data at the commas
        #split returns broken up values as a list
        sales_data = data_string.split(",") 
        validate_data(sales_data)

        if validate_data(sales_data):
            print("Data is valid!")
            break

    return sales_data


def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True

# Both functions below have been refactored to update_worksheet()
def update_sales_worksheet(data):
    """
    Update sales worksheet, add new row with the list data provided.
    """
    print("Updating sales worksheet...\n")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print("Sales worksheet updated successfully.\n")


def update_surplus_worksheet(data):
    """
    Update surplus worksheet, add new row with the list data provided.
    """
    print("Updating surplus worksheet...\n")
    surplus_worksheet = SHEET.worksheet("surplus")
    surplus_worksheet.append_row(data)
    print("Surplus worksheet updated successfully.\n")


def update_worksheet(data, worksheet):
    """
    Receives a list of integers to be inserted into a worksheet
    Update the relevant worksheet with the data provided
    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated successfully\n")

def calculate_surplus_data(sales_row):
    """
    Calculate surplus by subtracting sales from stock.
    Positive surplus = too much stock (did not sell all)
    Negative surplus = not enough stock (more required to match demand)
    """
    print("Calculating surplus data...\n")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]
    
    surplus_data = []
    for stock, sales in zip(stock_row, sales_row):
        surplus = int(stock) - sales
        surplus_data.append(surplus)
    
    return surplus_data


def get_last_5_entries_sales():
    """ 
    Collects colums of data from sales worksheet, collecting
    the last 5 entries for each phone and returns the data
    as a list of lists
    """

    sales = SHEET.worksheet("sales")
   
    columns = []
    for ind in range(1, 7):
        column = sales.col_values(ind)
        columns.append(column[-5:])
    
    return 
    

def calculate_stock_data(data):
    """
    Calculate the average stock for each item type, adding 10%
    """
    print("Calculating stock data...\n")
    new_stock_data = []

    for column in data:
        int_column = [int(num) for num in column]
        average = sum(int_column) / len(int_column)
        stock_num = average * 1.1
        new_stock_data.append(round(stock_num))

    return new_stock_data



def calculate_sales_total(data):
    """ 
    Calculate the total number of sales, per week
    for each phone
    """
    print("Calculating total number of sales...\n")
    sales_total = []

    for column in data:
        int_column = [int(num) for num in column]
        sum = sum(int_column)
        sales_total.append(sum)

    return sales_total



def main():
    """
    Runs all program functions
    """
    data = get_sales_data()
    sales_data = [int(num) for num in data]
    update_worksheet(sales_data, "sales")
    new_surplus_data = calculate_surplus_data(sales_data)
    update_worksheet(new_surplus_data, "surplus")
    sales_columns = get_last_5_entries_sales()
    stock_data = calculate_stock_data(sales_columns)
    print(stock_data)

print("Welcome to Phone Shop Data Automation")

main()


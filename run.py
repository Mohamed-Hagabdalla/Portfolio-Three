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
    Get sales figures input from the user
    """
    print("Enter sales data from the last market.")
    print("Data should be six numbers, seperated by commas.")
    print("Example: 1,2,3,4,5,6\n")  # '\n' =  extra line of space   

    data_string = input("Enter your data here: ")
    print(f"The data provided is {data_string}")


get_sales_data()
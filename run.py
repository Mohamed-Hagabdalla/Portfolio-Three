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
    
    #split breaks up data at the commas
    #split returns broken up values as a list
    sales_data = data_string.split(",") 
    validate_data(sales_data)


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


get_sales_data()

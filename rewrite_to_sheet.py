import gspread
import pandas as pd

def update_google_sheet():
    # Authenticate with your credentials JSON file
    gc = gspread.service_account(filename= r"C:\Users\User\Documents\Survey_data\northern-card-454808-g9-b52f90fc8682.json")
    
    # Open your Google Sheet by name
    spreadsheet = gc.open("Data for website")
    
    # Select the worksheet (Sheet3)
    worksheet = spreadsheet.worksheet("Sheet3")
    
    # Read the updated CSV file
    df_updated = pd.read_csv("Combined_data.csv")
    
    # Convert DataFrame to list of lists (Google Sheets format)
    data_to_write = [df_updated.columns.tolist()] + df_updated.values.tolist()
    
    # Clear the existing data in the sheet (optional)
    worksheet.clear()
    
    # Write updated data to the Google Sheet
    worksheet.update(data_to_write)
    
    print("Google Sheet successfully updated!")

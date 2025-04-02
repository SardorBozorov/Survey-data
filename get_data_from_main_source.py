import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

# Path to your downloaded JSON key file
def load_data():
    creds_path = r"C:\Users\User\Documents\Survey_data\modify-and-sheft-survey-data-9dcf4242cbbd.json"
    
    # Define API scope
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    
    # Authenticate with Google Sheets API
    creds = ServiceAccountCredentials.from_json_keyfile_name(creds_path, scope)
    client = gspread.authorize(creds)
    
    # Open Google Sheet by ID
    sheet_id1 = "1RwiAha-vG2vkXsdYTnxU6tI6OvXPJW1cFmZbeCK6pLM"
    sheet_id2 = "1OD-_WU16jmJKBsiriIG1jSWazDjgFuMWoSU4M56rx84"  # Replace with your sheet ID
    
    sheet1 = client.open_by_key(sheet_id1)
    sheet2 = client.open_by_key(sheet_id2)
    
    # Get the first worksheet
    worksheet1 = sheet1.sheet1  # You can also use `sheet.get_worksheet(index)`
    worksheet2 = sheet2.sheet1
    # Read all data
    data_uz = worksheet1.get_all_records()
    
    data_ru = worksheet2.get_all_records()
    
    # Convert to DataFrame
    df1 = pd.DataFrame(data_uz)
    
    df2 = pd.DataFrame(data_ru)
    
    # Save to CSV
    df1.to_csv("survey_data_uz.csv", index=False)
    
    df2.to_csv("survey_data_ru.csv", index=False)
    
    print("✅ Data successfully saved as 'survey_data_uz.csv' and 'survey_data_ru.csv' ")

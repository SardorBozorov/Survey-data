import pandas as pd

def Filter_df():
    # Read CSV files
    df_ru = pd.read_csv("survey_data_ru.csv")
    df_uz = pd.read_csv("survey_data_uz.csv")

    # Ensure both DataFrames have the same number of columns
    if len(df_ru.columns) != len(df_uz.columns):
        raise ValueError("Column count mismatch between the two CSV files.")

    # Rename Russian columns to match Uzbek
    df_ru.columns = df_uz.columns  

    # ✅ Correct way to filter specific columns
    filtered_df_ru = df_ru[[
        "Timestamp",
        "1. Jinsingiz:",
        "2. Qaysi yosh oralig'idasiz?",
        "3. Qaysi hududda yashaysiz?",
        "4. Nima bilan shug’ullanasiz?",
        "5. Ma'lumotingiz:",
        "1. IT sohasida ko‘proq bilim olishga qiziqasizmi (masalan, kompyuter ko‘nikmalari, dasturlash yoki raqamli vositalardan foydalanish)?",
        "2. Sizningcha, IT-ko‘nikmalarni yaxshilash ishingiz/o‘qishingiz/hayotingiz sifatini oshirishi mumkinmi?",
        "3. Siz hozirda IT va raqamli ko'nikmalaringiz darajasini qanday baholaysiz?  ",
    ]]

    filtered_df_uz = df_uz[[
        "Timestamp",
        "1. Jinsingiz:",
        "2. Qaysi yosh oralig'idasiz?",
        "3. Qaysi hududda yashaysiz?",
        "4. Nima bilan shug’ullanasiz?",
        "5. Ma'lumotingiz:",
        "1. IT sohasida ko‘proq bilim olishga qiziqasizmi (masalan, kompyuter ko‘nikmalari, dasturlash yoki raqamli vositalardan foydalanish)?",
        "2. Sizningcha, IT-ko‘nikmalarni yaxshilash ishingiz/o‘qishingiz/hayotingiz sifatini oshirishi mumkinmi?",
        "3. Siz hozirda IT va raqamli ko'nikmalaringiz darajasini qanday baholaysiz?  ",
    ]]

    # existing_df = pd.read_csv('main_source.csv')

    # Convert 'Timestamp' in existing_df to datetime and then to date (just the date part)
    # existing_df['Timestamp'] = pd.to_datetime(existing_df['Timestamp'], errors='coerce').dt.date
    
    filtered_df_uz = filtered_df_uz.copy()
    filtered_df_ru = filtered_df_ru.copy()

    filtered_df_uz['Timestamp'] = pd.to_datetime(filtered_df_uz['Timestamp'], errors='coerce').dt.date
    filtered_df_ru['Timestamp'] = pd.to_datetime(filtered_df_ru['Timestamp'], errors='coerce').dt.date


    # Drop rows with invalid 'Timestamp' (NaT) in filtered dataframes
    # filtered_df_uz = filtered_df_uz.dropna(subset=['Timestamp'])
    # filtered_df_ru = filtered_df_ru.dropna(subset=['Timestamp'])

    # Filter out rows where the date is already in existing_df['Timestamp']
    # filtered_df_uz = filtered_df_uz[~filtered_df_uz['Timestamp'].isin(existing_df['Timestamp'])]
    # filtered_df_ru = filtered_df_ru[~filtered_df_ru['Timestamp'].isin(existing_df['Timestamp'])]

    # Save the filtered data to new CSV files
    filtered_df_ru.to_csv("Filtered_data_ru.csv", index=False)
    filtered_df_uz.to_csv("Filtered_data_uz.csv", index=False)
    # existing_df.to_csv("main_source.csv")

# Filter_df()

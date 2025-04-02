import time
import os
from get_data_from_main_source import load_data
from Filter_data import Filter_df
from Translate import Translator
from clean_and_fix_data import *
from rewrite_to_sheet import update_google_sheet

def wait_for_file(filename, timeout=30):
    """Wait until a file is created, with a timeout."""
    start_time = time.time()
    while not os.path.exists(filename):
        if time.time() - start_time > timeout:
            raise TimeoutError(f"File {filename} was not created in time.")
        time.sleep(1)  # Wait 1 second before checking again

print("▶️ Running load_data()...")
load_data()
wait_for_file("survey_data_ru.csv")  # Ensure the data file is available
wait_for_file("survey_data_uz.csv")

print("▶️ Running Filter_df()...")
Filter_df()
wait_for_file("Filtered_data_ru.csv")  # Ensure filtered data is available
wait_for_file("Filtered_data_uz.csv")

print("▶️ Running Translator()...")
Translator()

print("▶️ Running distribute_age()...")
distribute_age()

print("▶️ Running clean_degree()...")
clean_degree()

print("▶️ Running clean_jobs()...")
clean_jobs()

print("▶️ Running update_google_sheet()...")
update_google_sheet()

print("✅ All functions executed successfully!")

import pandas as pd
import numpy as np

df = pd.read_csv("Combined_data.csv")

def distribute_age():
    global df  
    # df["ID"] = df.index + 1  # Add ID column

    # Count number of people in each age category
    age_counts = df["2. Qaysi yosh oralig'idasiz?"].value_counts()

    # Extract all "35 yosh va undan yuqori" rows
    age_35_yuqori_df = df[df["2. Qaysi yosh oralig'idasiz?"] == "35 yosh va undan yuqori"].copy()

    # Known age group counts
    age_36_45 = age_counts.get("36-45 yosh", 0)
    age_46_52 = age_counts.get("46-52 yosh", 0)
    age_53_60 = age_counts.get("53-60 yosh", 0)
    age_61_yuqori = age_counts.get("61 yosh va undan yuqori", 0)
    age_35_yuqori = len(age_35_yuqori_df)

    # Total known ages (excluding 35+)
    total_known = age_36_45 + age_46_52 + age_53_60 + age_61_yuqori

    if total_known == 0 or age_35_yuqori == 0:
        print("No valid age groups to distribute into or no '35 yosh va undan yuqori' values.")
        return

    # Calculate proportions
    p_36_45 = age_36_45 / total_known
    p_46_52 = age_46_52 / total_known
    p_53_60 = age_53_60 / total_known
    p_61_yuqori = age_61_yuqori / total_known

    # Calculate new counts
    count_36_45 = int(round(p_36_45 * age_35_yuqori))
    count_46_52 = int(round(p_46_52 * age_35_yuqori))
    count_53_60 = int(round(p_53_60 * age_35_yuqori))
    count_61_yuqori = age_35_yuqori - (count_36_45 + count_46_52 + count_53_60)  # Assign the remaining to 61+

    # Shuffle rows to ensure random distribution
    age_35_yuqori_df = age_35_yuqori_df.sample(frac=1, random_state=42).reset_index(drop=True)

    # Assign new age groups
    age_35_yuqori_df.iloc[:count_36_45, df.columns.get_loc("2. Qaysi yosh oralig'idasiz?")] = "36-45 yosh"
    age_35_yuqori_df.iloc[count_36_45:count_36_45+count_46_52, df.columns.get_loc("2. Qaysi yosh oralig'idasiz?")] = "46-52 yosh"
    age_35_yuqori_df.iloc[count_36_45+count_46_52:count_36_45+count_46_52+count_53_60, df.columns.get_loc("2. Qaysi yosh oralig'idasiz?")] = "53-60 yosh"
    age_35_yuqori_df.iloc[count_36_45+count_46_52+count_53_60:, df.columns.get_loc("2. Qaysi yosh oralig'idasiz?")] = "61 yosh va undan yuqori"

    # Remove original "35 yosh va undan yuqori" and append the updated data
    df = df[df["2. Qaysi yosh oralig'idasiz?"] != "35 yosh va undan yuqori"]
    df = pd.concat([df, age_35_yuqori_df], ignore_index=True)

    print("Distribution complete!")
    print(df["2. Qaysi yosh oralig'idasiz?"].value_counts())

    df.to_csv("Combined_data.csv", index=False)

def clean_jobs():
    global df
    valid_categories = [
        "Ishlayman (davlat/nodavlat/xususiy/xalqaro yoki boshqa tashkilot)",
        "Tadbirkorman",
        "O'qiyman",
        "Vaqtinchalik ishsizman"
    ]
    
    # Replace invalid values with "Boshqa"
    df["4. Nima bilan shug’ullanasiz?"] = df["4. Nima bilan shug’ullanasiz?"].apply(
        lambda x: x if x in valid_categories else "Boshqa"
    )

    # Print the count of rows where the value is "Boshqa"
    print(df[df["4. Nima bilan shug’ullanasiz?"] == "Boshqa"].count())

    # Save the modified DataFrame to a CSV file
    df.to_csv("Combined_data.csv", index=False)

def clean_degree():
    global df
    valid_categories = [
        "Oliy (bakalavriat, magistratura va undan yuqori)",
        "Hali maktabda o'qiyman",
        "O‘rta (maktab attestati)",
        "O‘rta-maxsus (kollej/litsey diplomi)"
    ]

    # Replace invalid values with "Boshqa"
    df["5. Ma'lumotingiz:"] = df["5. Ma'lumotingiz:"].apply(
        lambda x: x if x in valid_categories else "Boshqa"
    )

    # Print the count of rows where the value is "Boshqa"
    print(df[df["5. Ma'lumotingiz:"] == "Boshqa"].count())
    df.to_csv("Combined_data.csv", index=False)


# distribute_age()
# clean_jobs()
# clean_degree()
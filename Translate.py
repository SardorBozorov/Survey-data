import pandas as pd

def Translator():

    df_ru = pd.read_csv("Filtered_data_ru.csv")
    df_uz = pd.read_csv("Filtered_data_uz.csv")

    # Gender
    df_ru.loc[df_ru["1. Jinsingiz:"] == "Женский", "1. Jinsingiz:"] = "Ayol"
    df_ru.loc[df_ru["1. Jinsingiz:"] == "Мужской", "1. Jinsingiz:"] = "Erkak"

    # Location
    df_ru.loc[df_ru["3. Qaysi hududda yashaysiz?"] == "Город Ташкент", "3. Qaysi hududda yashaysiz?"] = "Toshkent shahri"
    df_ru.loc[df_ru["3. Qaysi hududda yashaysiz?"] == "Ташкентская область", "3. Qaysi hududda yashaysiz?"] = "Toshkent viloyati"
    df_ru.loc[df_ru["3. Qaysi hududda yashaysiz?"] == "Андижанская область", "3. Qaysi hududda yashaysiz?"] = "Andijon viloyati"
    df_ru.loc[df_ru["3. Qaysi hududda yashaysiz?"] == "Бухарская область", "3. Qaysi hududda yashaysiz?"] = "Buxoro viloyati"
    df_ru.loc[df_ru["3. Qaysi hududda yashaysiz?"] == "Ферганская область", "3. Qaysi hududda yashaysiz?"] = "Farg‘ona viloyati"
    df_ru.loc[df_ru["3. Qaysi hududda yashaysiz?"] == "Джизакская область", "3. Qaysi hududda yashaysiz?"] = "Jizzax viloyati"
    df_ru.loc[df_ru["3. Qaysi hududda yashaysiz?"] == "Хорезмская область", "3. Qaysi hududda yashaysiz?"] = "Xorazm viloyati"
    df_ru.loc[df_ru["3. Qaysi hududda yashaysiz?"] == "Наманганская область", "3. Qaysi hududda yashaysiz?"] = "Namangan viloyati"
    df_ru.loc[df_ru["3. Qaysi hududda yashaysiz?"] == "Навоийская область", "3. Qaysi hududda yashaysiz?"] = "Navoiy viloyati"
    df_ru.loc[df_ru["3. Qaysi hududda yashaysiz?"] == "Кашкадарьинская область", "3. Qaysi hududda yashaysiz?"] = "Qashqadaryo viloyati"
    df_ru.loc[df_ru["3. Qaysi hududda yashaysiz?"] == "Республика Каракалпакстан", "3. Qaysi hududda yashaysiz?"] = "Qoraqalpog‘iston Respublikasi"
    df_ru.loc[df_ru["3. Qaysi hududda yashaysiz?"] == "Самаркандская область", "3. Qaysi hududda yashaysiz?"] = "Samarqand viloyati"
    df_ru.loc[df_ru["3. Qaysi hududda yashaysiz?"] == "Сырдарьинская область", "3. Qaysi hududda yashaysiz?"] = "Sirdaryo viloyati"
    df_ru.loc[df_ru["3. Qaysi hududda yashaysiz?"] == "Сурхандарьинская область", "3. Qaysi hududda yashaysiz?"] = "Surxondaryo viloyati"


    # Age
    df_ru.loc[df_ru["2. Qaysi yosh oralig'idasiz?"] == "до 15 лет", "2. Qaysi yosh oralig'idasiz?"] = "15 yoshgacha"
    df_ru.loc[df_ru["2. Qaysi yosh oralig'idasiz?"] == "15–17 лет", "2. Qaysi yosh oralig'idasiz?"] = "15-17 yosh"
    df_ru.loc[df_ru["2. Qaysi yosh oralig'idasiz?"] == "18–20 лет", "2. Qaysi yosh oralig'idasiz?"] = "18-20 yosh"
    df_ru.loc[df_ru["2. Qaysi yosh oralig'idasiz?"] == "21–23 года", "2. Qaysi yosh oralig'idasiz?"] = "21-23 yosh"
    df_ru.loc[df_ru["2. Qaysi yosh oralig'idasiz?"] == "24–27 лет", "2. Qaysi yosh oralig'idasiz?"] = "24-27 yosh"
    df_ru.loc[df_ru["2. Qaysi yosh oralig'idasiz?"] == "28–35 лет", "2. Qaysi yosh oralig'idasiz?"] = "28-35 yosh"
    df_ru.loc[df_ru["2. Qaysi yosh oralig'idasiz?"] == "36-45 лет", "2. Qaysi yosh oralig'idasiz?"] = "36-45 yosh"
    df_ru.loc[df_ru["2. Qaysi yosh oralig'idasiz?"] == "46-52 года", "2. Qaysi yosh oralig'idasiz?"] = "46-52 yosh"
    df_ru.loc[df_ru["2. Qaysi yosh oralig'idasiz?"] == "53-60 лет", "2. Qaysi yosh oralig'idasiz?"] = "53-60 yosh"
    df_ru.loc[df_ru["2. Qaysi yosh oralig'idasiz?"] == "61 год и старше", "2. Qaysi yosh oralig'idasiz?"] = "61 yosh va undan yuqori"
    df_ru.loc[df_ru["2. Qaysi yosh oralig'idasiz?"] == "35 лет и старше", "2. Qaysi yosh oralig'idasiz?"] = "35 yosh va undan yuqori"

    # Occupation
    df_ru.loc[df_ru["4. Nima bilan shug’ullanasiz?"] == "Работаю (государственная/негосударственная/частная/международная или другая организация)", "4. Nima bilan shug’ullanasiz?"] = "Ishlayman (davlat/nodavlat/xususiy/xalqaro yoki boshqa tashkilot)"
    df_ru.loc[df_ru["4. Nima bilan shug’ullanasiz?"] == "Предприниматель", "4. Nima bilan shug’ullanasiz?"] = "Tadbirkorman"
    df_ru.loc[df_ru["4. Nima bilan shug’ullanasiz?"] == "Учусь", "4. Nima bilan shug’ullanasiz?"] = "O’qiyman"
    df_ru.loc[df_ru["4. Nima bilan shug’ullanasiz?"] == "Временно безработный", "4. Nima bilan shug’ullanasiz?"] = "Vaqtinchalik ishsizman"

    # Degree
    df_ru.loc[df_ru["5. Ma'lumotingiz:"] == "Пока учусь в школе", "5. Ma'lumotingiz:"] = "Hali maktabda o‘qiyman"
    df_ru.loc[df_ru["5. Ma'lumotingiz:"] == "Среднее (аттестат школы)", "5. Ma'lumotingiz:"] = "O‘rta (maktab attestati)"
    df_ru.loc[df_ru["5. Ma'lumotingiz:"] == "Средне-специальное (диплом колледжа/лицея)", "5. Ma'lumotingiz:"] = "O‘rta-maxsus (kollej/litsey diplomi)"
    df_ru.loc[df_ru["5. Ma'lumotingiz:"] == "Высшее (бакалавриат, магистратура или выше)", "5. Ma'lumotingiz:"] = "Oliy (bakalavriat, magistratura va undan yuqori)"


    df_ru.loc[df_ru["1. IT sohasida ko‘proq bilim olishga qiziqasizmi (masalan, kompyuter ko‘nikmalari, dasturlash yoki raqamli vositalardan foydalanish)?"] == "Да", "1. IT sohasida ko‘proq bilim olishga qiziqasizmi (masalan, kompyuter ko‘nikmalari, dasturlash yoki raqamli vositalardan foydalanish)?"] = "Ha"
    df_ru.loc[df_ru["1. IT sohasida ko‘proq bilim olishga qiziqasizmi (masalan, kompyuter ko‘nikmalari, dasturlash yoki raqamli vositalardan foydalanish)?"] == "Нет", "1. IT sohasida ko‘proq bilim olishga qiziqasizmi (masalan, kompyuter ko‘nikmalari, dasturlash yoki raqamli vositalardan foydalanish)?"] = "Yo'q"


    df_ru.loc[df_ru["2. Sizningcha, IT-ko‘nikmalarni yaxshilash ishingiz/o‘qishingiz/hayotingiz sifatini oshirishi mumkinmi?"] == "Да", "2. Sizningcha, IT-ko‘nikmalarni yaxshilash ishingiz/o‘qishingiz/hayotingiz sifatini oshirishi mumkinmi?"] = "Ha"
    df_ru.loc[df_ru["2. Sizningcha, IT-ko‘nikmalarni yaxshilash ishingiz/o‘qishingiz/hayotingiz sifatini oshirishi mumkinmi?"] == "Нет", "2. Sizningcha, IT-ko‘nikmalarni yaxshilash ishingiz/o‘qishingiz/hayotingiz sifatini oshirishi mumkinmi?"] = "Yo'q"

    df_ru.loc[df_ru["3. Siz hozirda IT va raqamli ko'nikmalaringiz darajasini qanday baholaysiz?  "] == "Практически ничего не знаю о компьютерах или интернете", "3. Siz hozirda IT va raqamli ko'nikmalaringiz darajasini qanday baholaysiz?  "] = "Kompyuter yoki internet haqida deyarli hech narsa bilmayman."
    df_ru.loc[df_ru["3. Siz hozirda IT va raqamli ko'nikmalaringiz darajasini qanday baholaysiz?  "] == "Имею базовые знания", "3. Siz hozirda IT va raqamli ko'nikmalaringiz darajasini qanday baholaysiz?  "] = "Bazaviy bilimlarga egaman."
    df_ru.loc[df_ru["3. Siz hozirda IT va raqamli ko'nikmalaringiz darajasini qanday baholaysiz?  "] == "Могу свободно пользоваться множеством цифровых инструментов", "3. Siz hozirda IT va raqamli ko'nikmalaringiz darajasini qanday baholaysiz?  "] = "Ko‘plab raqamli vositalardan bemalol foydalana olaman."
    df_ru.loc[df_ru["3. Siz hozirda IT va raqamli ko'nikmalaringiz darajasini qanday baholaysiz?  "] == "Обладаю продвинутыми навыками", "3. Siz hozirda IT va raqamli ko'nikmalaringiz darajasini qanday baholaysiz?  "] = "Ilg‘or ko‘nikmalarga egaman."


    df_ru.to_csv("Filtered_data_ru.csv", index=False)

    df_ru = df_ru.iloc[1:].reset_index(drop=True)

    combined_data = pd.concat([df_uz, df_ru], ignore_index=False)

    combined_data.to_csv("Combined_data.csv", index=False)
# Translator()
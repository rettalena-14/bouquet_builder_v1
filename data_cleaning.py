import pandas as pd

raw_file = "data/flowers_dictionary_indo.xlsx"

df = pd.read_excel(
    raw_file,
    sheet_name="flowers_dictionary_indo"
)

df.columns = df.columns.str.strip()

text_columns = [
    "flower_type",
    "flower_name",
    "colours",
    "variant_name",
    "blooming_season",
    "import_non"
]

for column in text_columns:
    df[column] = df[column].astype(str).str.strip()


numeric_columns = [
    "cost_per_stem",
    "cost_per_bunch",
    "quantity"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(
        df[column],
        errors="coerce"
    )


season_mapping = {
    "Jan": "January",
    "Feb": "February",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

df["blooming_season"] = df["blooming_season"].replace(
    season_mapping
)

month_mapping = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}


cleaned_rows = []

for _, row in df.iterrows():

    season = row["blooming_season"]

    if season == "all season":

        for month in range(1, 13):

            new_row = row.copy()

            new_row["date"] = pd.Timestamp(
                year=2026,
                month=month,
                day=1
            )

            cleaned_rows.append(new_row)

    elif season in month_mapping:

        month = month_mapping[season]

        new_row = row.copy()

        new_row["date"] = pd.Timestamp(
            year=2026,
            month=month,
            day=1
        )

        cleaned_rows.append(new_row)


cleaned_df = pd.DataFrame(cleaned_rows)

cleaned_df["date"] = pd.to_datetime(
    cleaned_df["date"]
)


cleaned_df = cleaned_df.reset_index(drop=True)


output_file = "cleaned/flowers_cleaned.csv"

cleaned_df.to_csv(
    output_file,
    index=False
)

print("Data cleaning complete!")
print(f"Raw rows: {len(df)}")
print(f"Cleaned rows: {len(cleaned_df)}")
print(f"Saved to: {output_file}")
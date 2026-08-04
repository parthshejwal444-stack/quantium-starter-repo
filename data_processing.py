import pandas as pd
import glob

files = glob.glob("data/*.csv")

dfs = []

for file in files:
    df = pd.read_csv(file)

    # Keep only Pink Morsels
    df = df[df["product"] == "pink morsels"]

    # Create Sales column
    df["Sales"] = df["quantity"] * df["price"]

    # Keep required columns
    df = df[["Sales", "date", "region"]]

    # Rename columns
    df.columns = ["Sales", "Date", "Region"]

    dfs.append(df)

final_df = pd.concat(dfs, ignore_index=True)

final_df.to_csv("processed_sales_data.csv", index=False)

print("processed_sales_data.csv created successfully!")
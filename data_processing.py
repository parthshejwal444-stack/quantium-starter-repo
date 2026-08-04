import pandas as pd
import os

# data folder path
data_folder = "data"

# all csv files
files = os.listdir(data_folder)

# empty dataframe
sales_data = pd.DataFrame()

# combine all csv files
for file in files:
    if file.endswith(".csv"):
        df = pd.read_csv(os.path.join(data_folder, file))
        sales_data = pd.concat([sales_data, df], ignore_index=True)

# show first rows
print("Data Preview:")
print(sales_data.head())

# show columns
print("\nColumns:")
print(sales_data.columns)

# save processed data
sales_data.to_csv("processed_sales_data.csv", index=False)

print("\nData processing completed!")
import pandas as pd
import sqlite3

# Define a function to read data from the Excel files
def extract_data(file_path):
    return pd.read_excel(file_path, engine='openpyxl')




def transform_data(df, region):
    df['total_sales'] = df['QuantityOrdered'] * df['ItemPrice']
    df['region'] = region
    df = df.drop_duplicates(subset=['OrderId'])
    return df

# Extract data from both regions
df_a = extract_data('order_region_a.xlsx')
df_b = extract_data('order_region_b.xlsx')

# Transform data for both regions
df_a_transformed = transform_data(df_a, 'A')
df_b_transformed = transform_data(df_b, 'B')

# Combine data from both regions
combined_df = pd.concat([df_a_transformed, df_b_transformed])

# Validate the data using pandas

# Count the total number of records
total_records = combined_df.shape[0]

# Find the total sales amount by region
total_sales_by_region = combined_df.groupby('region')['total_sales'].sum()

# Find the average sales amount per transaction
avg_sales_per_transaction = combined_df['total_sales'].mean()

# Ensure there are no duplicate OrderId values
duplicate_order_ids = combined_df.duplicated(subset=['OrderId']).sum()

# Print the results of the validation
print(f"Total number of records: {total_records}")
print(f"Total sales amount by region:\n{total_sales_by_region}")
print(f"Average sales amount per transaction: {avg_sales_per_transaction}")
print(f"Number of duplicate OrderId values: {duplicate_order_ids}")
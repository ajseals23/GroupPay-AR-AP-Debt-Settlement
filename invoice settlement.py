import pandas as pd

# Load data
df = pd.read_csv('Construction_Contracts.csv')

print(df.head())

# Calculate Accounts Payable
vendor_AP = df.groupby('contractor_id')['revised_amount'].sum().reset_index()

# Calculate Accounts Recievable
vendor_AR = df.groupby('vendor_id')['revised_amount'].sum().reset_index()

# need to add 


import pandas as pd
from GUI import on_company_selected

# Load data
df = pd.read_csv('Construction_Contracts.csv')

print(df.head())

# Calculate Accounts Payable
vendor_AP = df.groupby('contractor_id')['revised_amount'].sum()
# Calculate Accounts Recievable
vendor_AR = df.groupby('vendor_id')['revised_amount'].sum().reset_index()

# need to calculate net amount based on total AP & AR
# need to categorize by aging
# need to create meaure to show how much need

total_AP = vendor_AP[vendor_AP['contractor_id'] == 2]

print(total_AP)
import tkinter as tk
from tkinter import ttk
import pandas as pd

def company_details(company):
    print(f"Selected Company: {company}")

# Load CSV data
csv_filepath = 'company_ref.csv'
df = pd.read_csv(csv_filepath)
companies_list = df['company_name'].tolist()

# Create main window
root = tk.Tk()
root.title("Company Selector")

# Create label
label = ttk.Label(root, text="Select a Company:")
label.pack(padx=10, pady=10)

# Create Dropdown for selecting company
company_var = tk.StringVar()
company_combobox = ttk.Combobox(root, textvariable=company_var, values=companies_list, state="readonly")
company_combobox.pack(padx=10, pady=10)

# Start main loop
root.mainloop()
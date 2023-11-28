
import tkinter as tk
from tkinter import ttk
import pandas as pd

def company_details(company):
    df = pd.read_csv('Construction_Contracts.csv')

    # Calculate Accounts Payable
    vendor_AP = df[df['contractor_name'] == company]['revised_amount'].sum()

    # Calculate Accounts Receivable
    vendor_AR = df[df['vendor_name'] == company]['revised_amount'].sum()

    # Display results
    result_label.config(text=f"Selected Company: {company}\nTotal AP: {vendor_AP}\nTotal AR: {vendor_AR}")

def on_company_selected(event):
    selected_company = company_var.get()
    company_details(selected_company)

# Load company ref
csv_filepath = 'company_ref.csv'
df = pd.read_csv(csv_filepath)
companies_list = df['company_name'].tolist()

# main window
root = tk.Tk()
root.title("Company Selector")

# label
label = ttk.Label(root, text="Select a Company:")
label.pack(padx=10, pady=10)

# selecting company
company_var = tk.StringVar()
company_combobox = ttk.Combobox(root, textvariable=company_var, values=companies_list, state="readonly")
company_combobox.pack(padx=10, pady=10)

# Discount entry
discount_label = ttk.Label(root, text="Enter Discount Percentage:")
discount_label.pack(padx=10, pady=10)

discount_var = tk.StringVar()
discount_entry = ttk.Entry(root, textvariable=discount_var)
discount_entry.pack(padx=10, pady=10)
discount_entry.bind("<KeyRelease>", lambda _: apply_discount(discount_var.get()))

# display results
result_label = ttk.Label(root, text="")
result_label.pack(padx=10, pady=10)

# Bind the event handler to the combobox selection event
company_combobox.bind("<<ComboboxSelected>>", on_company_selected)

# main loop
root.mainloop()



# TO DO 
# add discount percentage for AR to get quicker cash 

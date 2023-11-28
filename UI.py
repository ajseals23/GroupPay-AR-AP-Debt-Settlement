import tkinter as tk
from tkinter import ttk
import pandas as pd

# Styling and Design
style = ttk.Style()
style.theme_use('clam')  # Using a theme for better widget styles
style.configure('TLabel', background='lightgray', font=('Helvetica', 10))
style.configure('TButton', font=('Helvetica', 10))
style.configure('TEntry', font=('Helvetica', 10))
style.configure('TCombobox', font=('Helvetica', 10))
style.configure('Header.TLabel', font=('Helvetica', 12, 'bold'))

def company_details(company):
    try:
        df = pd.read_csv('Construction_Contracts.csv')
    except FileNotFoundError:
        result_label.config(text="Error: 'Construction_Contracts.csv' file not found.")
        return 0, 0
        
    # Calculate Accounts Payable
    vendor_AP = df[df['contractor_name'] == company]['revised_amount'].sum()

    # Calculate Accounts Receivable
    vendor_AR = df[df['vendor_name'] == company]['revised_amount'].sum()

    return vendor_AP, vendor_AR  # Return the calculated values

def apply_discount():
    # Retrieve the name of the selected company from the dropdown menu
    selected_company = company_var.get()
        if selected_company:
            vendor_AP, vendor_AR = company_details(selected_company)
        if vendor_AP == 0 and vendor_AR == 0:
            return  # Exit if there was an error in reading the file

        try:
            discount = float(discount_var.get()) / 100
            if 0 <= discount <= 1:  # Ensure discount is within 0-100%
                discounted_AR = vendor_AR * (1 - discount)
                result_label.config(text=f"Selected Company: {selected_company}\nTotal AP: {vendor_AP}\nTotal AR: {vendor_AR}\nDiscounted AR: {discounted_AR}")
            else:
                result_label.config(text="Please enter a discount percentage between 0 and 100.")
        except ValueError:
            result_label.config(text="Please enter a valid discount percentage.")
    else:
        result_label.config(text="Please select a company.")

def on_company_selected(event):
    selected_company = company_var.get()
    if selected_company:
        vendor_AP, vendor_AR = company_details(selected_company)
        result_label.config(text=f"Selected Company: {selected_company}\nTotal AP: {vendor_AP}\nTotal AR: {vendor_AR}")
    

# Load company data
csv_filepath = 'company_ref.csv'
df = pd.read_csv(csv_filepath)
companies_list = df['company_name'].tolist()

# main window
root = tk.Tk()
root.title("Company Selector")
root.configure(background='lightgray')

# Header label
header_label = ttk.Label(root, text="Company Financial Details", style='Header.TLabel')
header_label.pack(padx=10, pady=(10, 5))

# Selecting company
company_var = tk.StringVar()
company_combobox = ttk.Combobox(root, textvariable=company_var, values=companies_list, state="readonly")
company_combobox.pack(padx=10, pady=5)
company_combobox.bind("<<ComboboxSelected>>", on_company_selected)

# Discount entry
discount_label = ttk.Label(root, text="Enter Discount Percentage:")
discount_label.pack(padx=10, pady= (5, 2))
discount_var = tk.StringVar()
discount_entry = ttk.Entry(root, textvariable=discount_var)
discount_entry.pack(padx=10, pady=2)
discount_entry.bind("<KeyRelease>", lambda _: apply_discount())

# display results
result_label = ttk.Label(root, text="", anchor='center')
result_label.pack(padx=10, pady=10, fill='x', expand=True)

# Bind the event handler to the combobox selection event
company_combobox.bind("<<ComboboxSelected>>", on_company_selected)

# main loop
root.mainloop()


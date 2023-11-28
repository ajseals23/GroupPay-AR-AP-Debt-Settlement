
import tkinter as tk
from tkinter import ttk
import pandas as pd

# Enhanced Styling
style = ttk.Style()
style.theme_use('clam')  # Using a theme for better widget styles
style.configure('TLabel', background='lightgray', font=('Helvetica', 10))
style.configure('TButton', font=('Helvetica', 10))
style.configure('TEntry', font=('Helvetica', 10))
style.configure('TCombobox', font=('Helvetica', 10))
style.configure('Header.TLabel', font=('Helvetica', 12, 'bold'))

def company_details(company):
    df = pd.read_csv('Construction_Contracts.csv')

    # Calculate Accounts Payable
    vendor_AP = df[df['contractor_name'] == company]['revised_amount'].sum()

    # Calculate Accounts Receivable
    vendor_AR = df[df['vendor_name'] == company]['revised_amount'].sum()

    # Display results
    result_label.config(text=f"Selected Company: {company}\nTotal AP: {vendor_AP}\nTotal AR: {vendor_AR}")

def apply_discount():
    # Retrieve the name of the selected company from the dropdown menu
    selected_company = company_var.get()

     # Check if a company is selected
    if selected_company:
    
        # Call the company_details function to get accounts payable and receivable for the selected company
        vendor_AP, vendor_AR = company_details(selected_company)
        
        try:
            # Attempt to convert the entered discount value to a float and divide by 100 to get a percentage
            discount = float(discount_var.get()) / 100

             # Calculate the discounted accounts receivable amount
            discounted_AR = vendor_AR * (1 - discount)

            # Update the result label to display the selected company, its accounts payable, receivable, and the discounted AR
            result_label.config(text=f"Selected Company: {selected_company}\nTotal AP: {vendor_AP}\nTotal AR: {vendor_AR}\nDiscounted AR: {discounted_AR}")
            
        except ValueError:
            # If the entered discount is not a valid number, update the result label to prompt for a valid discount percentage
            result_label.config(text="Please enter a valid discount percentage.")

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

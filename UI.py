import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import pandas as pd

class GroupPayApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("GroupPay")
        self.geometry("800x600")  # Set the window dimensions
        self.configure(bg="#F5F5F5")  # Change the background color
        self.df_companies = pd.read_csv('company_ref.csv')
        self.df_contracts = pd.read_csv('Construction_Contracts.csv')
        self.create_widgets()

    def create_widgets(self):
        self.configure_styles()
        self.create_title_frame()
        self.create_content_frame()

    def configure_styles(self):
        style = ttk.Style()
        style.theme_use("clam")  # Use the 'clam' theme for a modern appearance
        
        # Configure the style for labels
        style.configure("TLabel", font=("Arial", 18), foreground="#333333", background="#F5F5F5")
        
        # Configure the style for buttons
        style.configure("TButton", font=("Arial", 16), padding=10, foreground="white", background="#007acc")
        style.map("TButton", background=[("active", "#005a8e")])

        # Configure the style for combobox
        style.configure("TCombobox", font=("Arial", 18))
        
        # Configure the style for frames
        style.configure("TFrame", background="#F5F5F5")

    def create_title_frame(self):
        title_frame = ttk.Frame(self)
        title_frame.pack(pady=20)
        
        # Banner Image
        self.load_banner_image('group_pay_banner.png', title_frame)

        # Title Label
        title_label = ttk.Label(title_frame, text="GroupPay", font=("Helvetica", 36, "bold"), background="#007acc", foreground="white")
        title_label.pack(pady=20)

    def create_content_frame(self):
        content_frame = ttk.Frame(self)
        content_frame.pack(padx=20, pady=20)

        # Company Label and Combobox
        company_label = ttk.Label(content_frame, text="Select a Company:")
        company_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        self.company_var = tk.StringVar()
        company_combobox = ttk.Combobox(content_frame, textvariable=self.company_var, values=self.df_companies['company_name'].tolist(), state="readonly", style="TCombobox")
        company_combobox.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)
        company_combobox.bind("<<ComboboxSelected>>", self.on_company_selected)

        # Discount Label and Entry
        discount_label = ttk.Label(content_frame, text="Enter Discount Percentage:")
        discount_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        self.discount_var = tk.StringVar()
        discount_entry = ttk.Entry(content_frame, textvariable=self.discount_var, font=("Arial", 18))
        discount_entry.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)
        discount_entry.bind("<KeyRelease>", self.apply_discount)

        # Result Label
        self.result_label = ttk.Label(content_frame, text="", font=("Arial", 18), background="#F5F5F5")
        self.result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=20, sticky=tk.W)

    def load_banner_image(self, image_path, container):
        try:
            image = Image.open(image_path)
            image = image.resize((800, 200), Image.ANTIALIAS)
            self.banner_image = ImageTk.PhotoImage(image)
            banner_canvas = tk.Canvas(container, width=800, height=200)
            banner_canvas.create_image(0, 0, anchor=tk.NW, image=self.banner_image)
            banner_canvas.pack()
        except Exception as e:
            print(f"Error loading image: {str(e)}")

    def on_company_selected(self, event):
        selected_company = self.company_var.get()
        self.company_details(selected_company)

    def company_details(self, company, return_values=False):
        # Business Logic
        vendor_AP = self.df_contracts[self.df_contracts['contractor_name'] == company]['revised_amount'].sum()
        vendor_AR = self.df_contracts[self.df_contracts['vendor_name'] == company]['revised_amount'].sum()

        if return_values:
            return vendor_AP, vendor_AR
        else:
            self.result_label.config(text=f"Selected Company: {company}\nTotal AP: {vendor_AP}\nTotal AR: {vendor_AR}")

    def apply_discount(self, event):
        selected_company = self.company_var.get()
        discount = self.discount_var.get()
        if selected_company:
            vendor_AP, vendor_AR = self.company_details(selected_company, return_values=True)
            try:
                discount = float(discount) / 100
                discounted_AR = vendor_AR * (1 - discount)
                self.result_label.config(text=f"Selected Company: {selected_company}\nTotal AP: {vendor_AP}\nTotal AR: {vendor_AR}\nDiscounted AR: {discounted_AR:.2f}")
            except ValueError:
                self.result_label.config(text="Please enter a valid discount percentage.")

if __name__ == "__main__":
    app = GroupPayApp()
    app.mainloop()


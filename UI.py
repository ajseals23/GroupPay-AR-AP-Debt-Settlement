import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import pandas as pd
import logging

class GroupPayApp(tk.Tk):
    def __init__(self):
        super().__init__()
        # Setting up the main window
        self.title("GroupPay")
        self.geometry("800x600")
        self.configure(bg="#f4f4f4")

        # Initialize data and UI components
        self.init_data()
        self.configure_styles()
        self.create_widgets()

    def init_data(self):
        # Load data from CSV files
        try:
            self.df_companies = pd.read_csv('company_ref.csv')
            self.df_contracts = pd.read_csv('Construction_Contracts.csv')
        except Exception as e:
            # Log errors if loading fails
            logging.error(f"Error loading data: {str(e)}")
            self.df_companies = pd.DataFrame()
            self.df_contracts = pd.DataFrame()

    def configure_styles(self):
        # Configure the appearance of ttk widgets
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("TLabel", font=("Arial", 18), foreground="#333333", background="#f4f4f4")
        style.configure("TButton", font=("Arial", 16), padding=10, foreground="white", background="#28a745")
        style.map("TButton", background=[("active", "#218838")])
        style.configure("TCombobox", font=("Arial", 18))
        style.configure("TFrame", background="#f4f4f4")

    def create_widgets(self):
        # Create main frames and widgets of the application
        self.create_title_frame()
        self.create_content_frame()
        self.create_contact_footer()

    def create_title_frame(self):
        # Create the title frame with a banner and title label
        title_frame = ttk.Frame(self)
        title_frame.pack(pady=20)
        self.load_banner_image('group_pay_banner.png', title_frame)
        title_label = ttk.Label(title_frame, text="GroupPay", font=("Arial", 36, "bold"), foreground="#007bff", background="#f4f4f4")
        title_label.pack(pady=10)

    def create_content_frame(self):
        # Create the main content frame
        content_frame = ttk.Frame(self)
        content_frame.pack(padx=20, pady=20)
        self.create_company_selection(content_frame)
        self.create_discount_entry(content_frame)
        self.create_calculate_button(content_frame)
        self.create_result_label(content_frame)

    def create_company_selection(self, frame):
        # Create widgets for company selection
        company_label = ttk.Label(frame, text="Select a Company:")
        company_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        self.company_var = tk.StringVar()
        company_combobox = ttk.Combobox(frame, textvariable=self.company_var, values=self.df_companies['company_name'].tolist(), state="readonly")
        company_combobox.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)
        company_combobox.bind("<<ComboboxSelected>>", self.on_company_selected)

    def create_discount_entry(self, frame):
        # Create widgets for entering discount percentage
        discount_label = ttk.Label(frame, text="Enter Discount Percentage:")
        discount_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        self.discount_var = tk.StringVar()
        discount_entry = ttk.Entry(frame, textvariable=self.discount_var, font=("Arial", 18))
        discount_entry.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

    def create_calculate_button(self, frame):
        # Create a button to calculate discount
        calculate_button = ttk.Button(frame, text="Calculate", command=self.calculate_discount)
        calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=20)

    def create_result_label(self, frame):
        # Create a label to display the results
        self.result_label = ttk.Label(frame, text="", font=("Arial", 18), background="#f4f4f4")
        self.result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=20, sticky=tk.W)

    def load_banner_image(self, image_path, container):
        # Load and display the banner image
        try:
            image = Image.open(image_path)
            image = image.resize((800, 200), Image.ANTIALIAS)
            self.banner_image = ImageTk.PhotoImage(image)
            banner_canvas = tk.Canvas(container, width=800, height=200)
            banner_canvas.create_image(0, 0, anchor=tk.NW, image=self.banner_image)
            banner_canvas.pack()
        except Exception as e:
            logging.error(f"Error loading image: {str(e)}")

    def on_company_selected(self, event):
        # Handle company selection event
        selected_company = self.company_var.get()
        self.update_company_details(selected_company)

    def update_company_details(self, company):
        # Update and display company details
        try:
            vendor_AP, vendor_AR = self.calculate_company_details(company)
            self.result_label.config(text=f"Selected Company: {company}\nTotal AP: {vendor_AP}\nTotal AR: {vendor_AR}")
        except Exception as e:
            self.result_label.config(text=f"Error: {str(e)}")

    def calculate_company_details(self, company):
        # Calculate details for the selected company
        vendor_AP = self.df_contracts[self.df_contracts['contractor_name'] == company]['revised_amount'].sum()
        vendor_AR = self.df_contracts[self.df_contracts['vendor_name'] == company]['revised_amount'].sum()
        return vendor_AP, vendor_AR

    def calculate_discount(self):
        # Calculate and display discount based on user input
        selected_company = self.company_var.get()
        discount = self.discount_var.get()
        try:
            vendor_AP, vendor_AR = self.calculate_company_details(selected_company)
            discount = float(discount) / 100
            discounted_AR = vendor_AR * (1 - discount)
            self.result_label.config(text=f"Selected Company: {selected_company}\nTotal AP: {vendor_AP}\nTotal AR: {vendor_AR}\nDiscounted AR: {discounted_AR:.2f}")
        except ValueError:
            self.result_label.config(text="Please enter a valid discount percentage.")
        except Exception as e:
            self.result_label.config(text=f"Error: {str(e)}")

    def create_contact_footer(self):
        # Create a footer for contact information
        contact_frame = ttk.Frame(self)
        contact_frame.pack(side="bottom")
        contact_label = ttk.Label(contact_frame, text="Contact Us:", font=("Arial", 16, "bold"), foreground="#333333", background="#f4f4f4")
        contact_label.pack(side="left", padx=10, pady=5)
        contact_info_label = ttk.Label(contact_frame, text="Email: GroupPay@gmail.com | Phone: (407) 902-5737", font=("Arial", 12), foreground="#333333", background="#f4f4f4")
        contact_info_label.pack(side="left", padx=10)

if __name__ == "__main__":
    # Configure logging and run the application
    logging.basicConfig(level=logging.ERROR)
    app = GroupPayApp()
    app.mainloop()


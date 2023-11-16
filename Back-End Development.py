import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

# Create class for contract based on data

class Contract:
    def __init__(self, object_id, contract_number, description, status, contract_type, subtype, last_modified, original_amount, revised_amount, vendor_id):
        self.object_id = object_id
        self.contract_number = contract_number
        self.description = description
        self.status = status
        self.contract_type = contract_type
        self.subtype = subtype
        self.last_modified = last_modified
        self.original_amount = original_amount
        self.revised_amount = revised_amount
        self.vendor_id = vendor_id

# Create class for vendor based on data

class Vendor:
    def __init__(self, vendor_id, name):
        self.vendor_id = vendor_id
        self.name = name
        self.contracts = []

# Define add contract element

    def add_contract(self, contract):
        self.contracts.append(contract)

# Create class for Group

class Group:
    def __init__(self, group_id, name):
        self.group_id = group_id
        self.name = name
        self.vendors = []
        self.invoices = []

    def add_vendor(self, vendor):
        self.vendors.append(vendor)

    def add_invoice(self, invoice):
        self.invoices.append(invoice)

# Create class for Invoice

class Invoice:
    def __init__(self, invoice_id, amount, due_date):
        self.invoice_id = invoice_id
        self.amount = amount
        self.due_date = due_date

# Define and load contracts element

def load_contracts(csv_filepath):
    df = pd.read_csv(csv_filepath)
    vendors = {}
    for _, row in df.iterrows():
        vendor_id = row['vendor_id']
        if vendor_id not in vendors:
            vendors[vendor_id] = Vendor(vendor_id, row['vendor_name'])
        contract = Contract(
            row['object_id'], row['contract_number'], row['description'],
            row['status'], row['contract_type'], row['subtype'], 
            row['last_modified'], row['original_amount'], 
            row['revised_amount'], vendor_id
        )
        vendors[vendor_id].add_contract(contract)
    return vendors

# Add new route for getting vendors

@app.route('/vendors', methods=['GET'])
def get_vendors():
    csv_filepath = "~/Desktop/Construction_Contracts.csv"
    vendors = load_contracts(csv_filepath)
    vendors_data = [{vendor_id: vendor.name} for vendor_id, vendor in vendors.items()]
    return jsonify(vendors_data)

# In-memory storage for groups and invoices
groups = {}

# Add new route for adding group with logic

@app.route('/add_group', methods=['POST'])
def add_group():
    data = request.json
    group_id = data['group_id']
    if group_id in groups:
        return jsonify({"message": "Group already exists"}), 400
    new_group = Group(group_id, data['name'])
    groups[group_id] = new_group
    return jsonify({"message": "Group added successfully"}), 201






    






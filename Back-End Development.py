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

# Define and load contracts element

def load_contracts(csv_filepath):
    # Read the CSV file into a pandas DataFrame
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

# Define get_vendors element

@app.route('/vendors', methods=['GET'])
def get_vendors():
    csv_filepath = "~/Desktop/Construction_Contracts.csv"
    vendors = load_contracts(csv_filepath)
    vendors_data = [{vendor_id: vendor.name} for vendor_id, vendor in vendors.items()]
    return jsonify(vendors_data)







    






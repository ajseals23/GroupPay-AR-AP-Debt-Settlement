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


@app.route('/vendors', methods=['GET'])
def get_vendors():
    # Use the specific file path as requested
    csv_filepath = "~/Desktop/Construction_Contracts.csv"
    vendors = load_contracts(csv_filepath)
    vendors_data = [{vendor_id: vendor.name} for vendor_id, vendor in vendors.items()]
    return jsonify(vendors_data)







    






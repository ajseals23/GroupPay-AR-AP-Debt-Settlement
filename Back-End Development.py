import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

# Read Construction_Contract data

csv_filepath = "~/Desktop/Construction_Contracts.csv"
df_csv = pd.read_csv(csv_filepath)

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







    






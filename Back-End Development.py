#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.groups = []

class Group:
    def __init__(self, group_id, name):
        self.group_id = group_id
        self.name = name
        self.members = []
        self.invoices = []

class Invoice:
    def __init__(self, invoice_id, amount, issuer_id, receiver_id):
        self.invoice_id = invoice_id
        self.amount = amount
        self.issuer_id = issuer_id
        self.receiver_id = receiver_id

# Mock data for demonstration
users = [User(1, "Company A"), User(2, "Company B")]
groups = [Group(1, "Project X"), Group(2, "Project Y")]
invoices = [Invoice(1, 1000, 1, 2), Invoice(2, 500, 2, 1)]

# Function to add members to a group
def add_members_to_group(group, members):
    for member in members:
        if member not in group.members:
            group.members.append(member)
            member.groups.append(group)

# Function to add invoices to a group
def add_invoices_to_group(group, new_invoices):
    for invoice in new_invoices:
        if invoice not in group.invoices:
            group.invoices.append(invoice)

# Function to calculate group balances
def calculate_group_balances(group):
    balance = {}
    for member in group.members:
        balance[member.user_id] = {"owe": 0, "owed": 0}

    for invoice in group.invoices:
        balance[invoice.issuer_id]["owed"] += invoice.amount
        balance[invoice.receiver_id]["owe"] += invoice.amount

    return balance

# Example usage
add_members_to_group(groups[0], users)
add_invoices_to_group(groups[0], invoices)
balances = calculate_group_balances(groups[0])
print(balances)




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







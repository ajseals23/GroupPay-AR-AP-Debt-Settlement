import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('Construction_Contracts.csv')

# print(df.head())


# relationships
contractor_to_vendor_data = df[['contractor_id', 'vendor_id']]
vendor_to_contractor_data = df[['vendor_id', 'contractor_id']]

# graphs
G_contractor_to_vendor = nx.from_pandas_edgelist(contractor_to_vendor_data, 'contractor_id', 'vendor_id', create_using=nx.DiGraph())
G_vendor_to_contractor = nx.from_pandas_edgelist(vendor_to_contractor_data, 'vendor_id', 'contractor_id', create_using=nx.DiGraph())

fig, axes = plt.subplots(1, 2, figsize=(16, 8))

# Contractor to Vendor
axes[0].set_title('Contractor to Vendor Relationships')
pos_contractor_to_vendor = nx.spring_layout(G_contractor_to_vendor)
nx.draw(G_contractor_to_vendor, pos_contractor_to_vendor, with_labels=True, font_size=8,
        node_size=500, font_color='black', node_color='skyblue', edge_color='gray', arrowsize=10, ax=axes[0])

# Vendor to Contractor
axes[1].set_title('Vendor to Contractor Relationships')
pos_vendor_to_contractor = nx.spring_layout(G_vendor_to_contractor)
nx.draw(G_vendor_to_contractor, pos_vendor_to_contractor, with_labels=True, font_size=8,
        node_size=500, font_color='black', node_color='skyblue', edge_color='gray', arrowsize=10, ax=axes[1])

plt.show()



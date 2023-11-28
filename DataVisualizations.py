import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('Construction_Contracts.csv')

print(df.head())

relationship_data = df[['contractor_id', 'vendor_id']]

# Create graph
G = nx.from_pandas_edgelist(relationship_data, 'contractor_id', 'vendor_id', create_using=nx.DiGraph())

# Plot graph
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G)  
nx.draw(G, pos, with_labels=True, font_size=8, node_size=500, font_color='black', node_color='skyblue', edge_color='gray', arrowsize=10)

plt.title('Web of Connections Between Contractors and Vendors')
plt.show()



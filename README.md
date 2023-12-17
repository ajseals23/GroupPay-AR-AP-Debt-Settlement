# GroupPay Data Visualization and Invoice Management

## Overview

GroupPay is a Python project focused on visualizing and managing data from construction contracts. It uses data from two primary sources: `company-ref.csv` and `Construction_Contracts.csv`. The project consists of three main components:

1. **Data Visualization (`DataVisualizations.py`):** This script uses `pandas` for data handling, `networkx` for graph representation, and `matplotlib` for plotting. It provides visual insights into contractor-to-vendor and vendor-to-contractor relationships.

2. **Invoice Settlement (`invoice_settlement.py`):** This script calculates accounts payable and receivable for each vendor and contractor. It provides a console-based interface to display basic accounting information.

3. **User Interface (`UI.py`):** Built using `tkinter` and `PIL`, this script provides a graphical user interface for the application. It allows users to select companies, calculate discounts, and display financial details.

## Data Files

- **`company-ref.csv`:** Contains reference data for companies involved in the construction contracts.
- **`Construction_Contracts.csv`:** Includes detailed contract information between contractors and vendors.

## Installation and Usage

1. **Clone the repository:**
  ```
  git clone [(https://github.com/ajseals23/GroupPay-AR-AP-Debt-Settlement.git)]
  ```

2. **Install required dependencies:**
  ```
  pip install pandas networkx matplotlib Pillow
  ```

3. **Run the scripts:**
- To visualize data:
  ```
  python DataVisualizations.py
  ```
- To manage invoices:
  ```
  python invoice_settlement.py
  ```
- To use the UI:
  ```
  python UI.py
  ```

## Features

### Data Visualization

- Generates two types of network graphs:
- Contractor to Vendor Relationships
- Vendor to Contractor Relationships

### Invoice Settlement

- Calculates and displays total accounts payable and receivable.
- Provides insights into the financial status of contractors and vendors.

### User Interface

- Interactive GUI for selecting companies and calculating discounts.
- Displays detailed financial information for each selected company.

## Contributing

Contributions to the project are welcome. Please follow the standard procedures for contributing to GitHub projects.




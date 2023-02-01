# Section C: Forensics (25 Marks)

import pandas as pd

in_progress = "TBA"

# load both datasets into panda dataframes
employees = pd.read_excel("hr_sorted_data.xlsx")
transactions = pd.read_excel("sorted_txn_dataset.xlsx")

# clean date/time data
employees['Date'] = pd.to_datetime(employees['Date'], dayfirst=True)
transactions['Date'] = pd.to_datetime(transactions['Date'], dayfirst=True)

# remove unnecessary columns
employees.drop(columns='Role')
transactions = transactions.drop(columns=['Approver', 'Role'])

# reorder transactions data to display username first
columns = list(transactions.columns.values)
transactions = transactions[['Date', 'Username', 'Txn_amount']]

# FORENSIC INVESTIGATION ANSWERS

# find all employees with status other than 'active'
inactive_employees = employees.loc[employees['Status'] != "active"]

# save employee usernames to a set
inactive_usernames = set(inactive_employees["Username"])

# find transactions with inactive usernames
fraudulent_transactions = transactions[transactions['Username'].isin(inactive_usernames)]

# sum the total of the txn_amount column
total_amount = fraudulent_transactions['Txn_amount'].sum()

# DISPLAY INFORMATION TO USER

print("\n")
print("-" * 50)
print("{:^50}".format("Forensic Analysis"))
print("-" * 50)

print("{:<35} : {:<}".format("INACTIVE Employees", len(inactive_employees)))
print("-" * 50)
print("{:<35} : {:<}".format("FRAUDULENT Transactions", len(fraudulent_transactions)))
print("{:<35} : {:,.2f}".format("FRAUDULENT Transactions Amount (£)", total_amount))
print("-" * 50)

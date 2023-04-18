# Section C: Forensics (25 Marks)

import pandas as pd

# PREPARE THE DATA

# load in the datasets
employees_df = pd.read_csv("hr_sorted_data.csv")
transactions_df = pd.read_csv("sorted_txn_dataset.csv")

# remove entries with missing data
transactions_df.dropna(inplace=True)

# Convert strings to date
employees_df['Date'] = pd.to_datetime(employees_df['Date'], format='%d/%m/%Y')
transactions_df['Date'] = pd.to_datetime(transactions_df['Date'], format='%d/%m/%Y')

# FORENSIC INVESTIGATION ANSWERS

# find all employees with status other than 'active'
inactive_employees = employees_df.loc[employees_df['Status'] != "active"]

# create a list to store inactive user data
inactive_user_list = []

# extract the inactive usernames and expiry dates
for i in range(len(inactive_employees)):
    inactive_username = inactive_employees.iloc[i, 0]   # extract inactive username
    expiry_date = inactive_employees.iloc[i, 1]         # extract expiry date
    inactive_user = (inactive_username, expiry_date)    # save details to tuple
    inactive_user_list.append(inactive_user)

# convert the list of tuples to a dictionary
inactive_user_dict = dict(inactive_user_list)
# print(inactive_user_dict)

# get dataframe of suspicious transactions
inactive_usernames = set(inactive_employees['Username'])    # set of inactive usernames
suspect_transactions = transactions_df[transactions_df['Username'].isin(inactive_usernames)]

fraudulent_counter = 0  # count the number of fraudulent transactions
fraudulent_amount = 0   # to sum the total of fraudulent transactions

# loop through the suspicious transactions
for i in range(len(suspect_transactions)):
    txn_username = suspect_transactions.iloc[i, 1]
    txn_date = suspect_transactions.iloc[i, 0]
    # the username is used as a key to access the expiry date stored in the inactive employees dictionary
    if txn_date >= inactive_user_dict[txn_username]:
        # print(i, txn_username, txn_date, inactive_user_dict[txn_username])
        fraudulent_counter += 1
        fraudulent_amount += suspect_transactions.iloc[i, 3]


# DISPLAY INFORMATION TO USER

print("\n")
print("-" * 50)
print("{:^50}".format("Forensic Analysis"))
print("-" * 50)

# Question 1
print("{:<35} : {:<}".format("INACTIVE Employees", len(inactive_employees)))
print("-" * 50)

# Question 2
print("{:<35} : {:<}".format("FRAUDULENT Transactions", fraudulent_counter))
print("-" * 50)

# Question 3
print("{:<35} : {:,.2f}".format("FRAUDULENT Transactions Amount (£)", fraudulent_amount))
print("-" * 50)

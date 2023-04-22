# Section B: Encryption (25 Marks)

import pandas as pd
import random


# function for encryption
def password_encryption(text):
    # create the grid that the password goes into
    # "" for i in range(len(text)) creates a grid where num of columns = length of password
    # for j in range(5) creates 5 rows on the grid
    grid = [["" for i in range(len(text))] for j in range(5)]

    # variables to track direction on the grid
    direction = "down"
    row = 0

    # loop to place password into the grid
    for i in range(len(text)):
        grid[row][i] = text[i]
        # if on first row
        if row == 0:
            direction = "down"
        # if on last row
        elif row == 5 - 1:
            direction = "up"

        if direction == "down":
            row += 1
        else:
            row -= 1

    # read letters from grid
    encrypt = []
    for row in range(5):                # for each row
        for col in range(len(text)):    # for each column
            encrypt.append(grid[row][col])  # go across the rows and add letters to the list

    # create encrypted password
    encrypted = "".join(encrypt)    # create a string from the list of letters
    return encrypted


def get_user_detail(field):
    while True:
        user_detail = input(f"\nEnter your {field}: ")

        # if getting a password
        if field == "password":
            if len(user_detail) >= 5 and not user_detail.isspace():
                return user_detail
            else:
                print(f"{field} must be at least 5 characters long!".capitalize())

        # getting anything else
        else:
            if not user_detail or user_detail.isspace():
                print(f"{field} cannot be empty.")
            else:
                return user_detail


# Main Program
print("\n" + "-" * 50)
print("\t\tPress enter to get started!")
input("-" * 50)

while True:
    # get user details
    first_name = get_user_detail("first name")
    surname = get_user_detail("surname")
    password = get_user_detail("password")

    # generate username
    username = ""
    # first 3 letters of first name + last 2 letters of surname + random digit
    username_components = [first_name[0:3], surname[-2:], str(random.randint(10, 99))]
    # add components together
    for each_component in username_components:
        username += each_component
    # convert username to lowercase for uniformity
    username = username.lower()
    print("\nYour username is:", username)

    # encrypt the password
    encrypted_password = password_encryption(password)
    print("Your encrypted password is:", encrypted_password)

    # read csv file
    filename = "users.csv"
    users = pd.read_csv(filename)

    # create a dataframe for user data
    user = {
        "Name": first_name,
        "Surname": surname,
        "Username": username,
        "Encrypted Password": encrypted_password
    }
    user_df = pd.DataFrame([user])

    # add the new data to the existing data
    users = pd.concat([users, user_df], ignore_index=True)

    # save the data back to the file
    users.to_csv(filename, index=False)

    add_new = " "

    while add_new != "x" and add_new != "":
        add_new = input("\nPress enter to add another user or type \"x\" to exit: ")

    if add_new == "x":
        break
    else:
        continue
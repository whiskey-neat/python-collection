# Section B: Encryption (25 Marks)

import pandas as pd


# function for encryption
def password_encryption(text):
    # create the grid to put the password into
    # "" for i in range(len(text)) creates a grid where num of columns = length of password
    # for j in range(5) creates a grid with 5 rows
    grid = [["" for i in range(len(text))] for j in range(5)]

    # track whether we need to go up or down on the grid
    direction = "down"
    row = 0

    # place password into the grid
    for i in range(len(text)):
        grid[row][i] = text[i]
        if row == 0:  # if on first row
            direction = "down"  # place the letters diagonally down
        elif row == 5 - 1:  # if on the last row
            direction = "up"  # place the letters diagonally up
        if direction == "down":  # if going down: move to row below
            row += 1
        else:
            row -= 1  # if going up move to row below

    # create encrypted text
    encrypt = []
    for i in range(5):  # for each row
        for j in range(len(text)):  # for each column
            encrypt.append(grid[i][j])  # go across the rows and add letters to list

    # print encrypted password
    encrypted = "".join(encrypt)  # create a string from the list of letters
    return encrypted

    print("\n" + "-" * 50)
    print("\t\tPress enter to get started!")
    input("-" * 50)


while True:
    # get first name and surname
    first_name = input("\nEnter your first name: ")
    surname = input("Enter your surname: ")

    # get password
    while True:
        password = input("Enter a password: ")

        # password is valid
        if len(password) >= 5:
            break
        # password is invalid
        else:
            print("Password must be at least 5 characters long!")

    # generate username
    username = ""
    # first 3 letters of first name + last 2 letters of surname + length of first name + length of surname
    username_components = [first_name[0:3], surname[0:2], str(len(first_name)), str(len(surname))]
    for each_component in username_components:
        username += each_component

    username = username.lower()  # convert username to lowercase

    print("\nYour username is: " + username)

    # generate encrypted password
    encrypted_password = (password_encryption(password))
    print("Your password is:", encrypted_password)

    add_new = input("Press enter to add another user or enter \"x\" to exit")

    if add_new == "x":
        break

    # read the csv file
    users = pd.read_csv("users.csv")

    # create a dataframe for the user data
    user = {
        "Name": first_name,
        "Surname": surname,
        "Username": username,
        "Password": encrypted_password
    }
    user_df = pd.DataFrame([user])

    # add the new data to the existing data
    users = pd.concat([users, user_df], ignore_index=True)

    # save the data back to the file
    users.to_csv("users.csv", index=False)

    # print the contents of users.csv (testing purposes)
    # with open("users.csv", "r") as users:
    #     lines = users.readlines()
    #     for line in lines:
    #         print(line)

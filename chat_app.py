# Section D: Chat App (10 Marks)
# main menu for Chat App

import os

while True:
    select = input("1. Start the Server\n"
                   "2. Chat\n"
                   "3. Exit\n"
                   "Select an option: ")
    select = int(select)

    if select == 1:
        os.system("start cmd /k server.py")
    if select == 2:
        os.system("start cmd /k client.py")
    if select == 3:
        quit()
# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# <Daniel White>,<11.15.21>,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strFile = 'ToDoList.txt' # data storage file
objFile = None   # file handle
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open(strFile, "r")
for line in objFile:
    lstData = line.split(",")
    dicRow = {"task": lstData[0].strip(), "priority": lstData[1].strip()}
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("Your Current Data is:")
        for row in lstTable:
            print(' ', row["task"], ',', row["priority"], sep='')
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        print("Type in a 'Task' and 'Priority' for your To Do List")
        strTask = str(input("Enter a Task: "))
        strPriority = str(input("Enter a Priority: "))
        dicRow = {"task": strTask, "priority": strPriority}
        lstTable += [dicRow]
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        strData = input("Task to Remove: ")
        for row in lstTable:
            if strData == row["task"]:
                lstTable.remove(row)
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open(strFile, "w")
        for row in lstTable:
            objFile.write(str(row["task"]) + "," + str(row["priority"]) + "\n")
        objFile.close()
        print("The Data was Saved!")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("Your To Do List is Complete")
        break  # and Exit the program

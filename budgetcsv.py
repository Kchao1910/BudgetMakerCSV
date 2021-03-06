# Author: Kenny Chao
# Language: Python 
# Version Supported: 3.7.1
# First Update: 1/6/2019 (Working version)
# Second Update: 1/7/2019 (Added console layout, modularity)
# Third Update: 1/8/2019 (Added ability to update categories, not yet implemented is saving the changes to the file)
# Fourth Update: 1/9/2019 (Added ability to create budget/ expenses for newly created category. Also, added ability to save changes to csv file)
# Project Name: Excel Sheet Budget Maker in Python

import sys
import csv
import os.path
from os import path

# This function determines whether the user entered in a valid month (spelling counts). 
# A valid month in this case would only include those used in the US/Britain.
# Self-reminder: don't forget to implement non-case-sensitive functionality to month checker.
# Need to do: (1) Check if file will be overwritten or not

def monthChecker(Months, MonthName):
    count = 0
    truth = False
    for month in Months:
        if MonthName != month:
            count += 1
            truth = False
        elif MonthName == month and count <= 11:
            truth = True
            break
    if truth == False:
        print("Invalid month, please check your spelling.")
        sys.exit(0)

# This function's primary purpose is to determine the category names, budget, expenses, and total budget left.

def dataGenerator(NumCategories, categoryList, budgetList, expenseList, totalList):
    if NumCategories >= 1:
        for x in range(0, NumCategories):
            cName = input("Category %d: " % (x+1))
            categoryList.append(cName)
        print("---------------------------------------------------------------------------")
        for category in categoryList:
            budget = int(input("Enter in the budget for the %s category: " % category))
            budgetList.append(budget)  
            expense = int(input("Enter in the expenses for the %s category: " % category))
            expenseList.append(expense)
            total = budget - expense
            totalList.append(total)

# This function puts all rows and columns into the right format when writing to a csv file.

def fileOrganizer(NumCategories, categoryList, budgetList, expenseList, totalList, rowList):
    for i in range(0, NumCategories):
        rowList[i+1:i+1] = [[categoryList[i], budgetList[i], expenseList[i], totalList[i]]]

# This function makes it easier to read the console, the negative space used emphasizes different sections of the program

def blockSeparator():
    print("---------------------------------------------------------------------------")

# Functionality is in the name

def printNewline():
    print("\n")

def writeToCSV(csvFileName, rowList):
    with open(csvFileName, 'w', newline = "") as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(rowList)

    csvFile.close()

def newBudget():
    Months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    MonthName = input("What month would you like to set a budget for? ")
    MonthName = MonthName.capitalize()
    monthChecker(Months, MonthName)
    csvFileName = input("Enter in the name you would like to call your file: ")
    csvFileName = csvFileName + ".csv"
    blockSeparator()

    categoryList = []
    budgetList = []
    expenseList = []
    totalList = []
    rowList = [["Categories", "Budget", "Expenses", "Total Left"]]

    NumCategories = int(input("How many categories would you like to set for this month? "))

    # This function's primary purpose is to determine the category names, budget, expenses, and total budget left.

    dataGenerator(NumCategories, categoryList, budgetList, expenseList, totalList)
    blockSeparator()
    # This function puts all rows and columns into the right format to put into a csv file.

    fileOrganizer(NumCategories, categoryList, budgetList, expenseList, totalList, rowList)

    for y in range(0, len(rowList)):
        print(rowList[y])

    blockSeparator()

    # Create a csv file.

    writeToCSV(csvFileName, rowList)

#################################################################################################################3
def validUpdateOption(updateOptions):
    if updateOptions != 1 or updateOptions != 2 or updateOptions != 3:
        print("The option you entered in is not available.")
    else:
        return

def removeCategory(cR, categoryList, budgetList, expenseList, totalList):
    categoryList.remove(categoryList[cR])
    budgetList.remove(budgetList[cR])
    expenseList.remove(expenseList[cR])
    totalList.remove(totalList[cR])

def newCategory(cA, budgetList, expenseList, totalList):
    newBudget = int(input("Enter in the budget for %s: " % cA))
    budgetList.append(newBudget)
    newExpense = int(input("Enter in the expense for %s: " % cA))
    expenseList.append(newExpense)
    newTotal = newBudget - newExpense
    totalList.append(newTotal)

def reUpdate(updateOptions, categoryList, budgetList, expenseList, totalList):
    # For option 1, remember to check if list is empty or not
    if updateOptions == 1:
        categoryChoice = int(input("Choose an option:\n(1) Remove a category\n(2) Add a category\n"))
        blockSeparator()
        if categoryChoice == 1:
            for x in range(0, len(categoryList)):
                category = categoryList[x]
                print("Category %d: %s" % ((x+1),category))
            blockSeparator()
            categoryRemoval = int(input("Enter in the category you want to remove: "))
            if categoryRemoval < 1 or categoryRemoval > x+1:
                print("Option chosen must be one of the above category numbers.")
                sys.exit(0)
            cR = categoryRemoval - 1
            removeCategory(cR, categoryList, budgetList, expenseList, totalList)
            #cR = str(categoryList[categoryRemoval-1]) # This to make sure that the first line is not included (a.k.a. the "variables")
            #categoryList.remove(cR)
            blockSeparator()
        elif categoryChoice == 2:
            cA = input("Enter in the category you would like to add: ")
            categoryList.append(cA)
            newCategory(cA, budgetList, expenseList, totalList)
            blockSeparator()
        else: 
            print("%d is an invalid option." % categoryChoice)
            blockSeparator()
    elif updateOptions == 2:
        numOfCategories(categoryList)
        if len(categoryList) >=1:
            printCategories(categoryList)
            budgetChoice = int(input("Choose the category you would like to update the budget for: "))
            categoryChosen = categoryList[budgetChoice-1]
            budgetUpdate = int(input("Enter in the new budget for %s: " % categoryChosen))
            budgetList[budgetChoice-1] = budgetUpdate
            expense = int(expenseList[budgetChoice-1])
            totalList[budgetChoice-1] = (budgetUpdate - expense)
        else:
            print("Looks like there was a flaw in error checking! Look at updating budget as a start.")
    elif updateOptions == 3:
         numOfCategories(categoryList)
         if len(categoryList) >= 1:
            printCategories(categoryList)
            expenseChoice = int(input("Choose the category you would like to update the expense for: "))
            categoryChosen = categoryList[expenseChoice-1]
            expenseUpdate = int(input("Enter in the new expense for %s: " % categoryChosen))
            expenseList[expenseChoice-1] = expenseUpdate
            budget = int(budgetList[expenseChoice-1])
            totalList[expenseChoice-1] = (budget - expenseUpdate)
    else:
        print("Uh-oh, seems like an error went through.")

# Number of categories
def numOfCategories(categoryList):
    if len(categoryList) == 0:
          print("There is no budget that can be updated because no categories exist.")

# print out number of categories
def printCategories(categoryList):
    x = 1
    for category in categoryList:
        print("Category %d: %s" % (x, category)) 
        x += 1

# Note that when reading from the csv file contents from list become strings
def updateOrganizer():
    csvFileName = input("Enter in the file you would like to update (Ex. 'January 2019.csv'): ")
    fileExists = path.exists(csvFileName)
    blockSeparator()
    if fileExists == True:
        updateOptions = int(input("Choose the area you would like to update:\n(1) Categories\n(2) Budget\n(3) Expenses\n"))
        blockSeparator()
        with open(csvFileName) as csvFile:
            categoryList = []
            budgetList = []
            expenseList = []
            totalList = []
            rowList = []
            csvReader = csv.reader(csvFile, delimiter = ",")
            for row in csvReader:
                rowList.append(row)
            rowList.remove(rowList[0])
            x = 0
            for list in rowList:
                categoryList.append(list[x])
                budgetList.append(list[x+1])
                expenseList.append(list[x+2])
                totalList.append(list[x+3])
        rowList = []
        rowList.append(["Categories", "Budget", "Expense", "Total Left"])
        reUpdate(updateOptions, categoryList, budgetList, expenseList, totalList)
        NumCategories = len(categoryList)
        fileOrganizer(NumCategories, categoryList, budgetList, expenseList, totalList, rowList)
        writeToCSV(csvFileName, rowList)
        print(categoryList)
        print(budgetList)
        print(expenseList)
        print(totalList)
        blockSeparator()
    else:
        print("The file you entered in doesn't exist or cannot be found!")
        blockSeparator()


# User can continue re-using the program until as long as the loop condition is true
def loop(tOrf):
    cont = input("Enter in 'continue' to keep using the program or 'quit' to exit out: ")
    if cont == "continue":
        tOrf = True
    elif cont == "quit":
        sys.exit(0)
    else:
        print("Invalid input")

##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##
# Things in consideration
# (1) Would you like to update an existing file or create a new budget?
# (2) What things would you like to update for "filename"? "Down-down of available options"


tOrf = True
while tOrf == True:
    blockSeparator()
    chooseAnOption = int(input("Choose an option (Enter in the number):\n(1) Update an existing budget\n(2) Create a new budget\n"))
    blockSeparator()
    if chooseAnOption == 1:
        updateOrganizer()
        loop(tOrf)
    elif chooseAnOption == 2:
        newBudget()
        loop(tOrf)
    else:
        print("Invalid choice.")



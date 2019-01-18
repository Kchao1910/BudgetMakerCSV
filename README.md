# BudgetMakerCSV

Project Statement: To design a application that allows users to generate monthly budgets in csv format. 

# Pre-requisites

Python (3.7.1 used)

# Introduction

## __Updating Existing Budgets__
This console application allows users to either update existing budgets or create new budgets that are saved as csv files. When a user decides to update an existing budget, it is assumed that the file they have chosen was made through this program. The reason for this is due to the way stored data is written to the csv file.<br><br>
For example.<br>
<table>
    <tr>
        <th>Categories</th>
        <th>Budget</th>
        <th>Expenses</th>
        <th>Total Left</th>
    </tr>
    <tr>
        <th>Groceries</th>
        <th>200</th>
        <th>100</th>
        <th>100</th>
    </tr>
    <tr>
        <th>Rent</th>
        <th>1000</th>
        <th>800</th>
        <th>200</th>
    </tr>
    <tr>
        <th>Transportation</th>
        <th>250</th>
        <th>175</th>
        <th>75</th>
    </tr>
</table>

All rows except for the first are written in this format:<br> [category name, budget, expenses, total left]<br>


\* Warning: CSV files that are not in this format will not be recognized by the program, thus the program will crash.

After the user chooses to update an existing budget they will be asked to enter in the name of the file they want to upload (Ex. 'January 2019.csv'). Once the user uploads their file they will be ask to choose 1 of 3 options to update (Ex. enter in '1' to update categories in file):
1) Categories
2) Budget
3) Expenses

If a user decides to update categories they can either choose to remove or add a category. If a user decides to update a budget or expenses they must enter in the category number they want to update the budget/expenses for. 

## __Creating New Budgets__
There are 5 main steps in creating a new budget. First, the user chooses the month they would like to set a budget for. Second, the user enters in the name they would like to save the file as (do not include '.csv' at the end of your file). Third, the user enters in how many categories they would like to set (only postive whole numbers are accepted). Fourth, the user then sets the category name, budget, and expenses for all categories. Lastly, the user can choose to either continue to re-use the functions again or quit the program.

# Project Goals
1) CSV file generated (Complete)
2) Error Checking (In Progress)
3) Direction Manual (In Progress)

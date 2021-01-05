# Create a Python script that analyzes the records to calculate each of the following
    # Total number of months included in the dataset
    # Net total amount of "Profit/Losses" over the entire period
    # Changes in "Profit/Losses" over the period, then find the average of those changes
    # Greatest increase in profits (date and amount) over the entire period
    # Greatest decrease in losses (date and amount) over the entire period

#Final script should both print the analysis to the terminal and export a text file with the results

#import os and csv modules
import os
import csv

# set file path for csv
pyBank_csv = os.path.join("resources", "02-Homework_03-Python_PyBank_Resources_budget_data.csv")

def f(bank_data):
    #assign variable names
    date = str(bank_data[0])
    pnl = int(bank_data[1])

# set total_months count to 0 at start of loops below
total_months = 0

# open csv, read csv with delimiter as comma and print the header row
with open(pyBank_csv, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_file)
    print(f"Header: {csv_header}")
    
    #calculate total months in data set by looping through rows and adding 1 each time
    for row in csv_reader:
        total_months += 1
        print(total_months)
# Create a Python script that analyzes the records to calculate each of the following
# Total number of months included in the dataset
# Net total amount of "Profit/Losses" over the entire period
# Changes in "Profit/Losses" over the period, then find the average of those changes
# Greatest increase in profits (date and amount) over the entire period
# Greatest decrease in losses (date and amount) over the entire period

# Final script should both print the analysis to the terminal and export a text file with the results

# import os and csv modules
import os
import csv

# set file path for csv
pyBank_csv = os.path.join(
    "resources", "02-Homework_03-Python_PyBank_Resources_budget_data.csv")

# def f(bank_data):
#     #assign variable names
#     date = str(bank_data[0])
#     pnl = int(bank_data[1])

# set total_months count to 0 for start of loops below
# total_months = 0
# set total_pnl count to 0 for start of loops below
# total_pnl = 0

# capture all pnl changes in a dictionary and months in dictionary
all_pnl_changes = []
total_months = []
net_pnl = []

# open csv, read csv with delimiter as comma and print the header row
with open(pyBank_csv, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    # set starting pnl difference to 0 for start of loops below
    # set a starting reference for previous row as 0 for start of loops below. Each loop will then reference the previous row accurately to calculate the difference between it and the current row the loop is on
    pnl_change = 0
    previous_row = 867884

    # calculate total months in data set by looping through rows and adding 1 each time
    for row in csv_reader:
        total_months.append(row[0])
        # total_months += 1
        # print(total_months)

        # calculate total profit and losses (total_pnl) of data set
        # net_pnl = (net_pnl + int(row[1]))
        # print(total_pnl)
        net_pnl.append(int(row[1]))

        # calculate changes in pnl over data set and find average
        # find difference in pnl value between each row
        pnl_change = (int(row[1]) - previous_row)
        # print(pnl_change)
        # append all_pnl_changes list to use pull average later
        all_pnl_changes.append(pnl_change)
        # print(all_pnl_changes)

        # is there a better way of doing this, or will this suffice for the purpose of the homework, setting the intitital previous_row to equal the value of the first month's pnl?

        # sets new previous row reference value for calculation of pnl_change
        previous_row = int(row[1])
    
        #calculate ave_pnl_changes over data set
        # ave_pnl_changes = sum(all_pnl_changes) / len(pnl_change)
        # print(ave_pnl_changes)

        ## Use .index to compare the values in lists

        # Identify month associated with greatest increase value
        month_greatest_increase = all_pnl_changes.index(max(all_pnl_changes))

        # Identify month associated with greatest decrease value 
        month_greatest_decrease = all_pnl_changes.index(min(all_pnl_changes))


    print(f"Total Months: {len(total_months)}")
    print(f"Total Profits and Losses: {sum(net_pnl)}")
    print(f"Greatest Monthly Increase: {max(all_pnl_changes)}")
    print(f"Greatest Monthly Decrease: {min(all_pnl_changes)}")
    ## print(all_pnl_changes)
    print(f"Average Monthly Change: {sum(all_pnl_changes)/len(all_pnl_changes)}")
    print(month_greatest_increase)
    print(month_greatest_decrease)

    

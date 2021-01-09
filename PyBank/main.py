# import necessary modules
import os
import csv

# set file path for csv
pyBank_csv = os.path.join(
    "resources", "02-Homework_03-Python_PyBank_Resources_budget_data.csv")

# set up lists to store data from loops below
all_pnl_changes = []
total_months = []
net_pnl = []

# open and perform analysis on election data file
with open(pyBank_csv, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # skip/store header row to start data looping at first month of data
    csv_header = next(csv_file)

    # skip/store first month to avoid miscalculation of average changes
    january = next(csv_reader)
    
    #set initial previous row to first month of data
    previous_row = int(january[1])

    # loop through data set and store all values in lists for later calculations
    for row in csv_reader:
        # append lists for later calculations
        total_months.append(row[0])
        net_pnl.append(int(row[1]))

        # find difference in pnl value between each row
        pnl_change = (int(row[1]) - previous_row)
        # append all_pnl_changes list for later calculations
        all_pnl_changes.append(pnl_change)

        # sets new previous row reference value for calculation of pnl_change
        previous_row = int(row[1])

    # Identify month associated with greatest increase value from appended lists
    month_greatest_increase = all_pnl_changes.index(max(all_pnl_changes))

    # Identify month associated with greatest decrease value from appended lists
    month_greatest_decrease = all_pnl_changes.index(min(all_pnl_changes))

# assign variable with financial analysis results to reference in a print statement to terminal and print in text file
bank_results = (f"Financial Analysis\n----------\nTotal Months: {len(total_months)+1}\nTotal Profits and Losses: ${sum(net_pnl)+int(january[1])}\nAverage Monthly Change: ${round(sum(all_pnl_changes)/len(all_pnl_changes),2)}\nGreatest Monthly Increase: {total_months[month_greatest_increase]} (${max(all_pnl_changes)})\nGreatest Monthly Decrease: {total_months[month_greatest_decrease]} (${min(all_pnl_changes)})")

# print to terminal
print(bank_results)

# create new text file with analysis results
output_file = os.path.join("analysis","bank_results.txt")

#write analysis results to new text file
with open(output_file, "w") as txt_file:
    txt_file.write(bank_results)

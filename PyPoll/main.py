# calculate total number of votes cast
# Create a list of unique candidates who received votes
# Calculate percentage of votes each candidate received of the total votes cast
# Calculate the total number of votes each candidate received of the total votes cast
# Who won the election based on popular vote? Whoe has the highest number or votes?

import os
import csv

# set file path for csv
pyPoll_csv = os.path.join("resources","02-Homework_03-Python_PyPoll_Resources_election_data.csv")

with open(pyPoll_csv, newline = '') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")

    #skip header row
    csv_header = next(csv_file)
    print(csv_header)

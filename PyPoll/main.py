# calculate total number of votes cast
# Create a list of unique candidates who received votes
# Calculate percentage of votes each candidate received of the total votes cast
# Calculate the total number of votes each candidate received of the total votes cast
# Who won the election based on popular vote? Whoe has the highest number or votes?

import os
import csv

#set total_votes tracker to 0 for start of loop
total_votes=0
unique_candidates = []
candidate_votes = {}
# dictionary needs to include candidate_name: "", candidate_votes:

# set file path for csv
pyPoll_csv = os.path.join("resources","02-Homework_03-Python_PyPoll_Resources_election_data.csv")

with open(pyPoll_csv, newline = '') as election_data:
    csv_reader = csv.reader(election_data, delimiter = ",")

    #skip header row
    csv_header = next(election_data)
    print(csv_header)

    for row in csv_reader:

        # assign column index names for readibility
        voter_id = row[0]
        county_name = row[1]
        candidate_name = row[2]

        #append total_votes list
        total_votes= total_votes + 1

        #append unique_candidate list
        if candidate_name not in unique_candidates:
            unique_candidates.append(candidate_name)
            candidate_votes[candidate_name] = 0
        
        # find a way to create a dictionary and/or list that collects occurrences of candidate names and adds one to a vote count for each candidate
        # have: list of unique candidates
        # need: dictionary of votes per candidate on list
        #need to add candidate to dictionary of votes for each candidate
        if candidate_name in unique_candidates:
            candidate_votes[candidate_name] + 1

    print(total_votes)
    print(unique_candidates)
    print(candidate_votes)
    





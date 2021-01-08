
import os
import csv

#set total_votes tracker to 0 for start of loop
total_votes=0

# list to store unique candidate names as iterating through loops
unique_candidates = []
# dictionary to store vote tallies per candidate as iterating through loops
candidate_votes = {}

# set file path for csv
pyPoll_csv = os.path.join("resources","02-Homework_03-Python_PyPoll_Resources_election_data.csv")

with open(pyPoll_csv, newline = '') as election_data:
    csv_reader = csv.reader(election_data, delimiter = ",")

    #skip header row
    csv_header = next(election_data)
    
    # start looping through rows to collect data
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
        
        candidate_votes[candidate_name] += 1

    # print election results available from this iterative loop
    print("Election Results")
    print("--------------------")
    print(F"Total Votes: {total_votes}")
    print("--------------------")
    print(f"Vote Tally:")

    # pull the candidate votes out of the cadidate dictionary and calculate the percentage of the total votes
    for candidate in candidate_votes:
        percentage_votes = candidate_votes.get(candidate)
        print(f"{candidate}: {round((percentage_votes/total_votes)*100,2)}% ({percentage_votes})")
    

    # print remaining results
    print("--------------------")
    winning_votes = max(candidate_votes, key=candidate_votes.get)
    print(f"Winner: {winning_votes}")
    print("---------------------")



#set variable output file
output_file = os.path.join("election_results.txt")

with open(output_file, "w") as txt_file:

    election_results = (
        f"Election Results\n----------------\nTotal Votes: {total_votes}\n----------------\nVote Tally:\n{candidate_votes}\n----------------\nWinner: {winning_votes}\n----------------"
    )
    print(election_results)
    txt_file.write(election_results)

        
    
    





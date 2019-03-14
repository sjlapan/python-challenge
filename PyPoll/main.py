
# Load required packages

import os
import csv

# Set working directory

os.chdir("D:/DU_Bootcamp/code/python-challenge/PyPoll")

# Import .csv file

poll_csv = os.path.join("D:/DU_Bootcamp/code/python-challenge/PyPoll", "election_data.csv")

# Create function to tally votes

def vote_counter(candidate_index, vote_list):
    # @TODO Trying to automatically extract values of candidate list
    # to use as variables set to integer values...
    # create a list of zero values equal to the length of the candidate list
    # Create a dictionary to append vote counts to
    tally = dict.fromkeys(candidate_index, 0)
    for vote in vote_list:
        for key in tally:
            if key == vote:
                tally[key] += 1
    print(tally)



with open(poll_csv, newline = "") as poll_data:
    reader = csv.reader(poll_data, delimiter = ",")
    header = next(poll_data)
    # Extract elements for analysis to empty lists
    # @TODO voter_list is redundant, remove
    voter_list = []
    candidate_list = []
    total_vote = []
    # Collect all unique candidates and voter IDs
    for row in reader:
        voter_list.append(row[0])
        total_vote.append(row[2])
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
    vote_counter(candidate_list, total_vote)        

print(f"There are {len(voter_list)} unique voters.")
print(f"There are {len(candidate_list)} candidates.")
print(candidate_list)
print(f"There are {len(total_vote)} votes cast.")
       

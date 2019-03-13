
# Load required packages

import os
import csv

# Set working directory

os.chdir("D:/DU_Bootcamp/code/python-challenge/PyPoll")

# Import .csv file

poll_csv = os.path.join("D:/DU_Bootcamp/code/python-challenge/PyPoll", "election_data.csv")

with open(poll_csv, newline = "") as poll_data:
    reader = csv.reader(poll_data, delimiter = ",")
    header = next(poll_data)
    # Extract elements for analysis
    voter_list = []
    candidate_list = []
    # Collect all unique candidates and voter IDs
    for row in poll_data:
        if str(row[2]) not in candidate_list:
            candidate_list.append(str(row[2]))
    for row in poll_data:
        if str(row[0]) not in voter_list:
            voter_list.append(str(row[0]))

print(f"There are {len(voter_list)} unique votes.")
print(f"There are {len(candidate_list)} candidates.")
print(candidate_list)        

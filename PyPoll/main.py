
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
    # Extract elements for analysis to empty lists
    voter_list = []
    candidate_list = []
    # Collect all unique candidates and voter IDs
    for row in reader:
        voter_list.append(row[0])
        if str(row[2]) not in candidate_list:
            candidate_list.append(str(row[2]))
            

print(f"There are {len(voter_list)} unique voters.")
print(f"There are {len(candidate_list)} candidates.")
print(candidate_list)
       

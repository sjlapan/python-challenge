
# Load required packages

import os
import csv

# Set working directory

os.chdir("D:/DU_Bootcamp/code/python-challenge/PyPoll")

# Import .csv file

poll_csv = os.path.join("D:/DU_Bootcamp/code/python-challenge/PyPoll", "election_data.csv")

with open(poll_csv, newline = "") as poll_data:
    reader = csv.reader(poll_data, delimiter = ",")

import csv
import os

budget_csv = os.path.join("D:/DU_Bootcamp/code/python-challenge/PyBank", "budget_data.csv")

# Create variables to store the total values 
total_months = 0
net_change = 0
# Create lists for storing column headers and rows
header = []
rows = []

with open (budget_csv, newline = "") as budget:
    reader = csv.reader(budget, delimiter = ",")
    header = next(budget)
    for row in reader:
        rows.append(row)
    # Check the number of months stored in rows at the end of the loop
    print(f"There are {len(rows)} months in the table.")

# Check to make sure the headers were stored properly
print(header)
print(rows)
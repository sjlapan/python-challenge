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
print("Financial Analysis")
print("------------------------")
print(f"Total Months: {len(rows)}")


# Calculate net profit change
for month in rows:
    net_change += int(month[1])
print(f"Total: ${net_change}")

# Get the maximum and minimum profit/losses values
def max_profit(list):
    maximum = list[0]
    for row in list:
        if row[1] > maximum[1]:
            maximum = row
    print(f"Greatest Increase in Profits: {maximum} ")
    return maximum

def min_profit(list):
    minimum = list[0]
    for row in list:
        if row[1] < minimum[1]:
            minimum = row
    print(f"Greatest Decrease in Profits: {minimum} ")
    return minimum

#
max_profit(rows)
min_profit(rows)
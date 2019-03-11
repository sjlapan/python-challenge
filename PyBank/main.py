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
def total_profit(list):
    net_change = 0
    for row in list:
        net_change += int(row[1])
    print(f"Total: ${net_change}")
    return net_change

total_profit(rows)

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

def avg_profit_change(list):
    avg_change = (total_profit(list)/len(list)) * 100
    print(f"Average Change: ${avg_change}")

# Print out summary values
avg_profit_change(rows)
max_profit(rows)
min_profit(rows)
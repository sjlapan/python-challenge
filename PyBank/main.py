import csv
import os

budget_csv = os.path.join("D:/DU_Bootcamp/code/python-challenge/PyBank", "budget_data.csv")




with open (budget_csv, newline = "") as budget:
    reader = csv.reader(budget, delimiter = ",")
    # Store elements of the file in lists
    profit_loss = []
    profit_loss_change = []
    date = []
    header = next(budget)
    
    for row in reader:
        profit_loss.append(float(row[1])),
        date.append(row[0])
    print ("Financial Analysis")
    print("------------------------")
    print(f"Total Months: {len(date)}")
    print(f"Total: ${int(sum(profit_loss))}")
    for i in range(1, len(profit_loss)):
        profit_loss_change.append(profit_loss[i] - profit_loss[i-1])
    avg_change = sum(profit_loss_change)/len(profit_loss_change)
    min_change = min(profit_loss_change)
    max_change = max(profit_loss_change)
    #store the dates for the max and min in the dates list using index of max and min
    max_date = str(date[(profit_loss_change.index(max(profit_loss_change)) + 1)])
    min_date = str(date[(profit_loss_change.index(min(profit_loss_change)) + 1)])
    print(f"Average Change: ${round(avg_change, 2)}")
    print(f"Greatest Increase in Profits: {max_date} (${int(max_change)})")
    print(f"Greatest Decrease in Profits: {min_date} (${int(min_change)})")

# Specify where to save .txt file
os.chdir("D:/DU_Bootcamp/code/python-challenge/PyBank")

# Create a list of lines to write to the .txt file
text_list = []

text_list.append("Financial Analysis")
text_list.append("------------------------")
text_list.append(f"Total Months: {len(date)}")
text_list.append(f"Total: ${int(sum(profit_loss))}")
text_list.append(f"Average Change: ${round(avg_change, 2)}")
text_list.append(f"Greatest Increase in Profits: {max_date} (${int(max_change)})")
text_list.append(f"Greatest Decrease in Profits: {min_date} (${int(min_change)})")

file = open("budget_summary.txt", "a")
file.writelines()
file.close()



import csv
import os

budget_csv = os.path.join("D:/DU_Bootcamp/code/python-challenge/PyBank", "budget_data.csv")

with open (budget_csv, newline = "") as budget:
    reader = csv.reader(budget, delimiter = ",")
    header = next(budget)
     
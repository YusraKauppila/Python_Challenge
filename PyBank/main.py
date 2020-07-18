import csv
import os

budget_csv = r"/Users/yusrakauppila/Desktop/Python_Challenge/PyBank/Resources/budget_data.csv" 

with open(budget_csv) as csvfile:
    csvreader=csv.reader(csvfile)

    csvheader=next(csvreader)

    print(csvheader)
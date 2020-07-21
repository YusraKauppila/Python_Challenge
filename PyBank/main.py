import csv
import os


budget_csv = r"/Users/yusrakauppila/Desktop/Python_Challenge/PyBank/Resources/budget_data.csv" 
analysis_txt = r"Analysis/PyBank.txt"

with open(budget_csv, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    csvheader = next(reader)
    print(csvheader)

    
    months = []
    total = []
    average = []
    monthsList = []
    change = []
    previous = 0

        #total = sum(float(row[1]) for row in rows)

    for row in reader:

        total.append(int(row[1]))
        final_total = sum(total)
        totalAsFormattedString = '${:}'.format(final_total)
        months.append(row[0])
        # total = sum(float(row["Profit/Losses"]) for row in reader)
        # totalAsFormattedString = '${:,.2f}'.format(total)

        diff = int(row[1]) - int(previous)
        previous = row[1]
        change.append(diff)

    zipped = zip(months, change)
    zipped_lst = list(zipped)
    change.remove(change[0])
    zipped_lst.remove(zipped_lst[0])

    # The total number of months included in the dataset

    total_months= len(months)

# #     # The net total amount of "Profit/Losses" over the entire period

    increase = max(change)
    increaseAsFormattedString = '${:}'.format(increase)

    decrease = min(change)
    decreaseAsFormattedString = '${:}'.format(decrease)

    average = sum(change) / len(change)
    amountAsFormattedString = '${:.2f}'.format(average)

    month_decrease = 0

    month_increase = 0

for row in zipped_lst:
    if row[1] == increase:
        month_increase = row[0]
    if row[1] == decrease:
        month_decrease = row[0]

#  *** everything above this line works ***
# with open(budget_csv) as csvfile:
#     reader = csv.DictReader(csvfile)

#     total = sum((row[1]) for row in reader)

# #                                 # FOR EXAMPLE
# #                             # Financial Analysis
# #                        # ----------------------------
# #                             # Total Months: 86
# #                             # Total: $38382578
# #                             # Average  Change: $-2315.12
# #                             # Greatest Increase in Profits: Feb-2012 ($1926159)
# #                             # Greatest Decrease in Profits: Sep-2013 ($-2196167)

print("Financial Analysis")
print("____________________________")
print("Total Months:", (total_months))
print("Total:", (totalAsFormattedString))
# # # #     # #this ^^^ returns the total but does not give a dollar sign. Consider formatting the row maybe.
print("Average Change:", (amountAsFormattedString))
# # # #     # #this ^^^ returns an amount but doesn't match the example above. Consider formatting to 2 decimal places
print("Greatest Increase in Profits: "+month_increase + " " + (increaseAsFormattedString))
print("Greatest Decrease in Profits: "+month_decrease + " " + (decreaseAsFormattedString))
#     #^^^ figure out how to print the associated date (row[0]) with the number
# # final script should both print the analysis to the terminal and export a text file with the results.
#print("Total:", int(total))

f= open("analysis_txt", "w")

print("Financial Analysis", file=f)
print("____________________________", file=f)
print("Total Months:", (total_months), file=f)
print("Total:", (totalAsFormattedString), file=f)
print("Average Change:", (amountAsFormattedString), file=f)
print("Greatest Increase in Profits: "+month_increase + " " + (increaseAsFormattedString), file=f)
print("Greatest Decrease in Profits: "+month_decrease + " " + (decreaseAsFormattedString), file=f)
f.close()


# Modules
import os
import csv

# Set path for file
csvpath = os.path.join('.','PyBank_Resources_budget_data.csv')

total_month = 0
with open(csvpath, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    total_month = sum(1 for row in csvreader)
    print('Financial Analysis')
    print('----------------------------')
    print("Total Months: " + str(total_month))

sum_pandl = 0 
max_profit = 0
max_loss = 0
max_profit_month = ''
max_loss_month = ''
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        curr = int(row[1])
        sum_pandl = sum_pandl + curr
        if curr > max_profit:
            max_profit_month = row[0]
            max_profit = curr
        if curr < max_loss:
            max_loss_month = row[0]
            max_loss = curr
        avg_change = sum_pandl/total_month
    print("Avg Change: " +str(avg_change))
    print('Total Profit and Loss is '+ str(sum_pandl))
    print('Greatest Profit: ' + repr(max_profit) +' on ' + max_profit_month)
    print('Greatest Loss: ' + repr(max_loss) + ' on ' + max_loss_month)
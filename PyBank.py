import os 
import csv

# set the path for the csv file
file_path = r"c:\Users\kyled\AppData\Local\Temp\Temp1_Starter_Code (7).zip\Starter_Code\PyBank\Resources\budget_data.csv"

# create empty lists to store data
dates = []
profits_losses = []
profit_changes = []

# read the csv file and extract data
with open(file_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)  # skip the header row
    for row in csvreader:
        dates.append(row[0])
        profits_losses.append(int(row[1]))

# calculate the total number of months included in the dataset  
total_months = len(dates)         

print (len(dates))

# calculate the net total amount of "Profit/Losses" over the entire period  
net_total = sum(profits_losses)

print(sum(profits_losses))

# calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
#for i in range(len(profits_losses)-1):
    #profit_changes.append(profits_losses[i+1]-profits_losses[i])
#average_change = round(sum(profit_changes)/len(profit_changes),2)


for i in range(1, len(profits_losses)):
    profit_changes.append(profits_losses[i] - profits_losses[i-1])

# calculate the average change in profits/losses over the entire period
average_change = sum(profit_changes) / len(profit_changes)

print(sum(profit_changes) / len(profit_changes))

# find the greatest increase and decrease in profits/losses
greatest_increase = max(profit_changes)


print(max(profit_changes))


greatest_decrease = min(profit_changes)

print(min(profit_changes))

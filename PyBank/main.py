#Pybank
#import stuff needed
import csv 
import os

#make file path and open file
csvpath = os.path.join("Resources", "budget_data.csv")
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
#initialize variables
    header = next(csvreader)
    num_months = 0
    total_profit = 0.0
    delta = []
    greatest_profit = 0.0
    greatest_profit_month = ""
    greatest_loss = 0.0
    greatest_loss_month = ""
    #x is a storage variable for calulating the profil/loss change
    x = 0.0
#loop through each row and do the calculations
    for row in csvreader:
        total_profit += float(row[1])
        delta.append(float(row[1])-x)
        x = float(row[1])
        if delta[num_months] > greatest_profit:
            greatest_profit = delta[num_months]
            #this month thing could be a bit off
            greatest_profit_month = row[0]
        elif delta[num_months] < greatest_loss:
            greatest_loss = delta[num_months]
            #this month thing could be a bit off
            greatest_loss_month = row[0]
        num_months += 1

#calculate average of profit change
#i feel like this calculation will need work

y = 0
for x in range(85):
    a = delta[x+1]
    y = y + a
    average_change = y/(num_months-1)

print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(num_months))
print("Total: " + str(total_profit))
print("Average Change: $" + str(average_change))
print("Greatest Increase in Profits: " + greatest_profit_month + "(" + str(greatest_profit) + ")")
print("Greatest Decrease in Profits: " + greatest_loss_month + "(" + str(greatest_loss) + ")")

#export file
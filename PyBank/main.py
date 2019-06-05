import os
import csv

csvpath = os.path.join('..', 'PyBank/Resources','budget_data.csv')

months = []
amount = []
amount_change = []

with open(csvpath, newline='', encoding = 'UTF-8') as csvfile:

    csvreader = csv.reader(csvfile, delimiter= ',')

    print(csvreader)

    csv_header = next(csvreader)

    for row in csvreader:

        months.append(row[0])
        
        amount.append(int(row[1]))

    for x in range(1, len(amount)):

        amnt_chg = int(amount[x]) - int(amount[x-1])

        amount_change.append(amnt_chg)

# total number of months
total_months = len(months)

# net total amount of P/L
net_amount = sum(amount) 

# average of changes in P/L
amnt_chg_avg = sum(amount_change) / len(amount_change)

# greatest increase in P
greatest_increase = max(amount_change)

# greates decrease in L
greatest_decrease = min(amount_change)

# print summary
print("Financial Analysis")
print("----------------------------")
print(f"Total Month: {total_months}")
print(f"Total: {net_amount}")
print(f"Average Change: {amnt_chg_avg}")
print("Greatest Increase in Profits: " + str(months[amount_change.index(max(amount_change))+1]) + " ($" + str(greatest_increase) + ")")
print("Greatest Decrease in Profits: " + str(months[amount_change.index(min(amount_change))+1]) + " ($" + str(greatest_decrease) + ")")

# create text file and export summary
export_file = open("bank_results.txt","w")

export_file.write("Financial Analysis \n")
export_file.write("---------------------------- \n")
export_file.write(f"Total Month: {total_months} \n")
export_file.write(f"Total: {net_amount} \n")
export_file.write(f"Average Change: {amnt_chg_avg} \n")
export_file.write("Greatest Increase in Profits: " + str(months[amount_change.index(max(amount_change))+1]) + " ($" + str(greatest_increase) + ")\n")
export_file.write("Greatest Decrease in Profits: " + str(months[amount_change.index(min(amount_change))+1]) + " ($" + str(greatest_decrease) + ")\n")

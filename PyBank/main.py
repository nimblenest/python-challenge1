import os
import csv

budget_data_csv = os.path.join('C:/','Users','lukeb','python-challenge1','PyBank','Resources','budget_data.csv')

total_months = 0
total_profit_losses = 0
previous_profit_loss = 0
profit_losses_changes = []
dates = []

with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=",")

    csv_header = next(csv_file)

    for line in csv_file:
        data = line.strip().split(',')
        date = data[0]
        profit_loss = int(data[1])
        
        total_months += 1
        
        total_profit_losses += profit_loss
        
        if total_months > 1:
            profit_loss_change = profit_loss - previous_profit_loss
            profit_losses_changes.append(profit_loss_change)
            dates.append(date)
        
        previous_profit_loss = profit_loss

average_change = sum(profit_losses_changes) / len(profit_losses_changes)

max_increase = max(profit_losses_changes)
max_increase_index = profit_losses_changes.index(max_increase)
max_increase_date = dates[max_increase_index]

max_decrease = min(profit_losses_changes)
max_decrease_index = profit_losses_changes.index(max_decrease)
max_decrease_date = dates[max_decrease_index]

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses:.0f}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {max_increase_date} (${max_increase:.0f})")
print(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease:.0f})")

 
with open("financial_analysis.txt", "w") as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("----------------------------\n")
    txt_file.write(f"Total Months: {total_months}\n")
    txt_file.write(f"Total: ${total_profit_losses:.0f}\n")
    txt_file.write(f"Average Change: ${average_change:.2f}\n")
    txt_file.write(f"Greatest Increase in Profits: {max_increase_date} (${max_increase:.0f})\n")
    txt_file.write(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease:.0f})\n")

    
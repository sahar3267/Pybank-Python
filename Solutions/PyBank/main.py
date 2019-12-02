# import dependencies
import csv
import os

# input file path
input_file = os.path.join("Resources", "budget_data.csv")

# output file path
output_file = os.path.join("Analysis", "budget_analysis.txt")

# define variables to keep track of analysis
total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = [0, 0]
greatest_decrease = [0, 0]
total_net = 0

# read the csv and do stuff
with open(input_file, "r") as financial_data:
    reader = csv.reader(financial_data, delimiter=',')

    # read the header row
    header = next(reader)

    # start our calculations
    first_row = next(reader)
    total_months = total_months + 1
    total_net = total_net + int(first_row[1])
    prev_net = int(first_row[1])

    for row in reader:

        # Keep track of the totals
        total_months = total_months + 1
        total_net = total_net + int(row[1])

        # Keep track of the net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list = net_change_list + [net_change]
        month_of_change = month_of_change + [row[0]]

        # Calculate the greatest increase
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        # Calculate the greatest decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

# Calculate the Average Net Change
net_monthly_avg = sum(net_change_list) / len(net_change_list)


# Generate Output Summary
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average  Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print the output (to terminal)
print(output)

# Export the results to text file
with open(output_file, "w") as txt_file:
    txt_file.write(output)


# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv
os.chdir(os.path.dirname(os.path.abspath(__file__)))

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

#found = False
#unique_months = set()
lastmonth = 0
diff = 0
counter = 0
finalavg = 0
finaltotal = 0
sum =0
cnt_months = 0
Greatest_in_profit = []
greatest_increase = 0
greatest_decrease = 0

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    hdr = next(csvfile)
    
    print(hdr)
    # TO find the  difference and 
    for row in csvreader:
      
      cnt_months  = cnt_months + 1
      sum  = sum + int(row[1])
      diff = int(row[1]) - int(lastmonth)
      Greatest_in_profit.append(diff)
      if diff > greatest_increase:
        greatest_increase = diff
        greatest_increase_month = row[0]
      if diff < greatest_decrease:
        greatest_decrease = diff
        greatest_decrease_month = row[0]
        
      
      if ( lastmonth != 0 ):
        counter = counter + 1
        finaltotal = finaltotal + diff
             
      lastmonth = row[1]
finalavg = round(finaltotal/counter ,2)
print(f' Final Average : ${finalavg}')
print(f'Total months : {cnt_months}')
     
print(f'Total profit/Losses: ${sum}')
print(f'Greatest increase in profits:{(greatest_increase_month)} ${(greatest_increase)} ')

print(f'Greatest decrease in profits:  {(greatest_decrease_month)} ${(greatest_decrease)}')


output_path = os.path.join("..", "Analysis", "Budget_Results.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w',newline="") as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)

    csvwriter.writerow(['Financial analysis'])

    # Write the second row
    
    csvwriter.writerow(['---------------------------------------'])
    csvwriter.writerow ([f'Total months : {cnt_months}'])
    csvwriter.writerow([f'Final Average : ${finalavg}'])
    csvwriter.writerow ([f'Total profit/Losses: ${sum}'])
    csvwriter.writerow  ([f'Greatest increase in profits: {(greatest_increase_month)} ({(greatest_increase)})'])
    csvwriter.writerow ([f'Greatest decrease in profits: {(greatest_decrease_month)} ({(greatest_decrease)})'])
    
  
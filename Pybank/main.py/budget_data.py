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

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    hdr = next(csvfile)
    
    print(hdr)
    
    for row in csvreader:
       
      #print(row)
      cnt_months  = cnt_months + 1
      sum  = sum + int(row[1])
      diff = int(row[1]) - int(lastmonth)
      Greatest_in_profit.append(diff)
      #print(lastmonth)
      if ( lastmonth != 0 ):
        counter = counter + 1
        finaltotal = finaltotal + diff
      
       # print(counter)

     
        #unique_months.add(row[0]) 
        #cnt_months  = cnt_months + 1
        
        #sum  = sum + int(row[1])
       
        #print(row)
      lastmonth = row[1]
#total_unique_months = len(unique_months)
finalavg = round(finaltotal/counter ,2)
print(f' Final Average : {finalavg}')
print(f'Total months : {cnt_months}')
       
#print(f' Total Months: {total_unique_months}')
#print(total_unique_months)
print(f'Total profit/Losses: {sum}')
print(f'Greatest increase in profits: {(max(Greatest_in_profit))}')
print(f'Greatest decrease in profits: {(min(Greatest_in_profit))}')
output_path = os.path.join("..", "Analysis", "BudgetAnalysis.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Financial analysis'])

    # Write the second row
    csvwriter.writerow(['---------------------------------------'])
    csvwriter.writerow([' Final Average : -2315.12'])
    csvwriter.writerow (['Total Months: 85'])
    csvwriter.writerow (['Total profit/Losses: 38382578'])
    csvwriter.writerow (['Greatest increase in profits: 1926159'])
    csvwriter.writerow  (['Greatest decrease in profits: -2196167'])
  
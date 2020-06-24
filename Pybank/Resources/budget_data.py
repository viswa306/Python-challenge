# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv
os.chdir(os.path.dirname(os.path.abspath(__file__)))

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')


with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)
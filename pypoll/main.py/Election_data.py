# Module for reading CSV files
import csv
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    hdr = next(csvfile)
    Candidate_unique_list = []   
    Candidate_Vote_cnt = []
    Candidate_Vote_percent = 0 
    vote_percent = []
    total_vote_cnt = 0
    max_vote = 0
    winner = []
    y = 0
    #loop  to find the unique  names and index of the voters
    for row in csvreader:
        total_vote_cnt = total_vote_cnt + 1
        Candidate_in = (row[2])
        if Candidate_in in Candidate_unique_list:
         Candidate_index  = Candidate_unique_list.index(Candidate_in)
         
         Candidate_Vote_cnt[Candidate_index] = Candidate_Vote_cnt[Candidate_index] + 1
        else:
                Candidate_unique_list.append(Candidate_in) 
                Candidate_Vote_cnt.append(1) 
     # loop to find the voter percentages          
    for x in Candidate_Vote_cnt:
       Candidate_Vote_percent  = round(x / total_vote_cnt * 100, 0)
       vote_percent.append(Candidate_Vote_percent)
     
    max_vote = max(Candidate_Vote_cnt)
    Candidate_index  = Candidate_Vote_cnt.index(max_vote)
    winner = Candidate_unique_list[Candidate_index]   
      
    
print(f'Total votes:{total_vote_cnt}')
print(f'{Candidate_unique_list}')
print(f'{Candidate_Vote_cnt}')
print(f'{vote_percent}')
print(f' Winner:     {winner}')

# Set variable for output file
output_path = os.path.join("..", "Analysis", "pollAnalysis.txt")

#  Open the output file
with open(output_path, "w",  newline = "" , encoding='utf-8') as datafile:
    writer = csv.writer(datafile)
    

    # Write the header row
    writer.writerow(['   Election Results           ' ])
    writer.writerow(['----------------------------------'])
    writer.writerow([f'Total votes:{total_vote_cnt}'])
    writer.writerow(['-----------------------------------'])
    # loop to get the election results
    for z in range(len(Candidate_unique_list)):
        writer.writerow([f'{Candidate_unique_list[z]}  : {round(Candidate_Vote_cnt[z] / total_vote_cnt * 100 ,2)}% ({Candidate_Vote_cnt[z]})'])
        y = y + 1
    writer.writerow(['------------------------------------'])
    writer.writerow([f' Winner:     {winner}'])
    writer.writerow(['------------------------------------'])
        

    
import os
import csv

csvpath = os.path.join('..', 'PyPoll/Resources','election_data.csv')

votes_count = 0
candidates = []
candidate_votes_count = []

with open(csvpath, newline='', encoding = 'UTF-8') as csvfile:

    csvreader = csv.reader(csvfile, delimiter= ',')

    print(csvreader)

    csv_header = next(csvreader)
    
    for row in csvreader:

        # count votes cast
        votes_count += 1

        x = (row[2])

        # list of candidates
        if x in candidates:

            candidate_individual = candidates.index(x) 
            candidate_votes_count[candidate_individual] = candidate_votes_count[candidate_individual] + 1

        else:

            candidates.append(x)
            candidate_votes_count.append(1)

percent = []
votes_max = candidate_votes_count[0]
index_max = 0

for x in range(len(candidates)):

    vote_percent = candidate_votes_count[x] / votes_count * 100
    percent.append(vote_percent)

    if candidate_votes_count[x] > votes_max:

        votes_max = candidate_votes_count[x]
        index_max = x

winner = candidates[index_max] 

# format percent list 
percent = [ '%.3f' % elem for elem in percent ] 

# print summary
print("Election Results")
print("-------------------------------")
print(f"Total Votes: {votes_count}")
print("-------------------------------")
for x in range(len(candidates)):
    print(f'{candidates[x]} : {percent[x]}% ({candidate_votes_count[x]})') 
print("-------------------------------")
print(f'Election winner: {winner}')    
print("-------------------------------")

# create text file and export summary
export_file = open("election_results.txt","w") 

export_file.write("-------------------------------\n")
export_file.write(f"Total Votes: {votes_count}\n")
export_file.write("-------------------------------\n")
for x in range(len(candidates)):
    export_file.write(f'{candidates[x]} : {percent[x]}% ({candidate_votes_count[x]})\n') 
export_file.write("-------------------------------\n")
export_file.write(f'Election winner: {winner}\n')    
export_file.write("-------------------------------\n")

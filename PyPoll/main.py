import os
import csv

election_data_csv = os.path.join('C:/','Users','lukeb','python-challenge1','PyPoll','Resources','election_data.csv')

total_votes = 0
candidates = []
votes_per_candidate = {}

with open(election_data_csv) as csv_file:
    csvreader = csv.reader(csv_file, delimiter= ",")
    
    next(csvreader)
    
    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        
        if candidate not in candidates:
            candidates.append(candidate)
            votes_per_candidate[candidate] = 0
        votes_per_candidate[candidate] += 1

winning_candidate = ""
winning_votes = 0

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

for candidate in candidates:
    votes = votes_per_candidate[candidate]
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
    
    if votes > winning_votes:
        winning_candidate = candidate
        winning_votes = votes

print("-------------------------")
print(f"Winner: {winning_candidate}")
print("-------------------------")


with open("analysis/election_results.txt", "w") as result_file:
    result_file.write("Election Results\n")
    result_file.write("-------------------------\n")
    result_file.write(f"Total Votes: {total_votes}\n")
    result_file.write("-------------------------\n")
    for candidate in candidates:
        votes = votes_per_candidate[candidate]
        percentage = (votes / total_votes) * 100
        result_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    result_file.write("-------------------------\n")
    result_file.write(f"Winner: {winning_candidate}\n")
    result_file.write("-------------------------\n")

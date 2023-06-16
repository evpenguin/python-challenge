#PyPoll
#import stuff needed
import csv 
import os

#make file path and open file
csvpath = os.path.join("Resources", "election_data.csv")
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #initialize variables
    header = next(csvreader)
    total_votes = 0
    votes_calc = {}

    #loop through the cvs and tally votes
    for row in csvreader:
        #if the candidate is already in the dictionary, add one to their tally
        if row[2] in votes_calc:
            votes_calc[row[2]] += 1
        #if not, add the candidate to the dictionary and start tally
        else:
            votes_calc.update({row[2]: 1})
        total_votes += 1
            
#calculate votes percentage and store
#calculate winner
winner = ""
highest_votes = 0
votes_percentage = {}
for candidate in votes_calc:
    #calculate votes percentage
    percentage = (votes_calc[candidate]/total_votes) * 100
    votes_percentage.update({candidate: round(percentage,3)})
    #if they're winning, make them the winner
    if votes_calc[candidate] > highest_votes:
        highest_votes = votes_calc[candidate]
        winner = candidate

#output to terminal
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")
for candidate in votes_percentage:
    print(candidate + ": " + str(votes_percentage[candidate]) + "% (" + str(votes_calc[candidate]) + ")")
print("-------------------------")
print("Winner: " + winner)
    
#export file
output_path = os.path.join("analysis", "analysis.txt")
with open(output_path, 'w') as output:
    output.write("Election Results\n----------------------------\n")
    output.write("Total Votes: " + str(total_votes) + "\n----------------------------\n")
    for candidate in votes_percentage:
        output.write(candidate + ": " + str(votes_percentage[candidate]) + "% (" + str(votes_calc[candidate]) + ")\n")
    output.write("-------------------------\n")
    output.write("Winner: " + winner)
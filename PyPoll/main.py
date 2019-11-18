# Modules
import os
import csv

# Set path for file
csvpath = os.path.join('.','PyPoll_Resources_election_data.csv')
total_votes = 0

with open(csvpath, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    total_votes = sum(1 for row in csvreader)


candidate = {}
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
      if row[2] in candidate:
        candidate[row[2]] = candidate[row[2]] + 1
      else:
        candidate[row[2]] = 1
        
print('Election Results')
print('----------------------------')
print("Total votes: " + str(total_votes)) 
print('----------------------------')

for k,v in candidate.items():
  per = v/total_votes
  print('{}: {:2.3%} ({})'.format(k,per,v))

winner = max(candidate,key=candidate.get)
print('----------------------------')
print('The winner is...' + winner)


   




#import dependencies 


import csv
import os

#define csv path
csvpath = os.path.join('election_data.csv')

#read csv file and skip header
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    #clean up the csvreader file, I just need the names
    names = [row[2] for row in csvreader]
    # print(names)

    #define variables and lists 
    vote = 0 
    count = 0 
    candidates = []
    votes = []
    percentage = []

    #count total votes and create list of candidate names
    for name in names:
       vote += 1
       if name not in candidates:
           candidates.append(name)

    #count number of votes for each candidate and add to votes list
    for person in candidates:
        for name in names:
            if name == person:
                count += 1
        votes.append(count)
        #reset count to zero before starting on next candidate
        count = 0

    #calculate vote percentage, put in clean format and add to percentage list
    for number in votes:
        pct = number/vote
        pct_clean = "{:.3%}".format(pct)
        percentage.append(pct_clean)
    
    #zip results
    results = zip(candidates, percentage, votes)

    #convert results to list and find the winner
    result_list = list(results)
    winner = max(result_list, key = lambda i : i[1])[0] 


    #print results to terminal
    print("Election Results")
    print("-------------------")
    print("Total Votes: ", vote)
    print("-------------------")
    for i in result_list:
        print("{}: {} ({})".format(i[0],i[1],i[2]))
    print("-------------------")
    print("Winner: ", winner)
    print("-------------------")
   
    #export results to text file
f = open("C:/PythonStuff/election_count.txt","w")

print("Election Results", file = f)
print("-------------------", file = f)
print("Total Votes: ", vote, file = f)
print("-------------------", file = f)
for i in result_list:
    print("{}: {} ({})".format(i[0],i[1],i[2]), file= f)
print("-------------------", file = f)
print("Winner: ", winner, file = f)
print("-------------------", file = f)
f.close()


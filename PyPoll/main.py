import csv
import os
candidates = []
csvreader = ['1', '2']
total_vote = 0
candidate_vote_dict = {}

rows = csv.reader(open("/Users/yusrakauppila/Desktop/Python_Challenge/PyPoll/Resources/election_data.csv", "rb"))
data_csv = r"/Users/yusrakauppila/Desktop/Python_Challenge/PyPoll/Resources/election_data.csv" 
analysis_txt =r"/Users/yusrakauppila/Desktop/Python_Challenge/PyPoll/Analysis/PyPoll.txt"

with open(data_csv) as csvfile:
    csvreader=csv.reader(csvfile)

    csvheader=next(csvreader)

    print(csvheader)
    
    # for row in csv_reader:
    #     print(row[2])

# The total number of votes cast
with open(data_csv) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        # total_vote= len(list(csv_reader))

        if row[2] in candidate_vote_dict:
            candidate_vote_dict[row[2]] += 1
        else:
            candidate_vote_dict[row[2]] = 1

        total_vote = total_vote + 1
        winner = max(candidate_vote_dict, key=candidate_vote_dict.get)

vote_percent = {}
for key in candidate_vote_dict.keys():
    vote_list = []
    vote_list.append(candidate_vote_dict[key]/total_vote * 100)
    vote_list.append(candidate_vote_dict[key])
    vote_percent[key] = vote_list
#         candidate = row[2]
        # print(candidate)
# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote.

                                    # FOR EXAMPLE
                                # Election Results
                            # ---------------------------
                                # Total Votes: 3521001
                            # ---------------------------
                                # Khan: 63.000% (2218231)
                                # Correy: 20.000% (704200)
                                # Li: 14.000% (492940)
                                # O'Tooley: 3.000% (105630)
                            # ---------------------------
                                # Winner: Khan
                            # ---------------------------

print("Election Results")
print("_________________________")
print(f"Total Votes: {total_vote}")
print("_________________________")
for key in vote_percent:
    print(f"{key}: {vote_percent[key][0]}% ({vote_percent[key][1]})")
print("_________________________")
print(f"Winner: {winner}")

print("_________________________")
#print(distinct(name))
# Final script should both print the analysis to the terminal and export a text file with the results.
f= open("analysis_txt", "w")

print("Election Results", file=f)
print("_________________________", file=f)
print(f"Total Votes: {total_vote}", file=f)
print("_________________________", file=f)
for key in vote_percent:
    print(f"{key}: {vote_percent[key][0]}% ({vote_percent[key][1]})", file=f)
print("_________________________", file=f)
print(f"Winner: {winner}", file=f)

print("_________________________", file=f)

f.close()   
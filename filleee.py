import csv

# Open and read the CSV file
file_path = r"c:\Users\kyled\AppData\Local\Temp\Temp1_Starter_Code (7).zip\Starter_Code\PyPoll\Resources\election_data.csv"



# Open and read the CSV file
with open(file_path) as file:
    csvreader = csv.reader(file)
    next(csvreader) # skip header row
    data = list(csvreader)

# Get the total number of votes cast
total_votes = len(data)
print("Total Votes: ", total_votes)

# Create an empty list to store candidate names
candidates = []

# Loop through the data and append candidate names to the list
for row in data:
    candidate = row[2]
    if candidate not in candidates:
        candidates.append(candidate)

print("Candidates: ", candidates)

# Create a dictionary to store the vote counts for each candidate
vote_counts = {}

# Loop through the data and count the votes for each candidate
for row in data:
    candidate = row[2]
    if candidate in vote_counts:
        vote_counts[candidate] += 1
    else:
        vote_counts[candidate] = 1

# Calculate the percentage of votes each candidate won
percentage_votes_per_candidate = {}
for candidate, votes in vote_counts.items():
    percentage_votes = (votes / total_votes) * 100
    percentage_votes_per_candidate[candidate] = percentage_votes

print("Percentage of Votes Each Candidate Won:")
for candidate, percentage_votes in percentage_votes_per_candidate.items():
    print(candidate, ": ", percentage_votes)

# Print the total number of votes each candidate won
print("Total Votes per Candidate:")
for candidate, votes in vote_counts.items():
    print(candidate, ": ", votes)

# Get the winner of the election based on popular vote
winner = max(vote_counts, key=vote_counts.get)
print("Winner: ", winner)





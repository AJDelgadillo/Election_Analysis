# The data we need to retrieve.
import csv
import os

    # set datafile to variable
file_to_load = os.path.join("Resources" , "election_results.csv")

# Create a new text file to hold analysis findings.
    # Create a variable for this new file.
file_to_save = os.path.join('Analysis', 'election_analysis.text')

# Initialize total votes to 0

total_votes = 0

# List of candidates

candidate_options = []

# Dictioary candidate : votes

candidate_votes = {}

# Inititalizing the winning candidate.

winning_candidate = ''
winning_count = 0
winning_percentage = 0 

    # Open the datafile to perform analysis 
with open(file_to_load) as election_data:

# Read and Analyze the data here.
    file_reader = csv.reader(election_data) 

# Print each row in the CSV file.
    headers = next(file_reader)
    print(headers)

    for row in file_reader:
        # Add to the total vote count
        total_votes += 1
        # Print the candidate name from each row.
        candidate_name = row[2]
        # Add the candidate name to the lists of candidates 
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name) 
        # Counting the candidates votes
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

# Finding the percentage of votes for each candidate
for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) * 100
    
    # Print out the winning candidate, votes and percentage
    print(f'{candidate_name}: {vote_percentage:.3}% ({votes:,})\n')

    # Determine winning candidate and vote count 
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name
winning_candidate_summary = (
    f'-----------------------\n'
    f'Winner: {winning_candidate}\n'
    f'Winning Vote Count: {winning_count:,}\n'
    f'Winning Percentage: {winning_percentage:.3}%\n'
    f'-----------------------')


# Print the winning candidate summary
print(winning_candidate_summary)

# 1. The total number of votes cast.

# 2. A complete list of candidates who received votes.

# 3. The percentage of votes each candidate won.

# 4. The total number of votes each candidate won.

# 5. The winner of the election based on popular vote.

# Close the file.

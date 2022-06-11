# The data we need to retrieve.
import csv
import os

    # set datafile to variable
file_to_load = os.path.join("Resources" , "election_results.csv")

# Create a new text file to hold analysis findings.
    # Create a variable for this new file.
file_to_save = os.path.join('Analysis', 'election_analysis.text')

    # Open the datafile to perform analysis 
with open(file_to_load) as election_data:

# Read and Analyze the data here.
    file_reader = csv.reader(election_data) 

# Print each row in the CSV file.
    headers = next(file_reader)
    print(headers)

# 1. The total number of votes cast.

# 2. A complete list of candidates who received votes.

# 3. The percentage of votes each candidate won.

# 4. The total number of votes each candidate won.

# 5. The winner of the election based on popular vote.

# Close the file.

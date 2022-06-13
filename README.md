# Election_Analysis

## Overview of Election Audit
Seth and Tom from the Colorado Board of Elections have requested an analysis of election results in preparation of an election audit. They specifically wanted to determine how many votes were cast in the election, who were the candidates, and who is the winning candidate. Following instructions given in Module 3 I was able to accomplish this goal by writing the [PyPoll.py](PyPoll.py) script. The results of running this script were saved in a text file titled: [election_analysis.text](Analysis/election_analysis.text).

The goal for challenge 3 was to modify the PyPoll.py script to further analyze the election results and determine which county had the greatest voter turnout. The modified script written for challenge 3 was saved as [PyPoll_Challenge.py](PyPoll_Challenge.py) and the results of running this script were saved in a test file titled: [election_results.txt](Analysis/election_results.txt). 

Overall, for challenge 3 I analyzed the following parameters:

1. The total amount of votes cast in the election.
2. The names of each candidate who received votes.
3. How many votes each candidate received.
4. The percentage of votes each candidate received. 
5. Which candidate is the winner of the election, based on having the most amount of votes.
6. The names of each county participating in the election.
7. How many votes were cast in each county.
8. The percentage of votes cast from each county.
9. Which county had the greatest voter turnout.

## Resources
- Data Source: [election_results.csv](Resources/election_results.csv)  
- Software: Python 3.10.5, Visual Studio Code 1.67.2

## Election Audit Results
The analysis of the election results show that:
- The number of votes cast in the election
    - 369,711 votes
- The 3 candidates who received votes:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The results for each candidate:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
    - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
    - Raymon Anthony Doane received 3.14% of the vote and 11,606 number of votes.
- The winner of the election:
    - Candidate Diana DeGette who received 73.8% of the votes and 272,892 number of votes.
- Amount of votes cast in each county:
    - Jefferson county received 10.5% of the votes and 38,855 number of votes.
    - Denver county received 82.8% of the votes and 306,055 number of votes.
    - Arapahoe county received 6.7% of the votes and 24,801 number of votes.
- The county having the largest amount of votes cast:
    - Denver county which accounted for 82.8% of the votes and 306,055 number of votes.

## Election Audit Summary

This script could be used for any election with very minimal modification. One aspect that would need to be changed is the ‘file_to_load’ variable; we would need to edit this variable so that the correct relative path for the csv file is used. The results of running the script is entirely dependent on the data that is found in the csv file. We would also need to change the file_to_save variable so that the data analyzed by the script is saved in the correct text file.  

Besides those two small modifications to make sure that the script is utilizing the correct data files, we could also edit the script to analyze the data differently. Using the same dataset given in this challenge we could change the script to determine which candidate was the most popular in each county. 

We could also edit the script to analyze other types of datasets. For example, we could analyze a dataset concerning voter activity on ballot measures. Instead of writing the script to make a list of each candidate option I would make a list of ballot measures. I would also edit the CSV file to have a yes/no column and edit the script to determine the amount of yes or no votes given to each ballot measure. I would then be able to determine the percentage of yes and no votes, and ultimately which ballot measures were favored by the voters.  These are just two hypothetical situations, but this script is very versatile and could be used for many other similar datasets.

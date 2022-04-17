#the data we need to retrieve
#1. The total number of votes cast
#2 A complete list of candidates that received votes
#3 the percentage of votes each candidate won
#4 the total number of votes each candidate won
#5 the winner based on popular vote

#add dependencies
import csv
import os 

#Assign a variable for the file to load and the path
file_to_load= os.path.join("Resources", "election_results.csv")
#Assign a variable to save the file to a path
file_to_save= os.path.join('analysis', "election_analysis.txt")

#1. Initialize a total vote counter
total_votes= 0

#Print candidate name from each row
candidate_options = []

#Declare an empty dictionary
candidate_votes= {}

#Winning candidate and Winning Count tracker
winning_candidate = ""
winning_count=0
winning_percentage=0

#Open the election results and read the file
with open(file_to_load) as election_data:
    #read the file object with the reader function.
    file_reader= csv.reader(election_data)

    #Read and print the header row
    headers= next(file_reader)
    

    #Print each row in the CSV file.
    for row in file_reader:
        #Add to the total vote count
        total_votes += 1
        #Print the candidate name from each row
        candidate_name= row[2]
        #Add the candidate name to the candidate list
        if candidate_name not in candidate_options:
            #add candidates name to the candidate list
            candidate_options.append(candidate_name)
            #begin tracking that candidates vote count
            candidate_votes[candidate_name]=0
        #Add a vote to that candidate's count
        candidate_votes[candidate_name]+=1
#Determine the percentage of votes for each candidate by looping through the counts
#Iterate through the candidate list
for candidate_name in candidate_votes:
    #Retrieve vote count of a candidate
    votes=candidate_votes[candidate_name]
    #calculate the percentage of votes.
    vote_percentage= float(votes) / float(total_votes) * 100
    
    #print out each candidate's name, vote count, and percentage of votes in the terminal
    print(f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')
    #Determine winning vote count and candidate
    #Determin if the votes is greater than the winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        #if true then set winning_count = votes and winning_percent= vote_percentage
        winning_count = votes
        winning_percentage= vote_percentage
        winning_candidate= candidate_name
winning_candidate_summary = (
    f'---------------------\n'
    f'Winner: {winning_candidate}\n'
    f'Winning Vote Count: {winning_count:,}\n'
    f'Winning Percentage: {winning_percentage:.1f}%\n'
    f'---------------------\n')
print(winning_candidate_summary)

    




# #Open the election results and read the file
# with open(file_to_save, 'w') as txt_file:

#     #Write some data to the file
#     txt_file.write('Counties in the Election\n--------------------\nArapahoe\nDenver\nJefferson')


# #Use the open statement to open the file as a text file
# outfile= open(file_to_save, 'w')

# #Write some data to the file
# outfile.write('Hello World')

# #Close the file
# outfile.close()

#Cleaning up the above code using the with statement 

#This would retrieve the first item from each row
    #for row in file_reader:
        #print(row[0])
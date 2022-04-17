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

#Open the election results and read the file
with open(file_to_load) as election_data:
    #read the file object with the reader function.
    file_reader= csv.reader(election_data)

    #Read and print the header row
    headers= next(file_reader)
    print(headers)


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
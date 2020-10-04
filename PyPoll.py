# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("/Users","meghanministri","Desktop","git","Election_Analysis","Resources","election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("/Users","meghanministri","Desktop","git","Election_Analysis","analysis", "election_analysis.txt")

election_results = open(file_to_load, "r")

# To do: perform analysis.
#Print each row in the CSV file
for row in election_results:
     print(row)

# Open the election results and read the file.
with open(file_to_load) as election_results:
    file_reader = csv.reader(election_results)

# Read and print the header row.
    headers = next(file_reader)
    print(headers)




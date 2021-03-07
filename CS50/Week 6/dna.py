from sys import argv
from csv import reader, DictReader

# Check number of c l arguments
argc = len(argv)
if argc != 3:
    print("Invalid number of command line arguments")
    exit(1)

# Create a dic to put names in; and a list to store names
people = {}
names = []
sequences = []

# Put the number of the people as key for the dictionary and make dictionary
with open(argv[1], "r") as databasein:
    database = reader(databasein)
    i = 0
    for row in database:
        if i == 0:
            # Get a list with the squences to be searching for
            for item in row:
                sequences.append(item)
            i += 1
            sequences.pop(0)
        else:
            # Store values into the dictionary
            people[i - 1] = []
            list = []
            for item in row:
                list.append(item)
            list.pop(0)
            people[i - 1] = [int(char) for char in list]
            # Get list of names
            names.append(row[0])
            i += 1

# Read the DNA sequence and copy into string
with open(argv[2], "r") as sequencein:
    sequence = reader(sequencein)
    for row in sequence:
        DNAsequence = row

# Store in string
DNA = DNAsequence[0]

# Calculate longest consecutive DNA pairs for each DNA sequence to consider
lengths = []
# Repeat for each given sequence
for i in range(len(sequences)):
    charcount = 0
    maxcount = 0
    sequencecounter = 0
    # Iterate through DNA
    while charcount < len(DNA) - len(sequences[i]):
        # Iterate char by char until a match is found
        string = DNA[charcount: charcount + len(sequences[i])]
        # If there is a match
        if string == sequences[i]:
            sequencecounter += 1
            charcount += len(sequences[i])
            while charcount < len(DNA) - len(sequences[i]):
                string = DNA[charcount: charcount + len(sequences[i])]
                if string != sequences[i]:
                    # Return the count
                    if sequencecounter > maxcount:
                        maxcount = sequencecounter
                    # Reset counter
                    sequencecounter = 0
                    # Go back to normal char by char searching
                    break
                else:
                    sequencecounter += 1
                    charcount += len(sequences[i])
        charcount += 1
    lengths.append(maxcount)

for i in range(len(names)):
    if lengths == people[i]:
        print(names[i])
        exit(0)

print("No match")
exit(0)
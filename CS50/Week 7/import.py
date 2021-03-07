import cs50
import sys
import csv

# Check cla
if len(sys.argv) != 2:
    print("Invalid number of command line arguments")
    exit(1)

# Open connection to database
db = cs50.SQL("sqlite:///students.db")

# Open table to read
with open(sys.argv[1], "r") as filein:
    # Create a Dict Reader
    reader = csv.DictReader(filein)

    # Iterate through every student
    for line in reader:
        # Read name
        fullname = line["name"].split()
        # Separate into i, m, l
        # Get middle and last
        if len(fullname) == 2:  # No middle name
            middle = None
            last = fullname[1]
        else:
            middle = fullname[1]
            last = fullname[2]
        # Get house
        house = line["house"]
        # Get Birth
        birth = line["birth"]
        # Insert into database
        db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)",
                   fullname[0], middle, last, house, birth)
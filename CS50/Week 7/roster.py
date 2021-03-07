import cs50
import sys

# Check cla
if len(sys.argv) != 2:
    print("Invalid number of command line arguments")
    exit(1)

# Open connection to databse
db = cs50.SQL("sqlite:///students.db")

results = db.execute(
    "SELECT DISTINCT first, middle, last, birth FROM students WHERE house = :house ORDER BY last, first", house=sys.argv[1])

# Print results student by student
for student in results:
    print(student["first"], end=" ")
    # Print or maybe no middle
    if(student["middle"] != None):
        print(student["middle"], end=" ")
    # Print rest
    last = student["last"]
    birth = student["birth"]
    print(f"{last}, born {birth}")
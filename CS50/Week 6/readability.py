# Import
from cs50 import get_string

# Get string from user
string = get_string("Text: ")
string = string.lower()

letters = 0
words = 1
sentences = 0

# Define low
low = 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'

for c in string:
    if c in low:
        letters += 1
    elif c == ' ':
        words += 1
    elif c == "." or c == '?' or c == "!":
        sentences += 1
# Get index
index = 0.0588 * (100 * letters / words) - 0.296 * (100 * sentences / words) - 15.8
index = int(round(index))
# Check if index is > 16
if index >= 16:
    print("Grade 16+")
elif index < 1:
    print("Before Grade 1")
else:
    print(f"Grade {index}")
from cs50 import get_int

while (True):
    h = get_int("Height: ")
    if h < 9 and h > 0:
        break

for i in range(h):
    # Print spaces
    for j in range(h - (i + 1)):
        print(" ", end="")
    # Print #
    for j in range(i + 1):
        print("#", end="")
    # Print spaces between
    print("  ", end="")
    for j in range(i + 1):
        print("#", end="")
    print("")
from cs50 import get_float

while (True):
    change = get_float("How much money are you owed?\n")
    if change >= 0:
        break

change *= 100
coins = 0

if change > 0:
    while (change >= 25):
        coins += 1
        change -= 25
        round(change)
    while (change >= 10):
        coins += 1
        change -= 10
        round(change)
    while (change >= 5):
        coins += 1
        change -= 5
        round(change)
    while (change >= 1):
        coins += 1
        change -= 1
        round(change)

print(f"{coins}")
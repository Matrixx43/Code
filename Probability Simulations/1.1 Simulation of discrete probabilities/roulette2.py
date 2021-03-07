import random

# A player makes 1000 bets on red. See how much he wins.
# There are 38 slots, of which half of 36 are red = 18. Let them be the first 18.
list = []
for j in range(10):
    balance = 0

    n = 1000

    for i in range(1, n +1):
        roll = random.randint(1, 38)
        if roll <= 18:
            balance += 1
        else:
            balance -= 1
    list.append(balance)
print(list)
print(sum(list) / len(list))
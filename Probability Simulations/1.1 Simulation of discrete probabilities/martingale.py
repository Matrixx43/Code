import random
list = []
for i in range(100):
    balance = 0
    bet = 1
    count = 0

    while balance < 5 and balance > -100:
        roll = random.randint(1, 38)
        if roll <= 18:
            balance += bet
            bet = 1
        else:
            balance -= bet
            bet *= 2
            count += 1

    print(balance, end = "  |  ")
    print(count)
    list.append(balance)

print("Total balance:")
print(sum(list))
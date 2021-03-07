import random

count = 0
b_max = 0
b_min = 0
balance = 0
list = [1,2,3,4]
while list:
    count += 1
    bet = list[0] + list[len(list) - 1]
    # Bet on red the amount of first and last elements
    roll = random.randint(1,38)
    if roll <= 18:
        balance += bet
        list.pop
        list.pop(0)
    else:
        balance -= bet
        list.append(bet)
    if balance < b_min:
        b_min = balance

print(f"It took {count} bets. Max temporarily lost: {b_min}")
print(balance)
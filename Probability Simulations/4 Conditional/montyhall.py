import random

repeat = 10000

# There are 3 doors where 1 has a prize. Give the option to change or keep the door you chose after showing a not winner door's result.

# Choose option to play
option = 2
while option != 0 and option != 1:
    option = int(input("Do you want to change door after being shown wrong one 1(yes)/0(no): "))

wins = 0
if option == 0:
    for i in range(repeat):
        # Randomly assign a winner door and randomly select a door
        if random.randint(1,3) == random.randint(1,3):
            wins += 1
else:
    for i in range(repeat):
        # Randomly assign a winner door and randomly select a door. Then change selected to remaining door
        winner = random.randint(1,3)
        # Suppose participant always selects door 1
        if winner == 1:
            wins += 0 # Because part will change door
        else:
            wins += 1 # Because part will select correct one


print(f"Your probability of winning was {wins}/{repeat} = {wins/repeat}")
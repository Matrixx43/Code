import random

# Hospital A has 45 babies / day
# Hospital B has 15
# Prob(boy) = .5
for k in range(20):
    prop_A = []
    prop_B = []

    for i in range(365):
        boys_A = 0
        boys_B = 0
        # A
        for j in range(45):
            if random.randint(1,2) == 1:
                boys_A += 1
        # B
        for j in range(15):
            if random.randint(1,2) == 1:
                boys_B += 1
        prop_A.append(boys_A / 45)
        prop_B.append(boys_B / 15)

    extraA = 0
    extraB = 0
    for prop in prop_A:
        if prop > .6:
            extraA += 1
    for prop in prop_B:
        if prop > .6:
            extraB += 1

    print(f"Number of days when the proportion of boys was more than 60%: A: {extraA}  |  B: {extraB}")
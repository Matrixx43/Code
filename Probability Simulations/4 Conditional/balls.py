import random

n = 50
repeat = 100000

# Box 1 has all but one white balls
b1 = [0] * n
b1[0] = 1

# Box 2 has all but one black balls
b2 = [1] * n
b2[0] = 0

results = 0
for i in range(repeat):
    # Randomly select box, then randomly select ball
    if random.randint(0,1) == 0:
        # Box 1
        results += b1[random.randint(0, n - 1)]
    else:
        # Box 2
        results += b2[random.randint(0, n - 1)]

print(f"The proportion of black balls was {results/repeat}")
import random

n = 40
repeat = 10000

for j in range(n + 1):
    # Box 1 has j white balls and n - j  black balls
    b1 = [0] * j
    extra1 = [1] * (n - j)
    if b1:
        b1.extend(extra1)
    else:
        b1 = extra1

    # Box 2 has j black balls and n - j white balls
    b2 = [1] * j
    extra2 = [0] * (n - j)
    if b2:
        b2.extend(extra2)
    else:
        b2 = extra2

    results = 0
    for i in range(repeat):
        # Randomly select box, then randomly select ball
        if random.randint(0,1) == 0:
            # Box 1
            results += b1[random.randint(0, n - 1)]
        else:
            # Box 2
            results += b2[random.randint(0, n - 1)]

    print(f"{j}: the proportion of black balls was{results/repeat}", end="   ")
    print(b1, end = "")
    print(b2)
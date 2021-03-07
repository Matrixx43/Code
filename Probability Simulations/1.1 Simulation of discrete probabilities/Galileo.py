import random

n = 1000

for z in range(10):
    n_ten = 0
    n_nine = 0
    for i in range(1, n + 1):
        results = []
        for j in range(3):
            results.append(random.randint(1,6))
        sm = sum(results)
        if sm == 9:
            n_nine += 1
        elif sm == 10:
            n_ten += 1

    print(f"Proportion of 9: {n_nine/n}  |  Proportion of 10: {n_ten / n}", end = "         ")
    if n_ten > n_nine:
        print(f"10 > 9")
    else:
        print()
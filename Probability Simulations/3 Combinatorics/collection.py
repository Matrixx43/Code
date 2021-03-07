import random

n = 30 # Number of items to collect

p = 0 # Proportion of cards achieved for some m
m = int(2*n) # Number of trials
result = 1 # Proportion of cards of the collection to have
while p < result:
    print(f"Repeating. p = {p}")
    repeat = []
    # Repeat multiple times to get accurate result
    for j in range(1000):
        # Perform experiment
        exp = [0] * n
        for i in range(m):
            exp[random.randint(1,n) - 1] += 1
        # Count number of items got
        items = 0
        for i in range(n):
            if exp[i] != 0:
                items += 1
        repeat.append(items/n)
    p = sum(repeat) / len(repeat)
    if result - p > .03:
        m += 4
    elif result-p > .01:
        m += 2
    else:
        m += 1

print(m)
    
    
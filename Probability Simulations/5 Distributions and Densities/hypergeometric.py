import random

# Simulate a hypergeometric distribution, with parameters N, k, n
# Returns the number of tagged elements out of the k that are in a selection of n out of the N.

N = -1
while N < 0:
    N = int(input("Total population N: "))
k = -1
while k < 0:
    k = int(input("Tagged elements k: "))
n = -1
while n < 0:
    n = int(input("Elements to select n: "))

# Represent this as a Bernoulli trials process with P(tagged) = p = k / N, where p gets updated after each 'capture' and it is done n times
for i in range(20):
    # Set p
    p = k / N
    tagged = 0
    for j in range(n):
        p_copy = p
        # Do a Bernoulli trial with Prob = p
        if random.random() < p_copy:
            tagged += 1
        # Update p_copy because there is no replacement
        p_copy = (k - tagged) / (N - j - 1)
    print(f"Tagged: {tagged}")


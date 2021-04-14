import random

# Add random numbers until the sum first exceeds 1, and calculate the expectation

repeat = 1000000

count = 0
for i in range(repeat):
    n = random.random()
    count += 1
    while n < 1:
        n += random.random()
        count += 1

print(f"Expectation is {count / repeat}")

# The expectation is e!!!
import random

# 1000 products, of which D are defective. We want to find the maximum likelihood estimate for D, given that we sampled 100 and we found 2 defectives

# We want to iterate over D and find the one that gives the highest Prob of 2/100 happening.

N = 1000
repeat = 10000

for D in range(30):
    # Define the P of one sample being defective
    p = D / N
    # Run experiment to determine Prob of 2 being defective in 100
    double_defects = 0
    for i in range(repeat):
        defects = 0
        # Determine how many defects in 100 given Probability p
        for j in range(100):
            if random.random() < p:
                defects += 1
        if defects == 2:
            double_defects += 1
    # Calculate the Prob of 2 being defective in 100
    Prob = double_defects / repeat
    # If it is in a reasonable margin, print
    if Prob > .1:
        print(f"D = {D}. Prob(2 defective in 100 trials) = {Prob}")

# When running, we see how it peaks around 20 which is the reasonable estimate (That 2% of the 1000 are defective)
    
    
        
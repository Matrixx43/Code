import random
import math

repeat = 10000



for j in range(20):
    ins = 0
    for i in range(repeat):
        # Get random distances between 0-.5
        d1 = random.random()/2
        d2 = random.random()/2
        # Get random theta between 0 - pi/2 = 1.57079
        # Random between 0 - pi/2/2:
        theta = 2
        while theta > math.pi/4:
            theta = random.random()
        # Randomly add half the interval:
        if random.randint(1,2) == 1:
            theta += math.pi/4
        if d1 <= math.sin(theta)/2 or d2 <= math.cos(theta)/2:
            ins += 1
        
        

    print(f"Fraction = {ins/repeat}    Pi approx: {3*repeat/ins}")
import random
import math

repeat = 100

L = 10

for j in range(20):
    d = 0
    for i in range(repeat):
        # Get random theta between 0 - pi/2 = 1.57079
        # Random between 0 - pi/2/2:
        theta = 2
        while theta > math.pi/4:
            theta = random.random()
        # Randomly add half the interval:
        if random.randint(1,2) == 1:
            theta += math.pi/4
        d += L*math.cos(theta) + L*math.sin(theta)

    print(f"Pi approx: {4*L*repeat/d}")
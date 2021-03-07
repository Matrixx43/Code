import random
import math

repeat = 10000000



for j in range(1):
    ins = 0
    for i in range(repeat):
        x1 = random.random()
        x2 = random.random()
        # If above y=1/(1+x) do not count.
        if x2 < 1/(1 + x1):
            ins += 1

    print(f"The area estimate is {ins/repeat}.")
    print(ins)
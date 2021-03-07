import random
import math

repeat = 10000



for j in range(10):
    ins = 0
    for i in range(repeat):
        x1 = random.random()
        x2 = random.random()
        # If above y=sin(pi x) do not count.
        if x2 < math.sin(math.pi * x1):
            ins += 1

    print(f"The area estimate is {ins/repeat}. This gives a pi estimate of {2 / (ins/repeat)}")
    print(ins)
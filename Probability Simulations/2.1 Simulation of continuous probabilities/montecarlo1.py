import random

repeat = 100000000



for j in range(1):
    ins = 0
    for i in range(repeat):
        x1 = random.random()
        x2 = random.random()
        # If outside of the circle of r=1/2 and center (1/2,1/2), do not count.
        if ((x1-.5)**2 + (x2-.5)**2) < 1/4:
            ins += 1

    print(f"The area estimate is {ins/repeat}. This gives a pi estimate of {4 * ins/repeat}")
    print(ins)
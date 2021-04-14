import random

# Originally have 1 w and 1 b balls. Randomly choose one, replace it, and add one more of its color.
for j in range(10):
    repeat = 1000000 - 2

    balls = [0, 1]

    for i in range(repeat):
        balls.append(balls[random.randint(0, len(balls) - 1)])

    # Count number of balls by type and calculate proportion
    w = 0
    b = 0
    for i in range(len(balls)):
        if balls[i] == 0:
            w += 1
        else:
            b += 1

    print(f"There are {b} black balls and {w} white balls. The ratio is {b/w}")


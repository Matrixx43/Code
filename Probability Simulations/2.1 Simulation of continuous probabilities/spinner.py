import random

a = 0 # 1/2
b = 0 # 1/3
c = 0 # 1/6

repeat = 1000

for i in range(repeat):
    r = random.random()
    if r < .5:
        a += 1
    elif r >= .5 and r < 5/6:
        b += 1
    else:
        c += 1

print(f"Fraction of 1/2: {a / repeat}. Fraction of 1/3: {b/repeat}. Fraction of 1/6: {c/repeat}.")
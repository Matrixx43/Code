import random

repeat = 100000
count = 0
for i in range(repeat):
    b = random.random()
    c = random.random()
    if abs(b - c) > .5:
        count += 1
    elif b < .5 and c < .5:
        count += 1
    elif b > .5 and c > .5:
        count += 1

print(count/repeat)
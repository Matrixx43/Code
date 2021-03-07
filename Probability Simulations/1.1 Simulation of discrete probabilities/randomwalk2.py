import random

repeat = 10000000 #M

pos = [0,0]
count = 0
maxcount = 0

for i in range(repeat):
    if random.randint(1,2) == 1:
        pos[0] += 1
    else:
        pos[0] -= 1
    if random.randint(1,2) == 1:
        pos[1] += 1
    else:
        pos[1] -= 1
    count += 1
    if pos == [0,0]:
        # Show how many steps it took to get back to pos 1
        print(count)
        if count > maxcount:
            maxcount = count
        count = 0

print(maxcount)
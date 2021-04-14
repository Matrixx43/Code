import random

repeat = 10000
length = 5
count = 0

for i in range(repeat):
    list = []
    for j in range(length):
        # Assign random number that was not there before
        a = random.randint(1,9)
        while a in list:
            a = random.randint(1,9)
        list.append(a)
    for j in range(length):
        # Count number of inversions
        for k in range(j + 1 , length):
            if list[k] > list[j]:
                count += 1

print(count / repeat)

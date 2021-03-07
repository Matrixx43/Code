import random

# Average number of children per family if everyone had children until they had a boy
sample = 100000
count = 0
for i in range(sample):
    count += 1
    while random.randint(1,2) == 2:
        count += 1
print(count / sample)
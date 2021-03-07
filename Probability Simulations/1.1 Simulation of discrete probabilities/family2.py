import random

# Average number of children per family if everyone had children until they had a boy and a girl
sample = 100000
count = 0
for i in range(sample):
    boy = False
    girl = False
    while not boy or not girl:
        a = random.randint(1,2)
        count += 1
        if a == 1:
            boy = True
        else:
            girl = True
print(count / sample)
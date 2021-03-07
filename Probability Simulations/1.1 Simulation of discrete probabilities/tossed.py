import random

for j in range(10):
    balance = 0
    price = 17
    repeat = 100000

    balance = -repeat * price

    for i in range(repeat):
        count = 1
        while random.randint(1,2) == 2:
            count += 1
        balance += 2**count

    print(balance)

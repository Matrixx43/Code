import random

repeat_throws = 20000
max_n = 152

list = []
# Try different numbers of throws
for k in range(148, max_n):
    print(k)
    n = k
    # Repeat mamny times and keep count of which had a triple six
    succesful = 0
    for j in range(repeat_throws):
        triple6 = 0
        for i in range(1, n + 1):
            a = random.randint(1,6)
            b = random.randint(1,6)
            c = random.randint(1,6)

            if a == 6 and b == 6 and c == 6:
                triple6 += 1
        if triple6 > 0:
            succesful += 1
    
    list.append(succesful / repeat_throws)
print(list)

import random
count = 0

for i in range(2):
    for j in range(2):
        for k in range(2):
            for l in range(2):
                list = [i,j,k,l]
                if sum(list) == 2:
                    count += 1
                s = ""
                for element in list:
                    if element == 0:
                        s += "H"
                    else:
                        s += "T"
                print(s)
print(count)
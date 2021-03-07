from random import randint as rint
n = 100

for j in range(5):
    within = 0
    heads = 0
    for i in range(1, n+1):
        r = rint(1,2)
        if r == 1:
            heads += 1
        hprop = heads / i
        if hprop < .6 and hprop > .4:
            within += 1
    print(f"Repeated {n} times. Within range {within} times. Ratio: {within / n}")

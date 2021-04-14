import random
import math

# Show exact value of b(n, p, j) and the Possion approx for it

n = -1
while n < 0:
    n = int(input("n: "))
p = 2
while p < 0 or p > 1:
    p = float(input("p: "))
j = n + 1
while j < 0 or j > n:
    j = int(input("j: "))

# Calculate b(n, p, j) = choose(n, j) * p^j * (1-p)^(n-j)
bi = math.comb(n, j) * pow(p, j) * pow(1-p, n-j)
print(f"b({n}, {p}, {j}) = {bi}")

# Show Poisson approx P(X=x) = e^-lam * lam^x / x!, now let x = j
lam = n * p
Pois = math.exp(-lam) * pow(lam, j) / math.factorial(j)
print(f"The Posssion approximation is {Pois}")

print(f"The ratio is {bi / Pois}")
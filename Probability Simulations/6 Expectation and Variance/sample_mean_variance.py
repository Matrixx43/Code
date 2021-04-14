import random

# Roll a die n times and compute the sample menan and sample variance, for n = 10, n = 100 and n = 1000

n = 10
for j in range(3):
    # Perform n dice rolls
    results = [random.randint(1, 6) for i in range(n)]
    # Sample mean
    sample_mean = sum(results) / n
    # Sample variance
    sample_variance = 0
    for i in range(n):
        sample_variance += pow((results[i] - sample_mean), 2)
    sample_variance /= n
    print(f"For n = {n}, the sample mean is {sample_mean} and the sample variance is {sample_variance}")
    n *= 10

print("Expected mean is 3.5 and expected variance is 2.92")
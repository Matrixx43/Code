import random

# There are N moose in an island, of which 50 have been tagged.
# We recapture 200 and 8 of them are tagged.
# We want the most likely estimate for N

# Let m be the #moose not tagged, so N = 50 + m
# Randomly select 200 out of 50 + m, for different values of m, and we want that which will give 8 tagged ones with the biggest consistency
# Consider this as a Bernoulli trials process with P(tagged) = 50 / m = p repeated 200 times, but p gets updated as moose are not replaced

repeat = 1000

# Repeat the experiment for different values of m
for m in range(1000, 1500): # This range is made taking into account the expected result so it runs faster
    # Set Probabilities
    # P(tagged) = p
    p = 50 / m
    eigths = 0
    # Repeat Bernoulli trials process many times to get accurate estimate for this m
    for i in range(repeat):
        p_copy = p
        # Do trials process 200 times
        tagged = 0
        for j in range(200):
            # Do a Bernoulli trial with Prob = p
            if random.random() < p_copy:
                tagged += 1
            # Update p_copy because there is no replacement
            p_copy = (50 - tagged) / (m - j - 1)
        if tagged == 8:
            eigths += 1
    # get the accuracy of this m. We want to maximize the number of trials where we get 8 tagged samples out of 200
    m_accuracy = eigths / repeat
    # If in reasonable range, show:
    if m_accuracy > .16:
        print(f"m = {m}. For this m, the proportion of experiments with eight tagged moose was {m_accuracy}")

# When run, the value peaks around 1250, which is the intuitively reasonable value
            
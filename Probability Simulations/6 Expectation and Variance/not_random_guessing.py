import random

# There is a list with 10 objects of type 0 and 10 of type 1, in random order.
# We want to guess the next object, by knowing which ones came before, and calculate the expectation of correct guesses through simulation
# Without getting info, it should be 20 cases * 1/2 probability of right = 10 correct guesses. But by knowing which ones came before,
# we should be able to increase this expectation

repeat = 100000

# Create list
l = 10 * [1]
l.extend(10 * [0])

correct_guesses = 0
for i in range(repeat):
    # Keep track of previous results
    zeroes = 0
    ones = 0
    # Randomly shuffle list
    random.shuffle(l)
    for j in range(len(l)):
        # Guess 0 or 1, depending on which one has more probablity
        if zeroes <= ones: # If more ones have appeared then 0 is mor elikely
            # Guess 0
            if l[j] == 0:
                zeroes += 1
                correct_guesses += 1
            else:
                ones += 1
        else: # Guess 1
            if l[j] == 1:
                ones += 1
                correct_guesses += 1
            else:
                zeroes += 1


print(f"The average number (expectation) of correct guesses was {correct_guesses/repeat} for every {len(l)} elements.\n")
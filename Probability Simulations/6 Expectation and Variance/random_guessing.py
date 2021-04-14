import random

# There is a list with 10 objects of type 0 and 10 of type 1, in random order.
# We want to guess the next object, without getting any information, and calculate the expectation of correct guesses through simulatiom
# Theoretically, it should be 20 cases * 1/2 probability of right = 10 correct guesses

repeat = 10000

# Create list
l = 10 * [1]
l.extend(10 * [0])

correct_guesses = 0
for i in range(repeat):
    # Randomly shuffle list
    random.shuffle(l)
    for j in range(len(l)):
        # Randomly guess 0 or 1, with equal probability
        if random.random() < .5: # Guess 0
            if l[j] == 0:
                correct_guesses += 1
        else: # Guess 1
            if l[j] == 1:
                correct_guesses += 1

print(f"The average number (expectation) of correct guesses was {correct_guesses/repeat} for every {len(l)} elements.\n")
# As expected, it is very close to 10
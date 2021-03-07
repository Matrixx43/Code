import random

# We will take a sample of 1000 people to predict the outcome of an election and see how many times the prediction is correct

# Say 49% will vote Rep and 51% Dem
# We can play changing the sample size as well as the actual percentages of vote to see the effects on accuracy

predictions = []
correct = 0
repeat = 100

for j in range(repeat):
    sample = 3000
    w_votes = 0

    for i in range(sample):
        vote = random.random()
        # Keep track of number of votes for actual winner
        if vote < .51:
            w_votes += 1

    predictions.append(w_votes / sample)
    if w_votes / sample > .5:
        correct += 1

print(correct, end = " / ")
print(repeat, end = " = ")
print(correct/repeat)
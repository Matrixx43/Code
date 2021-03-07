import random

for z in range(10):
    n = 10000
    p1w = 0

    for j in range(1, n + 1):
        p1 = 0
        p2 = 0
        # Original turn for p1
        turn = 1

        while p1 < 21 and p2 < 21:
            # Get the winner
            win = random.random()
            if turn == 1:
                if win < .6: #.6 prob when serving
                    # p1 wins
                    p1 += 1
                else:
                    p2 += 1
                    turn = 2
            else:
                if win < .5: #.5 when not serving
                    # p1 wins
                    p1 += 1
                    turn = 1
                else:
                    p2 += 1

        if p1 > p2:
            p1w += 1

    print(p1w / n)
import numpy as np

# Monte Carlo estimation of probability that when
# rolling a pair of standard, 6-sided dice, the outcome
# is that both dice individually have a face value less
# than some integer k, for k=1,2,...,6

N = 1_000_000

for k in range(1, 7):
    # N rolls of a pair of dice
    dice1 = np.random.randint(1, 7, size=N)
    dice2 = np.random.randint(1, 7, size=N)

    count = 0
    for i in range(0, len(dice1)):
        if dice1[i] < k and dice2[i] < k:
            count += 1

    print("Probability both dice show less than {} is: {:.3f}".format(k, count/N))

import matplotlib.pyplot as plt
import numpy as np

cash = np.zeros(10000)
cash[0] = 1000

outcome = np.random.binomial(5, 0.5, 10000)

for i in range(1, 10000):
    if outcome[i] < 3:
        cash[i] = cash[i - 1] - 8
    elif outcome[i] <= 5:
        cash[i] = cash[i - 1] + 8
    else:
        print(np.max(outcome), np.min(outcome))
        raise AssertionError("Unexpected outcome ", outcome[i])

plt.plot(np.arange(len(cash)), cash)
plt.xlabel("Times of gamble")
plt.ylabel("Money remained")
plt.title("Simulate Gamble")
plt.show()
print(cash[-1])

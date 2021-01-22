import matplotlib.pyplot as plt
from sys import argv as args

handle = open(args[1], "r")
dev_y = []
for date in handle:
    dev_y.append(int(date.split(".")[0]))

plt.plot([i for i in range(len(dev_y))], dev_y)

pos = len(dev_y) / 5
for i in range(6):
    plt.axvline(x = (pos * i), color='r')

plt.ylabel("Success rate")
plt.xlabel("Iteration")

plt.show()

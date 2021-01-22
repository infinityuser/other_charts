import matplotlib.pyplot as plt
from sys import argv as args

handle = open(args[1], "r")
dev = []
for date in handle:
    dev.append(int(date.split(".")[0]))

plt.ylabel("Success degree")
plt.xlabel("Iteration")

while True:
    print("Range:", len(dev))
    fr, to = map(int, input().split()) 
    plt.plot([i for i in range(len(dev[fr:to]))], dev[fr:to])
    plt.show()

import random


bets = []
for _ in range(10):
    bets.append(random.choice(["head", "tail"]))

print(bets)
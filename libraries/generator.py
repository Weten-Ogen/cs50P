from random import choice

bets = []
for _ in range(10):
    bets.append(choice(["head", "tail"]))

print(bets)
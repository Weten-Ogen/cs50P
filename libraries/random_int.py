import random

num = random.randint(5,10)
print(num)

cards = ["jack", "Queen", "King"]
random.shuffle(cards)
for card in cards:
    print(card)
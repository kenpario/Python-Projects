import random

low = 1
high = 100
options = ("rock", "paper", "scissors")
cards = ["2H", "3D", "5S", "9C", "KD"]

# number = random.randint(low, high)
number = random.random() * 100
option = random.choice(options)
random.shuffle(cards)

print(f"{number:.2f}")
print(option)
print(cards)

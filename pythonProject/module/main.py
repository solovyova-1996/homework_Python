from random import randint, choice, sample, shuffle
print(randint(3,90))
players = ["Max", "Leo", "pit", "kate"]
print(choice(players))
print(sample (players, 2))
cards = ["6", "7", "8","9", "T", "J", "Q", "K", "A"]
shuffle(cards)
print(cards)


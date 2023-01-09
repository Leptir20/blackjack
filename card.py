import random

start = 1

def cardNum():
    number = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", 1]
    num = (random.choice(number))
    return num
def cardSuit():
    suit = ["Clubs", "Spades", "Hearts", "Diamonds"]
    suit = (random.choice(suit))
    return suit
    
while start == 1:
    cardNum()
    cardSuit()
    break

import random
import importlib

end = "No"
counter = 0
suit = ""
number = ""
card_input = "No"

start = input("Do you want to play a game of blackjack? ")

while end != "Yes":
    card_input = input("Do you want a card?" )
    if card_input == "Yes":
        playerCards = []
        import card
        
        cardOne = 0
        card_total = 0
        pcardOwn = 0
        
        number = card.cardNum()
        cardOne = number
        if cardOne == "J" or cardOne == "Q" or cardOne == "K":
            cardOne = 10
        card_total = card_total + int(cardOne)
        print(card_total)
        number = str(number)
        suit = card.cardSuit()
        
        playerCards.insert(counter, number + " of " + suit)
        print("Card One: " + playerCards[counter])
        counter = int(counter) + 1
        pcardOwn = int(pcardOwn) + 1
        print("You have: " + str(pcardOwn) + " cards!")
        
        importlib.reload(card)
        
        cardTwo = 0
        
        number = card.cardNum()
        cardTwo = number
        if cardTwo == "J" or cardTwo == "Q" or cardTwo == "K":
            cardTwo = 10
        card_total = int(card_total) + int(cardTwo)
        number = str(number)
        suit = card.cardSuit()
        
        playerCards.insert(counter, number + " of " + suit)
        print("Card Two: " + playerCards[counter])
        counter = int(counter) + 1
        pcardOwn = int(pcardOwn) + 1
        print("You have: " + str(pcardOwn) + " cards!")
        
        print()
        print("Your card total is " + str(card_total))
        print()
        
        print("Do you want to hit or pass?")
        play = input()
        if play == "Hit":
            cardThree = 0
            
            number = card.cardNum()
            cardThree = number
            if cardThree == "J" or cardThree == "Q" or cardThree == "K":
                cardThree = 10
            card_total = int(card_total) + int(cardThree)
            number = str(number)
            suit = card.cardSuit()
            
            playerCards.insert(counter, number + " of " + suit)
            print("Card One: " + playerCards[0])
            print("Card Two: " + playerCards[1])
            print("Card Three: " + playerCards[counter])
            counter = int(counter) + 1
            pcardOwn = int(pcardOwn) + 1
            print("You have: " + str(pcardOwn) + " cards!")
            
            importlib.reload(card)
            
            print()
            print("Your card total is " + str(card_total))
            print()
            
            print("Do you want to hit or pass?")
        play = input()
        if play == "Hit":
            cardThree = 0
            
            number = card.cardNum()
            cardThree = number
            if cardThree == "J" or cardThree == "Q" or cardThree == "K":
                cardThree = 10
            card_total = int(card_total) + int(cardThree)
            number = str(number)
            suit = card.cardSuit()
            
            playerCards.insert(counter, number + " of " + suit)
            print("Card One: " + playerCards[0])
            print("Card Two: " + playerCards[1])
            print("Card Three: " + playerCards[counter])
            counter = int(counter) + 1
            pcardOwn = int(pcardOwn) + 1
            print("You have: " + str(pcardOwn) + " cards!")
            
            importlib.reload(card)
            
            print()
            print("Your card total is " + str(card_total))
            print()
            
            print("Do you want to hit or pass?")
        play = input()
        if play == "Hit":
            cardThree = 0
            
            number = card.cardNum()
            cardThree = number
            if cardThree == "J" or cardThree == "Q" or cardThree == "K":
                cardThree = 10
            card_total = int(card_total) + int(cardThree)
            number = str(number)
            suit = card.cardSuit()
            
            playerCards.insert(counter, number + " of " + suit)
            print("Card One: " + playerCards[0])
            print("Card Two: " + playerCards[1])
            print("Card Three: " + playerCards[counter])
            counter = int(counter) + 1
            pcardOwn = int(pcardOwn) + 1
            print("You have: " + str(pcardOwn) + " cards!")
            
            importlib.reload(card)
            
            print()
            print("Your card total is " + str(card_total))
            print()
            
            print("Do you want to hit or pass?")
        play = input()
        if play == "Hit":
            cardThree = 0
            
            number = card.cardNum()
            cardThree = number
            if cardThree == "J" or cardThree == "Q" or cardThree == "K":
                cardThree = 10
            card_total = int(card_total) + int(cardThree)
            number = str(number)
            suit = card.cardSuit()
            
            playerCards.insert(counter, number + " of " + suit)
            print("Card One: " + playerCards[0])
            print("Card Two: " + playerCards[1])
            print("Card Three: " + playerCards[counter])
            counter = int(counter) + 1
            pcardOwn = int(pcardOwn) + 1
            print("You have: " + str(pcardOwn) + " cards!")
            
            importlib.reload(card)
            
            print()
            print("Your card total is " + str(card_total))
            print()
            
    end = "Yes"

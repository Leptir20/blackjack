import random
import importlib

end = "No"
counter = 0
suit = ""
number = ""
card_input = "No"

start = input("Do you want to play a game of blackjack? ")

while end != "Yes":
    card_input = input("Do you want a card? " )

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
        elif cardOne == "Ace":
            cardOne = 1

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
        elif cardTwo == "Ace":
            cardTwo = 1

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
        play = ""
        print()
        
        while play != "End":
            print("Do you want to hit or pass?")
            play = input()

            if play == "Hit":
                newCard == True
            elif play == "Pass":
                play == "End"
            else:
                print("Please re-enter your response")


        while newCard == True:
            if play == "Hit":
                cardThree = 0
            
                number = card.cardNum()
                cardThree = number
                if cardThree == "J" or cardThree == "Q" or cardThree == "K":
                    cardThree = 10
                elif cardTwo == "Ace":
                    cardTwo = 1
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
                newCard == False
            elif play == "Pass":
                newCard == "End"

        if play == "Hit":
            cardFour = 0
            
            number = card.cardNum()
            cardFour = number

            if cardFour == "J" or cardFour == "Q" or cardFour == "K":
                cardFour = 10
            elif cardFour == "Ace":
                cardFour = 1

            card_total = int(card_total) + int(cardFour)
            number = str(number)
            suit = card.cardSuit()
            
            playerCards.insert(counter, number + " of " + suit)
            print("Card One: " + playerCards[0])
            print("Card Two: " + playerCards[1])
            print("Card Three: " + playerCards[2])
            print("Card Four: " + playerCards[counter])
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
            cardFive = 0
            
            number = card.cardNum()
            cardFive = number
            if cardFive == "J" or cardFive == "Q" or cardFive == "K":
                cardFive = 10
            elif cardFive == "Ace":
                 cardFive = 1
            card_total = int(card_total) + int(cardFive)
            number = str(number)
            suit = card.cardSuit()
            
            playerCards.insert(counter, number + " of " + suit)
            print("Card One: " + playerCards[0])
            print("Card Two: " + playerCards[1])
            print("Card Three: " + playerCards[2])
            print("Card Four: " + playerCards[3])
            print("Card Five: " + playerCards[counter])
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
            cardSix = 0
            
            number = card.cardNum()
            cardSix = number
            if cardSix == "J" or cardSix == "Q" or cardSix == "K":
                cardSix = 10
            elif cardSix == "Ace":
                cardSix = 1
            card_total = int(card_total) + int(cardSix)
            number = str(number)
            suit = card.cardSuit()
            
            playerCards.insert(counter, number + " of " + suit)
            print("Card One: " + playerCards[0])
            print("Card Two: " + playerCards[1])
            print("Card Three: " + playerCards[2])
            print("Card Four: " + playerCards[3])
            print("Card Five: " + playerCards[4])
            print("Card Six: " + playerCards[counter])
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
            cardSeven = 0
            
            number = card.cardNum()
            cardSeven = number
            if cardSeven == "J" or cardSeven == "Q" or cardSeven == "K":
                cardSeven = 10
            elif cardSeven == "Ace":
                cardSeven = 1
            card_total = int(card_total) + int(cardSeven)
            number = str(number)
            suit = card.cardSuit()
            
            playerCards.insert(counter, number + " of " + suit)
            print("Card One: " + playerCards[0])
            print("Card Two: " + playerCards[1])
            print("Card Three: " + playerCards[2])
            print("Card Four: " + playerCards[3])
            print("Card Five: " + playerCards[4])
            print("Card Six: " + playerCards[5])
            print("Card Seven: " + playerCards[counter])
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
            cardEight = 0
            
            number = card.cardNum()
            cardNine = number
            if cardEight == "J" or cardEight == "Q" or cardEight == "K":
                cardEight = 10
            elif cardEight == "Ace":
                cardEight = 1
            card_total = int(card_total) + int(cardEight)
            number = str(number)
            suit = card.cardSuit()
            
            playerCards.insert(counter, number + " of " + suit)
            print("Card One: " + playerCards[0])
            print("Card Two: " + playerCards[1])
            print("Card Three: " + playerCards[2])
            print("Card Four: " + playerCards[3])
            print("Card Five: " + playerCards[4])
            print("Card Six: " + playerCards[5])
            print("Card Seven: " + playerCards[6])
            print("Card Eight: " + playerCards[counter])
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
            cardNine = 0
            
            number = card.cardNum()
            cardNine = number
            if cardNine == "J" or cardNine == "Q" or cardNine == "K":
                cardNine = 10
            elif cardNine == "Ace":
                cardNine = 1
            card_total = int(card_total) + int(cardNine)
            number = str(number)
            suit = card.cardSuit()
            
            playerCards.insert(counter, number + " of " + suit)
            print("Card One: " + playerCards[0])
            print("Card Two: " + playerCards[1])
            print("Card Three: " + playerCards[2])
            print("Card Four: " + playerCards[3])
            print("Card Five: " + playerCards[4])
            print("Card Seven: " + playerCards[6])
            print("Card Eight: " + playerCards[7])
            print("Card Nine: " + playerCards[counter])
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
            cardTen = 0
            
            number = card.cardNum()
            cardTen = number
            if cardTen == "J" or cardTen == "Q" or cardTen == "K":
                cardTen = 10
            elif cardTen == "Ace":
                cardTen = 1
            card_total = int(card_total) + int(cardTen)
            number = str(number)
            suit = card.cardSuit()
            
            playerCards.insert(counter, number + " of " + suit)
            print("Card One: " + playerCards[0])
            print("Card Two: " + playerCards[1])
            print("Card Three: " + playerCards[2])
            print("Card Four: " + playerCards[3])
            print("Card Five: " + playerCards[4])
            print("Card Six: " + playerCards[5])
            print("Card Seven: " + playerCards[6])
            print("Card Eight: " + playerCards[7])
            print("Card Nine: " + playerCards[8])
            print("Card Ten: " + playerCards[counter])
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
            cardEleven = 0
            
            number = card.cardNum()
            cardEleven = number
            if cardEleven == "J" or cardEleven == "Q" or cardEleven == "K":
                cardEleven = 10
            elif cardEleven == "Ace":
                cardEleven = 1
            card_total = int(card_total) + int(cardEleven)
            number = str(number)
            suit = card.cardSuit()
            
            playerCards.insert(counter, number + " of " + suit)
            print("Card One: " + playerCards[0])
            print("Card Two: " + playerCards[1])
            print("Card Three: " + playerCards[2])
            print("Card Four: " + playerCards[3])
            print("Card Five: " + playerCards[4])
            print("Card Six: " + playerCards[5])
            print("Card Seven: " + playerCards[6])
            print("Card Eight: " + playerCards[7])
            print("Card Nine: " + playerCards[8])
            print("Card Ten: " + playerCards[9])
            print("Card Eleven: " + playerCards[counter])
            counter = int(counter) + 1
            pcardOwn = int(pcardOwn) + 1
            print("You have: " + str(pcardOwn) + " cards!")
            
            importlib.reload(card)
            
            print()
            print("Your card total is " + str(card_total))
            print()
            
    end = "Yes"

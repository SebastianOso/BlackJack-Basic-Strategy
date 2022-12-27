import random

#In blackjack they use a "sabot", a big deck that consist of 5 decks

deck = [
    "A","A","A","A",
    2,2,2,2,
    3,3,3,3,
    4,4,4,4,
    5,5,5,5,
    6,6,6,6,
    7,7,7,7,
    8,8,8,8,
    9,9,9,9,
    10,10,10,10,
    "J","J","J","J",
    "Q","Q","Q","Q",
    "K","K","K","K"
]

sabot = []

for i in range(0,3):
    sabot.extend(deck)

random.shuffle(sabot)


def PracticeHardHand(sabot):
    #to practice hard hands we have to erase from the list all the aces from the sabot
    handsplayed = 0
    correcthands = 0

    
    for i in sabot:  #Here we remove the aces with a for
        if i == "A":
            sabot.remove(i)
    for i in sabot:  #the process its done 2 times because in the first 'for cycle' for a unknown reason  
                     #there were still aces left in the sabot
        if i == "A":
            sabot.remove(i)
        #Here we get the length of the sabot to use it later to pick a random card from the sabot
    
    while True:

        print(correcthands,"/",handsplayed, 'Hands')

        lengthsabot = len(sabot)

        # In blackjack the dealer has 2 cards, a card facing upwards and a card facing down, for basic strategy
        # the only thing we need to know is the dealer card thats facing upwards and it is called the dealer upcard

        dealerupcard = sabot.pop(random.randint(0,lengthsabot))
        pcard1 = sabot.pop(random.randint(0,lengthsabot))
        pcard2 = sabot.pop(random.randint(0,lengthsabot))


        dealerupcard1 = [dealerupcard]
        playerhand = [pcard1,pcard2]


        #hee we display in the terminal the dealerupcard and the 2 cards the player has
        print("Dealer upcard: ", dealerupcard)
        print("Your Hand:",', '.join(map(str, playerhand)))

        # In blackjack you can do several things like hitting(ask for another card), double(its like a hit but you can only
        # hit once), stand, you can also split the cards when both of them are the same number and finally you can surrender

        print("What are you going to do?")
        print("1.- Hit")
        print("2.- Double")
        print("3.- Stand")
        print("4.- Split")
        print("5.- Surrender")
        print("6.- leave")

        #here we are changing the figure cards for it's value to make a player hand total
        #so we can start making decisions based on the basic strategy chart


        for index in range(len(playerhand)):

            if playerhand[index] == "J":
                playerhand[index] = 10
        
    
            elif playerhand[index] == "Q":
                playerhand[index] = 10 
    
            elif playerhand[index] == "K":
                playerhand[index] = 10

        if dealerupcard == "J":
            dealerupcard = 10

        if dealerupcard == "Q":
            dealerupcard = 10

        if dealerupcard == "K":
            dealerupcard = 10


        playerhandTotal = playerhand[0] + playerhand[1]

        choiceinp = input("")
        choice = int(choiceinp)


# After this to make all the decisions it is based on the blackjack basic strategy chart
# made y BlackJack Apprenticeship, link to the charts: https://www.blackjackapprenticeship.com/blackjack-strategy-charts/

        if choice == 6:

            print("Have a nice day, come back later")
            break


        #if the player has a correct answer, the correct hand variable is added a 1
        #and also the hands played will be added 1, so if the player loses only the 
        # hands played will be added 1 


        if playerhandTotal >= 17:

            if  choice == 3: #player decides to stand

                correcthands = correcthands + 1
                handsplayed = handsplayed + 1
                print("correct")

            else:

                handsplayed = handsplayed + 1
                print("wrong")

        elif playerhandTotal >=13 and playerhandTotal <= 16:

            if choice == 1: #player decides to hit

                if  dealerupcard >= 7 and dealerupcard <=10:

                    correcthands = correcthands + 1
                    handsplayed = handsplayed + 1
                    print("correct")

                else:

                    handsplayed = handsplayed + 1
                    print("wrong")

            elif choice == 3: #player decides to stand

                if  dealerupcard >= 2 and dealerupcard <=6:

                    correcthands = correcthands + 1
                    handsplayed = handsplayed + 1
                    print("correct")

                else:

                    handsplayed = handsplayed + 1
                    print("wrong")

            else:

                handsplayed = handsplayed + 1
                print("wrong")

        elif playerhandTotal == 12:

            if choice == 1: #player decides to hit

                if dealerupcard == 2 or dealerupcard == 3:

                    correcthands = correcthands + 1
                    handsplayed = handsplayed + 1
                    print("correct")

                elif  dealerupcard >= 7 and dealerupcard <=10:

                    correcthands = correcthands + 1
                    handsplayed = handsplayed + 1
                    print("correct")

                else:
                    handsplayed = handsplayed + 1
                    print("wrong")

            elif choice == 3: #player decides to stand

                if dealerupcard <= 4 and dealerupcard >=6:
                    correcthands = correcthands + 1
                    handsplayed = handsplayed + 1
                    print("correct")

                else:

                    handsplayed = handsplayed + 1
                    print("wrong")

            else:

                handsplayed = handsplayed + 1
                print("wrong")

        elif playerhandTotal == 11:

            if choice == 2: #player decides to double
                correcthands = correcthands + 1
                handsplayed = handsplayed + 1
                print("correct")

            else:

                handsplayed = handsplayed + 1
                print("wrong")

        elif playerhandTotal == 10:

            if choice == 1: #player decides to hit

                if dealerupcard == 10:

                    correcthands = correcthands + 1
                    handsplayed = handsplayed + 1
                    print("correct")

                else:

                    handsplayed = handsplayed + 1
                    print("wrong")

            elif choice == 2: #player decides to double

                if dealerupcard >= 2 and dealerupcard <= 9:

                    correcthands = correcthands + 1
                    handsplayed = handsplayed + 1
                    print("correct")

                else:

                    handsplayed = handsplayed + 1
                    print("wrong")

            else:

                handsplayed = handsplayed + 1
                print("wrong")

        elif playerhandTotal == 9:

            if choice == 1: #player decides to hit

                if dealerupcard == 2:

                    correcthands = correcthands + 1
                    handsplayed = handsplayed + 1
                    print("correct")

                elif dealerupcard >= 7 and dealerupcard <= 10:

                    correcthands = correcthands + 1
                    handsplayed = handsplayed + 1
                    print("correct")

                else:

                    handsplayed = handsplayed + 1
                    print("wrong")

            elif choice == 2: #player decides to double

                if dealerupcard >= 3 and dealerupcard <= 6:

                    correcthands = correcthands + 1
                    handsplayed = handsplayed + 1
                    print("correct")

                else:

                    handsplayed = handsplayed + 1
                    print("wrong")

            else:

                handsplayed = handsplayed + 1
                print("wrong")

        elif playerhandTotal <= 8:

            if choice == 1: #player decides to hit

                correcthands = correcthands + 1
                handsplayed = handsplayed + 1
                print("correct")

            else:

                handsplayed = handsplayed + 1
                print("wrong")
        
        sabot.append(dealerupcard)
        sabot.append(pcard1)
        sabot.append(pcard2)


def PracticeSoftHands(sabot):

    #Practicing soft hands requires the player has to have an Ace in his hand 

    handsplayed = 0
    correcthands = 0

    #so as we are practicing soft hands we can have all the cards in the 
    while True:

        print(correcthands,"/",handsplayed, 'Hands')
        lengthsabot = len(sabot)

        # In blackjack the dealer has 2 cards, a card facing upwards and a card facing down, for basic strategy
        # the only thing we need to know is the dealer card thats facing upwards and it is called the dealer up card

        dealerupcard = sabot.pop(random.randint(0,lengthsabot))
        pcard1 = "A"  #as said before the player ALWAYS has to have an ace 
        pcard2 = sabot.pop(random.randint(0,lengthsabot))

        dealerupcard1 = [dealerupcard]
        playerhand = [pcard1,pcard2]

        #here we display in the terminal the dealerupcard and the 2 cards the player has
        print("Dealer upcard: ", dealerupcard)
        print("Your Hand:",', '.join(map(str, playerhand)))

        # I blackjack you can do several things like hitting(ask for another card), double(its like a hit but you can only
        # hit once), stand, you can also split the cards when both of them are the same number and finally you can surrender
        print("What are you going to do?")
        print("1.- Hit")
        print("2.- Double")
        print("3.- Stand")
        print("4.- Split")
        print("5.- Surrender")
        print("6.- leave")
    
        #here to change the values of the figure cards, we dont need the for cycle
        # because we know that the first index is the ace card and we only need to chang    e the second index
        # 
        if playerhand[1] == "J":
            playerhand[1] = 10

        elif playerhand[1] == "Q":
            playerhand[1] = 10 

        elif playerhand[1] == "K":
            playerhand[1] = 10

        if dealerupcard == "J":
            dealerupcard = 10

        if dealerupcard == "Q":
            dealerupcard = 10

        if dealerupcard == "K":
            dealerupcard = 10

        if pcard2 == 10:

            print("BlackJack!!")
            handsplayed += 1
            correcthands += 1
            continue

        elif pcard2 == "J":

            print("BlackJack!!")
            handsplayed += 1
            correcthands += 1
            continue

        elif pcard2 == "Q":

            print("BlackJack!!")
            handsplayed += 1
            correcthands += 1
            continue

        elif pcard2 == "K":

            print("BlackJack!!")
            handsplayed += 1
            correcthands += 1
            continue

        choiceinp = input("")
        choice = int(choiceinp)   

        #after doing all of this all that is left to do, is to make all the decisions

        if choice == 6:

            print("Have a nice day, come back later")
            break

        if pcard2 == "A":

            if choice == 1:

                print("correct")
                handsplayed += 1
                correcthands += 1

            else:

                print("wrong")
                handsplayed += 1

        elif pcard2 == 9:

            if choice == 3:

                print("correct")
                handsplayed += 1
                correcthands += 1

            else:

                print("wrong")
                handsplayed += 1

        elif pcard2 == 8:

            if choice == 3:

                print("correct")
                handsplayed += 1
                correcthands += 1

            else:

                print("wrong")
                handsplayed += 1

        elif pcard2 == 7:

            if choice == 1:

                if dealerupcard == "A":

                    print("correct")
                    handsplayed += 1
                    correcthands += 1

                elif dealerupcard >= 9 and dealerupcard <= 10:

                    print("correct")
                    handsplayed += 1
                    correcthands += 1

                else:

                    print("wrong")
                    handsplayed += 1

            elif choice == 3:

                if dealerupcard >= 2 and dealerupcard <= 8:

                    print("correct")
                    handsplayed += 1
                    correcthands += 1

                else:

                    print("wrong")
                    handsplayed += 1

            else:

                print("wrong")
                handsplayed += 1

        elif pcard2 == 6:

            if choice == 1:

                if dealerupcard == "A":

                    print("correct")
                    handsplayed += 1
                    correcthands += 1

                elif dealerupcard == 2:

                    print("correct")
                    handsplayed += 1
                    correcthands += 1

                elif dealerupcard >= 7 and dealerupcard <= 10:

                    print("correct")
                    handsplayed += 1
                    correcthands += 1

                else:

                    print("wrong")
                    handsplayed += 1

            elif choice == 2:

                if dealerupcard >= 3 and dealerupcard <= 6:

                    print("correct")
                    handsplayed += 1
                    correcthands += 1

                else:

                    print("wrong")
                    handsplayed += 1
            else:

                print("wrong")
                handsplayed += 1

        elif pcard2 == 5:

            if choice == 1:

                if dealerupcard == "A":

                    print("correct")
                    handsplayed += 1
                    correcthands += 1

                elif dealerupcard >= 2 and dealerupcard <= 3:

                    print("correct")
                    handsplayed += 1
                    correcthands += 1

                elif dealerupcard >= 7 and dealerupcard <= 10:

                    print("correct")
                    handsplayed += 1
                    correcthands += 1

                else:

                    print("wrong")
                    handsplayed += 1

            elif choice == 2:

                if dealerupcard >= 4 and dealerupcard <= 6:

                    print("correct")
                    handsplayed += 1
                    correcthands += 1

                else:

                    print("wrong")
                    handsplayed += 1

            else:

                print("wrong")
                handsplayed += 1

        elif pcard2 == 4:

            if choice == 1:

                if dealerupcard == "A":

                    print("correct")
                    handsplayed += 1
                    correcthands += 1

                elif dealerupcard >= 2 and dealerupcard <= 3:

                    print("correct")
                    handsplayed += 1
                    correcthands += 1

                elif dealerupcard >= 7 and dealerupcard <= 10:

                    print("correct")
                    handsplayed += 1
                    correcthands += 1

                else:

                    print("wrong")
                    handsplayed += 1

            elif choice == 2:

                if dealerupcard >= 4 and dealerupcard <= 6:

                    print("correct")
                    handsplayed += 1
                    correcthands += 1

                else:

                    print("wrong")
                    handsplayed += 1
            else:

                print("wrong")
                handsplayed += 1\
                
        elif pcard2 == 3:

            if choice == 1:

                if dealerupcard == "A":

                    print("correct")
                    handsplayed += 1
                    correcthands += 1

                elif dealerupcard >= 2 and dealerupcard <= 4:

                    print("correct")
                    handsplayed += 1
                    correcthands += 1

                elif dealerupcard >= 7 and dealerupcard <= 10:

                    print("correct")
                    handsplayed += 1
                    correcthands += 1

                else:

                    print("wrong")
                    handsplayed += 1

            elif choice == 2:

                if dealerupcard == 5:

                    print("correct")
                    handsplayed += 1
                    correcthands += 1

                if dealerupcard == 6:

                    print("correct")
                    handsplayed += 1
                    correcthands += 1

            else:

                print("wrong")
                handsplayed += 1

        elif pcard2 == 2:

            if choice == 1:

                if dealerupcard == "A":

                    print("correct")
                    handsplayed += 1
                    correcthands += 1

                elif dealerupcard >= 2 and dealerupcard <= 4:

                    print("correct")
                    handsplayed += 1
                    correcthands += 1

                elif dealerupcard >= 7 and dealerupcard <= 10:

                    print("correct")
                    handsplayed += 1
                    correcthands += 1

                else:

                    print("wrong")
                    handsplayed += 1

            elif choice == 2:

                if dealerupcard == 5:

                    print("correct")
                    handsplayed += 1
                    correcthands += 1

                elif dealerupcard == 6:

                    print("correct")
                    handsplayed += 1
                    correcthands += 1

                else:

                    print("wrong")
                    handsplayed += 1  

            else:

                print("wrong")
                handsplayed += 1

            sabot.append(dealerupcard)
            sabot.append(pcard2)





PracticeHardHand(sabot)
PracticeSoftHands(sabot)
    






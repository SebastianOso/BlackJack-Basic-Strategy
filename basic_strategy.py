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

for i in range(0,5):
    sabot.extend(deck)
    
random.shuffle(sabot)

def PracticeHardHand(sabot):
    #to practice hard hands we have to erase from the list all the aces from the sabot
    handsplayed = 0
    correcthands = 0

    while True:

        print(correcthands,"/",handsplayed, 'Hands')
        for i in sabot:  #Here we remove the aces with a for
            if i == "A":
                sabot.remove(i)
        for i in sabot:  #the process its done 2 times because in the first 'for cycle' for a unknown reason  
                         #there were still aces left in the sabot
            if i == "A":
                sabot.remove(i)
        #Here we get the length of the sabot to use it later to pick a random card from the sabot    

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

        # I blackjack you can do several things like hitting(ask for another card), double(its like a hit but you can only
        # ht once), stand, you can also split the cards when both of them are the same number and finally you can surrender

        print("What are you going to do?")
        print("1.- Hit")
        print("2.- Double")
        print("3.- Stand")
        print("4.- Split")
        print("5.- Surrender")
        print("6.- leave")
        if playerhand[0] == "J":
            playerhand[0] = 10
        if playerhand[1] == "J":
            playerhand[1] = 10
        if playerhand[0] == "Q":
            playerhand[0] = 10
        if playerhand[1] == "Q":
            playerhand[1] = 10
        if playerhand[0] == "K":
            playerhand[0] = 10
        if playerhand[1] == "K":
            playerhand[1] = 10
        if dealerupcard == "J":
            dealerupcard = 10
        if dealerupcard == "J":
            dealerupcard = 10
        if dealerupcard == "Q":
            dealerupcard = 10
        if dealerupcard == "Q":
            dealerupcard = 10
        if dealerupcard == "K":
            dealerupcard = 10
        if dealerupcard == "K":
            dealerupcard = 10
        playerhandTotal = playerhand[0] + playerhand[1]
        print(playerhandTotal)
        choiceinp = input("")

        choice = int(choiceinp)
        # Aterthis to make all the decisions it is based on the blackjack basic strategy chart
        # mde y BlackJack Apprenticeship, link to the charts: https://www.blackjackapprenticeship.com/blackjack-strategy-charts/
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





PracticeHardHand(sabot)
    






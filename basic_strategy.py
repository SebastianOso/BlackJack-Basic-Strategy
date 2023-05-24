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



def PracticeHardTotals(sabot):
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

        index_dupcard = random.randint(0,lengthsabot)
        dealerupcard = sabot.pop(index_dupcard)
    
        index_pcard1 = random.randint(0,lengthsabot-1)
        pcard1 = sabot.pop(index_pcard1)
    

        index_pcard2 = random.randint(0,lengthsabot-2)
        pcard2 = sabot.pop(index_pcard2)



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
        print(playerhandTotal)
        print(len(sabot))

        match playerhandTotal:

            case 21:

                correcthands = correcthands + 1
                handsplayed = handsplayed + 1
                print("You win")
                continue

        while True:
            try:
                choice = int(input("Select an option --> "))
                break  # Break out of the loop if the input is a valid integer
            except ValueError:
                print("Invalid input. You have to pick a number from 1 to 6.")
                continue


# After this to make all the decisions it is based on the blackjack basic strategy chart
# made y BlackJack Apprenticeship, link to the charts: https://www.blackjackapprenticeship.com/blackjack-strategy-charts/

        if choice == 6:
            print("Have a nice day, come back later")
            break


        #if the player has a correct answer, the correct hand variable is added a 1
        #and also the hands played will be added 1, so if the player loses only the 
        # hands played will be added 1 


        match playerhandTotal:

            case 1|2|3|4|5|6|7|8:

                match choice:

                    case 1:

                        correcthands = correcthands + 1
                        handsplayed = handsplayed + 1
                        print("correct")

                    case _:

                        handsplayed = handsplayed + 1
                        print("wrong")

            case 9:

                match choice:

                    case 1:

                        match dealerupcard:

                            case 2|7|8|9|10:

                                correcthands = correcthands + 1
                                handsplayed = handsplayed + 1
                                print("correct")

                            case _:

                                handsplayed = handsplayed + 1
                                print("wrong")

                    case 2:

                        match dealerupcard:

                            case 3|4|5|6:

                                correcthands = correcthands + 1
                                handsplayed = handsplayed + 1
                                print("correct")

                            case _:

                                handsplayed = handsplayed + 1
                                print("wrong")

                    case _:

                        handsplayed = handsplayed + 1
                        print("wrong")
            
            case 10:

                match choice:

                    case 1:

                        match dealerupcard:

                            case 10:

                                correcthands = correcthands + 1
                                handsplayed = handsplayed + 1
                                print("correct")

                            case _:

                                handsplayed = handsplayed + 1
                                print("wrong")

                    case 2:

                        match dealerupcard:

                            case 2|3|4|5|6|7|8|9:

                                correcthands = correcthands + 1
                                handsplayed = handsplayed + 1
                                print("correct")

                            case _:

                                handsplayed = handsplayed + 1
                                print("wrong")

                    case _:

                        handsplayed = handsplayed + 1
                        print("wrong")
                        
            case 11:

                match choice:

                    case 2:

                        correcthands = correcthands + 1
                        handsplayed = handsplayed + 1
                        print("correct")

                    case _:

                        handsplayed = handsplayed + 1
                        print("wrong")

            case 12:

                match choice:

                    case 1:

                        match dealerupcard:

                            case 2|3|7|8|9|10:

                                correcthands = correcthands + 1
                                handsplayed = handsplayed + 1
                                print("correct")

                            case _:
                                handsplayed = handsplayed + 1
                                print("wrong")
                    
                    case 3:

                        match dealerupcard:

                            case 4|5|6:

                                correcthands = correcthands + 1
                                handsplayed = handsplayed + 1
                                print("correct")

                            case _:

                                handsplayed = handsplayed + 1
                                print("wrong")

                    case _:

                        handsplayed = handsplayed + 1
                        print("wrong")

            case 13|14|15|16:

                print()

                match choice:

                    case 1:

                        match dealerupcard:

                            case 7|8|9|10:

                                correcthands = correcthands + 1
                                handsplayed = handsplayed + 1
                                print("correct")

                            case _:

                                handsplayed = handsplayed + 1
                                print("wrong")

                    case 3:

                        match dealerupcard:

                            case 2|3|4|5|6:

                                correcthands = correcthands + 1
                                handsplayed = handsplayed + 1
                                print("correct")

                            case _:

                                handsplayed = handsplayed + 1
                                print("wrong")
                    
                    case _:

                                handsplayed = handsplayed + 1
                                print("wrong")

            case 17|18|19|20:

                match choice:

                    case 3:

                        correcthands = correcthands + 1
                        handsplayed = handsplayed + 1
                        print("correct")

                    case _:

                        handsplayed = handsplayed + 1
                        print("wrong")

            case 21:

                correcthands = correcthands + 1
                handsplayed = handsplayed + 1
                print("You win")

        
        sabot.append(dealerupcard)
        sabot.append(pcard1)
        sabot.append(pcard2)


def PracticeSoftTotals(sabot):

    #Practicing soft hands requires the player has to have an Ace in his hand 

    handsplayed = 0
    correcthands = 0

    #so as we are practicing soft hands we can have all the cards in the 
    while True:

        print(correcthands,"/",handsplayed, 'Hands')
        lengthsabot = len(sabot)

        # In blackjack the dealer has 2 cards, a card facing upwards and a card facing down, for basic strategy
        # the only thing we need to know is the dealer card thats facing upwards and it is called the dealer up card

        index_dupcard = random.randint(0,lengthsabot-3)
        dealerupcard = sabot.pop(index_dupcard)
    
        index_pcard1 = random.randint(0,lengthsabot-3)
        pcard1 = sabot.pop(index_pcard1)
    
        pcard2 = 'A'


        dealerhand = [dealerupcard]
        playerhand = [pcard1, pcard2]


        if "A" in playerhand:

            indexA = playerhand.index('A')

            if indexA == 1:
                playerhandA = playerhand[::-1]
                pcard1 = playerhandA[0]
                pcard2 = playerhandA[1]

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
        if pcard2 == "J":
            pcard2 = 10

        if pcard2 == "Q":
         pcard2 = 10

        if pcard2 == "K":
            pcard2 = 10

        if dealerupcard == "J":
            dealerupcard = 10

        if dealerupcard == "Q":
            dealerupcard = 10

        if dealerupcard == "K":
            dealerupcard = 10

        if dealerupcard == "A":
            dealerupcard = 11

        if pcard2 == 10:
            correcthands = correcthands + 1
            handsplayed = handsplayed + 1
            print("You win")
            continue

        while True:
            try:
                choice = int(input("Select an option --> "))
                break  # Break out of the loop if the input is a valid integer
            except ValueError:
                print("Invalid input. You have to pick a number from 1 to 6.")
                continue
        #after doing all of this all that is left to do, is to make all the decisions

        if choice == 6:

            print("Have a nice day, come back later")
            break
        
        if playerhand[0] == 'A' and playerhand[0] == 'A':

            if choice == 1:

                correcthands = correcthands + 1
                handsplayed = handsplayed + 1
                print("correct")
                sabot.append(dealerupcard)
                sabot.append(pcard1)
                sabot.append(pcard2)
                continue
                

            else:

                handsplayed = handsplayed + 1
                print("wrong")
                sabot.append(dealerupcard)
                sabot.append(pcard1)
                sabot.append(pcard2)
                continue
                
        match pcard2:

            case 2|3:

                match choice:

                    case 1:

                        match dealerupcard:

                            case 2|3|4|7|8|9|10|11:

                                correcthands = correcthands + 1
                                handsplayed = handsplayed + 1
                                print("correct")

                            case _:

                                handsplayed = handsplayed + 1
                                print("wrong")

                    case 2:

                        match dealerupcard:

                            case 5|6:

                                correcthands = correcthands + 1
                                handsplayed = handsplayed + 1
                                print("correct")

                            case _:

                                handsplayed = handsplayed + 1
                                print("wrong")

                    case _:

                        handsplayed = handsplayed + 1
                        print("wrong")

            case 4:

                match choice:

                    case 1:

                        match dealerupcard:

                            case 2|3|7|8|9|10|11:

                                correcthands = correcthands + 1
                                handsplayed = handsplayed + 1
                                print("correct")

                            case _:

                                handsplayed = handsplayed + 1
                                print("wrong")

                    case 2:

                        match dealerupcard:

                            case 4|5|6:

                                correcthands = correcthands + 1
                                handsplayed = handsplayed + 1
                                print("correct")

                            case _:

                                handsplayed = handsplayed + 1
                                print("wrong")

                    case _:
                        handsplayed = handsplayed + 1
                        print("wrong")

            case 5:

                match choice:

                    case 1:

                        match dealerupcard:

                            case 2|3|7|8|9|10|11:

                                correcthands = correcthands + 1
                                handsplayed = handsplayed + 1
                                print("correct")

                            case _:

                                handsplayed = handsplayed + 1
                                print("wrong")

                    case 2:

                        match dealerupcard:

                            case 4|5|6:

                                correcthands = correcthands + 1
                                handsplayed = handsplayed + 1
                                print("correct")

                            case _:

                                handsplayed = handsplayed + 1
                                print("wrong")

                    case _:

                        handsplayed = handsplayed + 1
                        print("wrong")

            case 6:

                match choice:

                    case 1:

                        match dealerupcard:

                            case 2|7|8|9|10|11:

                                correcthands = correcthands + 1
                                handsplayed = handsplayed + 1
                                print("correct")

                            case _:

                                handsplayed = handsplayed + 1
                                print("wrong")

                    case 2:

                        match dealerupcard:

                            case 3|4|5|6:

                                correcthands = correcthands + 1
                                handsplayed = handsplayed + 1
                                print("correct")

                            case _:

                                handsplayed = handsplayed + 1
                                print("wrong")

                    case _:

                        handsplayed = handsplayed + 1
                        print("wrong")

            case 7:

                match choice:

                    case 1:

                        match dealerupcard:

                            case 9|10|11:

                                correcthands = correcthands + 1
                                handsplayed = handsplayed + 1
                                print("correct")

                            case _:

                                handsplayed = handsplayed + 1
                                print("wrong")

                    case 3:

                        match dealerupcard:

                            case 2|3|4|5|6|7|8:

                                correcthands = correcthands + 1
                                handsplayed = handsplayed + 1
                                print("correct")

                            case _:

                                handsplayed = handsplayed + 1
                                print("wrong")

                    case _:

                        handsplayed = handsplayed + 1
                        print("wrong")

            case 8:

                match choice:

                    case 3:

                        correcthands = correcthands + 1
                        handsplayed = handsplayed + 1
                        print("correct")

                    case _:

                        handsplayed = handsplayed + 1
                        print("wrong")

            case 9:

                match choice:

                    case 3:

                        correcthands = correcthands + 1
                        handsplayed = handsplayed + 1
                        print("correct")

                    case _:

                        handsplayed = handsplayed + 1
                        print("wrong")
            
            case _:

                handsplayed = handsplayed + 1
                print("wrong")

            
        sabot.append(dealerupcard)
        sabot.append(pcard1)
        sabot.append(pcard2)


def BasicStrategy(sabot):

    handsplayed = 0
    correcthands = 0
    print()



def printMenu():

    print("Hello and welcome to the Basic Strategy trainer, we have different options for you to learn Basic Strategy \nand become a really good BlackJack player.")
    print("We know it is complicated to learn all the basic strategy, so we divided it into three parts/modes:")
    print("1.- The first mode in which you only practice hard totals, so there is no aces involved")
    print("2.- The second mode you practice soft totals, in consequence there is no figure cards or 10's in the sabot")
    print("3.- For the third mode is a normal basic strategy practice, basically you practice both hard and soft totals in the same mode.")
    print("We suggest you to first practice the hard and soft totals to then hop onto our third mode :^) (COMING SOON) \n")

    print("Select an option: ")
    print("1.- Practice Hard Totals")
    print("2.- Practice Soft Totals")
    print("3.- Practice overall BasicStrategy")
    print("4.- Quit game")

    while True:
        try:
            option = int(input("Your choice --> "))
            break  # Break out of the loop if the input is a valid integer
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue
    

option = printMenu()


while option != 4 :

    if option == 1 :
        PracticeHardTotals(sabot)
        
    elif option == 2 :
        PracticeSoftTotals(sabot)

    elif option == 3 :
        PracticeBasicStrategy(sabot)

    else :
        print("Invalid input")
    
    opcion = printMenu()




#ayu dark bordered
#electron highlighter


    






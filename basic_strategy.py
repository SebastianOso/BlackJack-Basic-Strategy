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
#poner las lists comprehensions aqui

sabotoriginal = []

for i in range(0,3):
    sabotoriginal.extend(deck)



random.shuffle(sabotoriginal)

def ShuffleSabot(sabotshu):
    random.shuffle(sabotshu)
    return sabotshu

def GetCards(sabotgc):

    lengthsabot = len(sabotgc)

    index_dupcard = random.randint(0,lengthsabot)
    dealerupcardfunc = sabotgc.pop(index_dupcard)
    
    index_pcard1 = random.randint(0,lengthsabot-1)
    pcard1 = sabotgc.pop(index_pcard1)
    
    index_pcard2 = random.randint(0,lengthsabot-2)
    pcard2 = sabotgc.pop(index_pcard2)

    return dealerupcardfunc, pcard1, pcard2

def ReturnCards(sabotrc,dealercard,pcard1r,pcard2r):

    sabotrc.append(dealercard)
    sabotrc.append(pcard1r)
    sabotrc.append(pcard2r)
    
    return "The cards are back in the sabot"


#The next two functions made the decisions based on the BlackJack Apprenticeship: basic strategy table,
#link to the charts: https://www.blackjackapprenticeship.com/blackjack-strategy-charts/


def checkhardtotalwin(playerhandtotalch, dealerupcardch, choicech):

    match playerhandtotalch:
        
        case 1|2|3|4|5|6|7|8:

            match choicech:

                case 1:
                    print("Correct")
                    return True


                case _:
                    print("Correct play was hit")
                    return False

        case 9:

            match choicech:

                case 1:

                    match dealerupcardch:

                        case 2|7|8|9|10:

                            print("correct")
                            return True

                        case _:

                            print("Correct play was double")
                            return False

                case 2:

                    match dealerupcardch:

                        case 3|4|5|6:

                            print("correct")
                            return True

                        case _:

                            print("Correct play was hit")
                            return False

                case _:

                    match dealerupcardch:

                        case 2|7|8|9|10:
                            print("The correct play was hit")
                            return False

                        case 3|4|5|6:
                            print("The correct play was double")
                            return False

        case 10:

            match choicech:

                case 1:

                    match dealerupcardch:

                        case 10:

                            print("correct")
                            return True

                        case _:

                            print("The correct play was double")
                            return False

                case 2:

                    match dealerupcardch:

                        case 2|3|4|5|6|7|8|9:

                            print("correct")
                            return True

                        case _:

                            print("The correct play was hit")
                            return False

                case _:

                    match dealerupcardch:

                        case 10:

                            print("The correct play was hit")
                            return False

                        
                        case 2|3|4|5|6|7|8|9:
                            
                            print("The correct play was double")
                            return False

        case 11:

            match choicech:

                case 2:

                    print("Correct")
                    return True

                case _:

                    print("The correct play was double ")
                    return False

        case 12:

            match choicech:

                case 1:

                    match dealerupcardch:

                        case 2|3|7|8|9|10:

                            print("correct")
                            return True

                        case _:
                            
                            print("The correct play was stand")
                            return False
                    
                case 3:

                    match dealerupcardch:

                        case 4|5|6:

                            print("correct")
                            return True

                        case _:

                            print("The correct play was hit")

                case _:

                    match dealerupcardch:

                        case 2|3|7|8|9|10:

                            print("The correct play was hit")
                            return False

                        
                        case 4|5|6:
                            
                            print("The correct play was stand")
                            return False

        case 13|14|15|16:

            match choicech:

                case 1:

                    match dealerupcardch:

                        case 7|8|9|10:

                            print("correct")
                            return True

                        case _:

                            print("The correct play was stand")
                            return False


                case 3:

                    match dealerupcardch:

                        case 2|3|4|5|6:

                            print("correct")
                            return True

                        case _:

                            print("The correct play was hit")
                            return False
                    

                case _:

                    match dealerupcardch:

                        case 7|8|9|10:

                            print("The correct play was hit")
                            return False

                        
                        case 2|3|4|5|6:
                            
                            print("The correct play was stand")
                            return False

        case 17|18|19|20:

            match choicech:

                case 3:

                    print("correct")
                    return True

                case _:

                    print("The correct play was stand")
                    return False

        case 21:

            print("BlackJack!")
            return True


#this is the other function based in the basic strategy chart

def checksofttotalwin(playercardst, dealerupcardst, choicest):

    match playercardst:

            case 2|3:

                match choicest:

                    case 1:

                        match dealerupcardst:

                            case 2|3|4|7|8|9|10|11:

                                print("correct")
                                return True

                            case _:

                                print("The correct play was hit")
                                return False

                    case 2:

                        match dealerupcardst:

                            case 5|6:

                                print("correct")
                                return True

                            case _:

                                print("The correct play was double")

                    case _:

                        match dealerupcardst:
                            
                            case 2|3|4|7|8|9|10|11:

                                print("The correct play was hit")
                                return False

                            case 5|6:

                                print("The correct play was double")
                                return False

            case 4|5:

                match choicest:

                    case 1:

                        match dealerupcardst:

                            case 2|3|7|8|9|10|11:

                                print("correct")
                                return True

                            case _:

                                print("The correct play was hit")
                                return False

                    case 2:

                        match dealerupcardst:

                            case 4|5|6:

                                print("correct")
                                return True

                            case _:

                                print("The correct play was double")
                                return False

                    case _:

                        match dealerupcardst:

                            case 2|3|7|8|9|10|11:

                                print("The correct play was hit")
                                return False

                            case 4|5|6:

                                print("The correct play was double")
                                return False

            case 6:

                match choicest:

                    case 1:

                        match dealerupcardst:

                            case 2|7|8|9|10|11:

                                print("correct")
                                return True

                            case _:

                                print("The correct play was hit")
                                return False

                    case 2:

                        match dealerupcardst:

                            case 3|4|5|6:

                                print("correct")
                                return True

                            case _:

                                print("The correct play was double")
                                return False

                    case _:

                        match dealerupcardst:

                            case 2|7|8|9|10|11:

                                print("The correct play was hit")
                                return False

                            case 3|4|5|6:

                                print("The correct play was double")
                                return False

            case 7:

                match choicest:

                    case 1:

                        match dealerupcardst:

                            case 9|10|11:

                                print("correct")
                                return True

                            case _:

                                print("The correct play was hit")
                                return False

                    case 3:

                        match dealerupcardst:

                            case 2|3|4|5|6|7|8:

                                print("correct")
                                return True

                            case _:

                                print("The correct play was stand")
                                return False

                    case _:

                        match dealerupcardst:

                            case 2|3|4|5|6|7|8:

                                print("The correct play was stand")
                                return False
                            
                            case 9|10|11:

                                print("The correct play was hit")
                                return False

            case 8|9:

                match choicest:

                    case 3:

                        print("correct")
                        return True

                    case _:

                        print("The correct play was stand")
                        return False
            




def PracticeHardTotals(sabotht):
    #to practice hard hands we have to erase from the list all the aces from the sabot
    handsplayed = 0
    correcthands = 0

    
    for i in sabotht:  #Here we remove the aces with a for
        if i == "A":
            sabotht.remove(i)
    for i in sabotht:  #the process its done 2 times because in the first 'for cycle' for a unknown reason  
                     #there were still aces left in the sabot
        if i == "A":
            sabotht.remove(i)
        #Here we get the length of the sabot to use it later to pick a random card from the sabot
    
    while True:

        ShuffleSabot(sabotht)

        print(correcthands,"/",handsplayed, 'Hands')
        
        # In blackjack the dealer has 2 cards, a card facing upwards and a card facing down, for basic strategy
        # the only thing we need to know is the dealer card thats facing upwards and it is called the dealer upcard
        
        dealerupcard1, playercard1, playercard2 = GetCards(sabotht)

        dealerupcardht =  dealerupcard1
        playerhandht = [playercard1, playercard2]

        #here we display in the terminal the dealerupcard and the 2 cards the player has
        print("Dealer upcard: ", dealerupcardht)
        print("Your Hand:",', '.join(map(str, playerhandht)))

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


        for index in range(len(playerhandht)):

            if playerhandht[index] == "J":
                playerhandht[index] = 10
            
        
            elif playerhandht[index] == "Q":
                playerhandht[index] = 10 
        
            elif playerhandht[index] == "K":
                playerhandht[index] = 10


        if dealerupcardht == "J":
            dealerupcardht = 10

        elif dealerupcardht == "Q":
            dealerupcardht = 10

        elif dealerupcardht == "K":
            dealerupcardht = 10


        playerhandTotal = playerhandht[0] + playerhandht[1]
        print(playerhandTotal)
        print(len(sabotht))

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


        if choice == 6:
            print("Have a nice day, come back later")
            break
    

        #if the player has a correct answer, the correct hand variable is added a 1
        #and also the hands played will be added 1, so if the player loses only the 
        # hands played will be added 1 


        checkhtwin = checkhardtotalwin(playerhandTotal, dealerupcard, choice)

        if checkhtwin:

            correcthands = correcthands + 1
            handsplayed = handsplayed + 1

        else:

            handsplayed = handsplayed + 1
        
        #at the end of the hand, the card that were used back in the sabot
        ReturnCards(sabotht, dealerupcard1, playercard1, playercard2)



def PracticeSoftTotals(sabotst):

    #Practicing soft hands requires the player has to have an Ace in his hand 

    handsplayed = 0
    correcthands = 0

    #so as we are practicing soft hands we can have all the cards in the 
    while True:

        ShuffleSabot(sabotst)

        print(correcthands,"/",handsplayed, 'Hands')
        lengthsabot = len(sabotst)

        # In blackjack the dealer has 2 cards, a card facing upwards and a card facing down, for basic strategy
        # the only thing we need to know is the dealer card thats facing upwards and it is called the dealer up card

        dealerupcardstf, playercardst1f, playercardst2f = GetCards(sabotst)

        playercardst1 = playercardst1f

        playercardst1 = 'A'

        dealerupcardst =  dealerupcardstf
        playerhandst = [playercardst1, playercardst2f]
    

        #here we display in the terminal the dealerupcard and the 2 cards the player has
        print("Dealer upcard: ", dealerupcardst)
        print("Your Hand:",', '.join(map(str, playerhandst)))

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
        # because we know that the first index is the ace card and we only need to change the second index
        # 
        if playerhandst[1] == "J":
            playerhandst[1] = 10

        elif playerhandst[1] == "Q":
            playerhandst[1] = 10

        elif playerhandst[1] == "K":
            playerhandst[1] = 10


        if dealerupcardst == "J":
            dealerupcardst = 10

        elif dealerupcardst == "Q":
            dealerupcardst = 10

        elif dealerupcardst == "K":
            dealerupcardst = 10

        elif dealerupcardst == "A":
            dealerupcardst = 11


        if playerhandst[1] == 10:
            correcthands = correcthands + 1
            handsplayed = handsplayed + 1
            print("You win")
            continue

        while True:
            try:
                choicestotal = int(input("Select an option --> "))
                break  # Break out of the loop if the input is a valid integer
            except ValueError:
                print("Invalid input. You have to pick a number from 1 to 6.")
                continue
        #after doing all of this all that is left to do, is to make all the decisions

        if choicestotal == 6:

            print("Have a nice day, come back later")
            break
        
        checkstwin = checksofttotalwin(playerhandst[1], dealerupcardst, choicestotal)

        if checkstwin:

            correcthands = correcthands + 1
            handsplayed = handsplayed + 1

        else:

            handsplayed = handsplayed + 1 


        ReturnCards(sabotst, dealerupcardstf, playercardst1f, playercardst2f)


def PracticeBasicStrategy(sabotbs):

    handsplayed = 0
    correcthands = 0
    

    while True:

        ShuffleSabot(sabotbs)

        print(correcthands,"/",handsplayed, 'Hands')

        dealerupcardbs1f, playercardbs1f, playercardbs2f = GetCards(sabotbs)

        dealerupcardbs =  dealerupcardbs1f
        playerhandbs = [playercardbs1f, playercardbs2f]

        #here we display in the terminal the dealerupcard and the 2 cards the player has
        print("Dealer upcard: ", dealerupcardbs)
        print("Your Hand:",', '.join(map(str, playerhandbs)))


        for index in range(len(playerhandbs)):

            if playerhandbs[index] == "J":
                playerhandbs[index] = 10
            
            elif playerhandbs[index] == "Q":
                playerhandbs[index] = 10 
        
            elif playerhandbs[index] == "K":
                playerhandbs[index] = 10

            elif playerhandbs[index] == "A":
                playerhandbs[index] = 11
        

        if dealerupcardbs == "J":
            dealerupcardbs = 10

        elif dealerupcardbs == "Q":
            dealerupcardbs = 10

        elif dealerupcardbs == "K":
            dealerupcardbs = 10

        elif dealerupcardbs == "A":
            dealerupcardbs = 11

        print("What are you going to do?")
        print("2.- Double")
        print("3.- Stand")
        print("4.- Split")
        print("5.- Surrender")
        print("6.- leave")
        print("1.- Hit")
    
        if 11 in playerhandbs:

            aceindex = playerhandbs.index(11)

            if aceindex == 1:

                playerhandbs = [playercardbs2f, playercardbs1f]

            if playerhandbs[1] == 10:
                correcthands = correcthands + 1
                handsplayed = handsplayed + 1
                print("You win")
                continue

            while True:
                try:
                    choicebstotal = int(input("Select an option --> "))
                    break  # Break out of the loop if the input is a valid integer
                except ValueError:
                    print("Invalid input. You have to pick a number from 1 to 6.")
                    continue
            #after doing all of this all that is left to do, is to make all the decisions

            if choicebstotal == 6:

                print("Have a nice day, come back later")
                break
            
            checkstwin = checksofttotalwin(playerhandbs[1], dealerupcardbs, choicebstotal)

            if checkstwin:

                correcthands = correcthands + 1
                handsplayed = handsplayed + 1

            else:

                handsplayed = handsplayed + 1 


            ReturnCards(sabotbs, dealerupcardbs1f, playercardbs1f, playercardbs2f)


        else:

            playerhandTotalbs = playerhandbs[0] + playerhandbs[1]
            print(playerhandTotalbs)
            print(len(sabotbs))

            match playerhandTotalbs:

                case 21:

                    correcthands = correcthands + 1
                    handsplayed = handsplayed + 1
                    print("You win")
                    continue

            while True:
                try:
                    choicebs = int(input("Select an option --> "))
                    break  # Break out of the loop if the input is a valid integer
                except ValueError:
                    print("Invalid input. You have to pick a number from 1 to 6.")
                    continue


            if choicebs == 6:
                print("Have a nice day, come back later")
                break

            checkhtwin = checkhardtotalwin(playerhandTotalbs, dealerupcardbs, choicebs)

            if checkhtwin:

                correcthands = correcthands + 1
                handsplayed = handsplayed + 1

            else:

                handsplayed = handsplayed + 1

            ReturnCards(sabotbs, dealerupcardbs1f, playercardbs1f, playercardbs2f)


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
            optionmenu = int(input("Your choice --> "))
            break  # Break out of the loop if the input is a valid integer
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

    return optionmenu

optionmenu = printMenu()

while optionmenu != 4 :

    if optionmenu == 1 :
        PracticeHardTotals(sabotoriginal)
        
    elif optionmenu == 2 :
        PracticeSoftTotals(sabotoriginal)

    elif optionmenu == 3 :
        PracticeBasicStrategy(sabotoriginal)
    
    optionmenu = printMenu()


    
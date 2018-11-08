import random

ROLLNUM = 2

def dice():
    loop = "y"

    #setOfDice = createDice()
    #printDiceSideBySide(setOfDice)
    times = 0
    while loop== "y":
        diceList = [0]*ROLLNUM
        #for i in range(ROLLNUM):
        (roll, roll2) = randnum()
        print(roll, roll2)
        input()
        diceList = createDice(roll, roll2)

        printDiceSideBySide(diceList)
            #printDiceSideBySide(diceSet)
        times += 1

        print ('you rolled a ' + str(roll) + " and a " +str(roll2))
        loop = input('would you like to play again (y/n)')
        print('you have played ' + str(times) + " times")



def randnum():
    x = random.randint(1,5)
    y = random.randint(1,5)
    return(x,y)

def createDice(roll, roll2):
   topBot = ' ------- '
   blank1  = '|       |'
   blankL  = '| *     |'
   blankR  = '|     * |'
   blankM  = '|   *   |'
   blank2  = '|  * *  |'
   one = [topBot, blank1, blankM, blank1, topBot]
   two = [topBot, blank1, blank2, blank1, topBot]
   three = [topBot, blankL, blankM, blankR, topBot]
   four = [topBot, blank2, blank1, blank2, topBot]
   five = [topBot, blank2, blankM, blank2, topBot]
   six = [topBot, blank2, blank2, blank2, topBot]

   if roll == 1:
       roll = one

   elif roll == 2:
       roll = two

   elif roll == 3:
       roll = three

   elif roll == 4:
       roll = four

   elif roll == 5:
       roll = five

   elif roll == 6:
       roll = six

   if roll2 == 1:
       roll2 = one

   elif roll2 == 2:
       roll2 = two

   elif roll2 == 3:
       roll2 = three

   elif roll2 == 4:
       roll2 = four

   elif roll2 == 5:
       roll2 = five

   elif roll2 == 6:
       roll2 = six

   else:
       print('error')

   Dice1 = roll
   Dice2 = roll2



   allDice = [Dice1, Dice2]


   return allDice

def printDiceSideBySide(allDice):
     for row in range(0,len(allDice[0])):
         for col in range(0,len(allDice)):
             print(allDice[col][row], end = '\t')
         print()


dice()

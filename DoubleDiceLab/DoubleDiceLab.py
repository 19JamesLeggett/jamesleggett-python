from random import *
def dice():
    loop = "y"
    list = ['|       |', '|   *   |', '|  * *  |']
    times = 0
    while loop== "y":
        times = times + 1
        y = randnum()
        print(whichDice(y,list))
        print ('you rolled a ' + str(y))
        loop = input('would you like to play again (y/n)')
        print('you have played ' + str(times) + " times")

def randnum():
    x = randint(1,6)
    return(x)

def whichDice(randnum , list):
    a = "---------"
    e = "---------"

    if randnum == 1 or randnum == 2:
        b = list[0]
    elif randnum == 3:
        b = list[1]
    elif randnum == 4 or randnum == 5 or randnum == 6:
        b = list[2]

    if randnum == 1 or randnum == 3 or randnum == 5:
        c = list[1]
    elif randnum == 4:
        c = list[0]
    elif randnum == 2 or randnum == 6:
        c = list[2]

    if randnum == 1 or randnum == 2:
        d = list[0]
    elif randnum == 3:
        d = list[1]
    elif randnum == 4 or randnum == 5 or randnum == 6:
        d = list[2]




    return(a + "\n" + b + "\n" + c + "\n" + d + "\n" + e)

dice()

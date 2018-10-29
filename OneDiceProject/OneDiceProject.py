from random import *

def main ():
    loop = 'Y'
    times=0
    while loop =='Y' :
        times = times + 1
        Y = randNum ()
        print(whichDice(Y))
        print("You rolled a - " + str(Y))
        loop = input ("Would you like this to run again? (Y/N) - ")
        print ("You have played " + str(times) + " times.")

def randNum () :
    x = randint(1,6)
    return (x)

def whichDice (randnum) :
    a = ' -------'

    if randnum==1 or randnum==2 :
        b = '|      |'
    elif randnum==3 :
        b = '|   *  |'
    elif randnum==4 or randnum==5 or randnum==6 :
        b = "| *  * |"

    if randnum==1 or randnum==3 or randnum==5 :
        c = '|   *  |'
    elif randnum==4 :
        c = '|      |'
    elif randnum==2 or randnum==6 :
        c = '| *  * |'

    if randnum==1 or randnum==2 :
        d = '|      |'
    elif randnum==3 :
        d = '|   *  |'
    elif randnum==4 or randnum==5 or randnum==6 :
        d = c = '| *  * |'

    e = ' -------'


    return(a + "\n" + b + "\n" + c + "\n" + d + "\n" +e)
        
main()

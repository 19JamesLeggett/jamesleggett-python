def myfunc() :
    print("Bellarmine")
    print("Python")




def grade() :
    x=input("What Grade are you in -")
    y=int(x)-1
    print(str(y))



def city(x,y):
   print(x)
   print(y)

from random import *

def randomNumber():
    x = input("what is my start value? - ")
    y = input("what is my end value? - ")
    myNumber = randint(int(x), int(y))
    print(myNumber)


def areaBox(num1,num2):
    num3 = int(num1) * int(num2)
    return(num3)

def boxPerimeter(num1,num2):
  num3= int(num1)*2+ int(num2)*2
  return(num3)

myfunc()

grade()

myCity=input("What city are you from -")
myGrade=input("What Grade are you in -")


city(myCity, myGrade)


randomNumber()


oneNumber= input("enter length")
twoNumber= input("enter width")
areaNum= areaBox(oneNumber, twoNumber)
print("the answer is " + str(areaNum))

perimeterNum= boxPerimeter(oneNumber, twoNumber)
print("the answer is" + str(perimeterNum))

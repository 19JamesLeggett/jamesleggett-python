def main():
    myString = str(input("Enter any string - "))
    print ("Your string is -" + myString)

    print ("Your string without vowels is -" + deVowel(myString))





def deVowel(myString):
    myString2 = myString
    myStringV = ""
    for x in myString2:
        if (x!= "a" and x!= "e" and x!= "i" and x!= "o" and x!= "u" and x!= "A" and x!= "E" and x!= "U" and x!= "I" and x!= "O") :
            myStringV = myStringV + x

    return (myStringV)

main()

def main2():
    list = [1,2,3,4]
    m=2
    print(mathstuff(list, m))

def mathstuff(list, m):
    listf = []
    for x in list:
        listf.append(float(x) * float(m))
    return(listf)
main2()

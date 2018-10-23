#def main():
    #listOfLists= [['tooth paste', 'q-tips', 'milk'],['milk', 'candy', 'apples'],['paper', 'pencils', 'q-tips']]

    #shoppingList=listOfLists
    #print(shoppingList)


#def allInOne(listOfLists):
   # listOfLists =[['tooth paste', 'q-tips', 'milk'],['milk', 'candy', 'apples'],['paper', 'pencils', 'q-tips']]
   # finalList = []
    #for num in listOfLists:
      #  if num not in finalList:
        #    finalList.append(num)
      #  return listOfLists



#def countQTips(listOfLists):
    #print('countQTips')

#main()

def main():

    Item1a = input("Group 1 item 1 - ")
    Item2a = input("Group 1 item 2 - ")
    Item3a = input("Group 1 item 3 - ")
    Item1b = input("Group 2 item 1 - ")
    Item2b = input("Group 2 item 2 - ")
    Item3b = input("Group 2 item 3 - ")
    Item1c = input("Group 3 item 1 - ")
    Item2c = input("Group 3 item 2 - ")
    Item3c = input("Group 3 item 3 - ")
    AllinOne = [[Item1a, Item2a, Item3a], [Item1b, Item2b, Item3b], [Item3a, Item3b, Item3c]]


    ShoppingCart =AllinOne

    print ("oldCart - "+ str(ShoppingCart))
    print()
    print("newCart - "+ combineLists(ShoppingCart))
    print()
    print("the number of q-tips is -" + countTips(ShoppingCart))

def combineLists (origCart) :
    newCart = []
    for group in origCart :
        for item in group:
            if item not in newCart :
                newCart = newCart + [item]
    return (str(newCart))

def countTips (cart) :
    numtips = int(0)
    for group in cart :
        for item in group :
            if item=='q-tips' :
                numtips = numtips + 1
            elif item == 'Q-tips' :
                numtips = numtips + 1
            elif item == "Qtips" :
                numtips = numtips + 1
            elif item == "qtips" :
                numtips = numtips + 1
    return (str(numtips))

main()

#def AllinOne ():
   # Item1a = input("Group 1 item 1 - ")
   # Item2a = input("Group 1 item 2 - ")
   # Item3a = input("Group 1 item 3 - ")
   # Item1b = input("Group 2 item 1 - ")
    #Item2b = input("Group 2 item 2 - ")
   # Item3b = input("Group 2 item 3 - ")
   # Item1c = input("Group 3 item 1 - ")
   # Item2c = input("Group 3 item 2 - ")
   # Item3c = input("Group 3 item 3 - ")
  #  AllinOne = [[Item1a, Item2a, Item3a], [Item1b, Item2b, Item3b], [Item3a, Item3b, Item3c]]
   # return(AllinOne)


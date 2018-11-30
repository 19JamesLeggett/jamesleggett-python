textCodes = {"JimBo" : "jimmy" , "lol" : "laugh", "gg" : "good game"}
def main () :
    textCodes = {"Jimbo" : "Jimmy" , "lol" : "laugh" , "gg" : "good game"}
    d = 'y'
    while d=='y' :
        f = input("Would you like to use dictionary or modify dictionary or view dictionary or clear console (u/m/v/c) - ")
        if f=='u' :
            textCodes = norm(textCodes)
        elif f=='m' :
            textCodes = mod(textCodes)
        elif f=='c' :
            textCodes('\n'*50)
        else :
            textCodes = view(textCodes)
def norm (textCodes) :
    x='y'
    while x=='y' :
        d = input('Put in code - ')
        if d in textCodes :
            print(textCodes[d])
        else :
            print("This isnt in the dictionary currently")
            n = input("Would you like to add it to the dictionary? (y/n) - ")
            if n=='y' :
                c = input("What does that stand for - ")
                textCodes[d] = c

        x = input('Would you like to read another abreviation (y/n) - ')
        print()
    return(textCodes)

def mod (textCodes) :
    x = 'y'
    while x=='y' :
        f = input("Would you like to remove or edit an entrey (r/e) - ")
        if f=='r' :
            l = input("What abreviation would you like to remove? - ")
            del textCodes[l]
        elif f=='e' :
            g = input("What abreviation would you like to edit? - ")
            q = input("What does that abreviation actually stand for? - ")
            del textCodes[g]
            textCodes[g] = q
        else :
            print("This isn't valid, please input an r or e for remove and edit!")
        x = input("Would you like to remove another item(y/n) - ")
        print()
    return(textCodes)

def view(textCodes) :
    for x in textCodes :
        print(x + ' : ' + textCodes[x] + '      ', end='')
    print()
    print()
    return (textCodes)


main()




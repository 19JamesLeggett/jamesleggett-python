class petClass():
    def __init__(self,vName, vBreed):
        self.name = vName
        self.breed = vBreed

    def getName(self):
        return(self.name)
    def getBreed(self):
        return(self.breed)
    def whatIsIt(self):
        print("My Pet's name is " + Pet1.name + " The breed is a " + Pet1.breed)

Pet1 = petClass('George', 'Boxer')

Pet1.whatIsIt()

class dog(petClass):
    def __init__(self, vName, vBreed, vBaseball):
        petClass.__init__(self, vName, vBreed)
        self.baseball = vBaseball

    def getBaseball(self):
        return(self.baseball)
    def whatIsIt2(self):
        print("My Pet's name is " + Pet2.name + " The breed is a " + Pet2.breed + " He plays " + Pet2.baseball)

Pet2 = dog('George', 'Boxer', 'baseball')

Pet2.whatIsIt2()

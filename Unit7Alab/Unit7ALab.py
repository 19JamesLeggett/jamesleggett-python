class petClass():
    petType = 'cage free pet'

    def __init__(self, vType, vName, vBreed):
        self.type = vType
        self.name = vName
        self.breed = vBreed

    def getType(self):
        return(str(self.type))
    def getName(self):
        return(str(self.name))
    def getBreed(self):
        return(str(self.breed))
    def whatIsIt(self):
        print('My Pet is a ' + Pet1.type + " Their name is " + Pet1.name + " The breed is a " + Pet1.breed)
    def whatIsIt2(self):
        print('My Pet is a ' + Pet2.type + " Their name is " + Pet2.name + " The breed is a " + Pet2.breed)

Pet1 = petClass('Dog', 'George', 'Boxer')

Pet1.whatIsIt()

Pet2 = petClass('Cat', 'Fred', 'Birman')

Pet2.whatIsIt2()

class petCage:
    def __init__(self, vType, vDanger, vBreed):
        self.type = vType
        self.danger = vDanger
        self.breed = vBreed
    def getType(self):
        return(self.type)
    def getDanger(self):
        return(self.danger)
    def getBreed (self) :
        return(self.breed)
    def whatdanger(self):
        if self.danger == 'True':
            return('dangerous')
        elif self.danger == 'False':
            return ('not dangerous')
    def whatIsIt3(self):
        print('My Pet is a ' + Pet3.type + "They are " + Pet3.whatdanger() + " The breed is a " + Pet3.breed)
        print('My Pet is a ' + Pet4.type + "They are " + Pet4.whatdanger() + " The breed is a " + Pet4.breed)

Pet3 = petCage('Snake', 'True', 'King Cobra')
Pet4 = petCage('Rat', 'False', 'King Cobra')


Pet3.whatIsIt3()


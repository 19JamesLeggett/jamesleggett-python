def main():
    print('Bellarmine student current grade point average')
    myClass=(input("What grade are you in? - "))

    resultAnswer=yearInSchool(myClass)
#sends the the information from yearInSchool up to main and down from main
    print('congrats you are a - '+ resultAnswer)

    listofGrades=[100.0, 90.5, 90.4, 98.3]
    num=len(listofGrades)
    answerGpa=getGpafunction(listofGrades,num)

#gives a list and sends it down to Gpa function

    print('my Gpa is ' + str(answerGpa))


    letterGradeanswer=LetterGrade(answerGpa)
#sends information down to letterGrade and back
    print(("your current Letter Grade is a ") + str(letterGradeanswer))

    if (letterGradeanswer) == "A":
        print("Congrats you are passing")

    elif (letterGradeanswer) == "B":
        print("Congrats you are passing")

    elif (letterGradeanswer) == "C":
        print("Congrats you are passing")

    elif (letterGradeanswer) == "D":
        print("Congrats you are passing")

    elif (letterGradeanswer) == "F":
        print("Better get to work, you are falling")

    else:
        print('you have no grade')

#prints if you are passing
def yearInSchool(Class):
    if (Class) == '12':
        classResult="Senoir!"

    elif (Class) == '11':
        classResult="Junior"

    elif (Class) == '10':
        classResult="Sophomore"

    elif (Class) == '9':
        classResult="Freshman!"

    else:
        classResult="Your not in school."

    return classResult
#returns what class you are
#yearInSchool(enteredclass)

def getGpafunction(myGrades,myNum):


    totalamount=myGrades[0]+myGrades[1]+myGrades[2]+myGrades[3]
    gradeAverage=(totalamount/myNum)

    return gradeAverage
    
#gives you the average grades


def LetterGrade(Grade):
    if (Grade) > 90:
        averageGrade= 'A'

    elif (Grade) > 80:
        averageGrade= "B"

    elif (Grade) > 70:
        averageGrade= "C"

    elif (Grade) >60:
        averageGrade= "D"

    else:
        averageGrade= "F"


    return averageGrade

#gives you a letter number
#calcAverageGrade(givenGrade)


main()

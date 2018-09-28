def main():
    print('Bellarmine student current grade point average')
    myClass=(input("What grade are you in? - "))

    resultAnswer=yearInSchool(myClass)
#sends the the information from yearInSchool up to main and down from main
    print('congrats you are a - '+ resultAnswer)

    listofGrades=[100.0, 70.5, 95.4, 85.9]
    num=len(listofGrades)
    answerGpa=getGpafunction(listofGrades,num)

#gives a list and sends it down to Gpa function

    print('my Gpa is ' + str(answerGpa))


    letterGradeanswer=LetterGrade(answerGpa)
#sends information down to letterGrade and back
    print(letterGradeanswer)

    if (letterGradeanswer) == "A" or "B" or "C" or "D":
        print('passing')
    else:
        print('falling')
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

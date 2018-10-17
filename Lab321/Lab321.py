def main():
    print('Bellarmine student current grade point average')
    myClass=(input("What grade are you in? - "))

    resultAnswer=yearInSchool(myClass)
#sends the the information from yearInSchool up to main and down from main
    print('congrats you are a - '+ resultAnswer)


    num1 = input('how many grades -')
    grades=[]
    for x in range(0,int(num1)):
        myGrades= input('grade')
        grades.append(myGrades)
    print (grades)



    #myLists=[100,98, 48, 56]
    #print(len(myLists))
    #myLists=getGpafunction()
    #num=len(grades)

    answerGpa=getGpafunction(grades)

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

def getGpafunction(myGrades):
     #gpa=sum(myGrades) / float(myNum)
    total=0
    for x in myGrades:
         total+=float(x)
    gradeAverage = ((total) / len(myGrades))

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

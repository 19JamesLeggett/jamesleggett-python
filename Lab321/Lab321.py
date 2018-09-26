def main():
    print('Bellarmine student current grade point average')
    myClass=(input("What grade are you in? - "))

    resultAnswer=yearInSchool(myClass)

    print('congrats you are a - '+ resultAnswer)

    listofGrades=[86.5, 94.2, 100.0, 96.8]
    (len(listofGrades))
    answerGpa=getGpafunction(listofGrades)


    resultGrade=calcAverageGrade(Grade)

    print("grade - "+ resultGrade)


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

#yearInSchool(enteredclass)

def getGpafunction(listofGrades):
    totalamount=(86.5+94.2+100.0+96.8)
    gradeAverage=(totalamount/4)

    



def LetterGrade(Grade):
    if (Grade) < 90:
        averageGrade= 'A, Great Job!'

    elif (Grade) < 80:
        averageGrade= "B, Good Work!"

    elif (Grade) < 70:
        averageGrade= "C, Ok!"

    else:
        averageGrade="Study more!"

    return averageGrade


#calcAverageGrade(givenGrade)


main()

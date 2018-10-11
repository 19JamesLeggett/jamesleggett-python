def main():
    draw7()
    starsAndStripes()
def draw7():
    string = ""
    for i in range(0,7):
        string = ""
        for i in range(0,7):
            string += "*"
        print (string)

def starsAndStripes():
    for i in range(0,3):
        for a in range(0,7):
            print("*", end = "")





main()

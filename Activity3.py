
def getGrade(num):
    if num >= 920:
        Grade = "A"
    elif num >= 880:
        Grade = "B+"
    elif num >= 820:
        Grade = "B"
    elif num >= 780:
        Grade = "C+"
    elif num >= 700:
        Grade = "C"
    elif num >= 600:
        Grade = "D"
    else:
        Grade = "F"

    return Grade

print ("ISQA 4900 Letter Grade Calculator")

isGood = False
while not isGood:
    num = input ("Enter total number of points earned: " )
    num = int(num)

    letterGrade = getGrade(num)
    print ("Letter grade: " + letterGrade)
    print(" ")
    yn = input("Continue (y/n)?: ")
    if yn == "y":
        isGood = False
    else:
        isGood = True
print ("Bye")
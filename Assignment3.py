# This is the IF/ELSE Statement rewritten
#if parmValue > 5 and parmValue <=10: 
   # print("parmValue is greater then 5 and less then 11")
#else: 
   # print("parmValue is not greater than 5 and less than 11")
    
    
# This is the function that uses IF/ELSE statements to display your grade
def displayGrade (FMyGPA):
    if FMyGPA >= 3.5:
        print("You received an A")

    elif FMyGPA < 3.5 and FMyGPA >= 3.0:
        print("You received a B")
    
    elif FMyGPA < 3.0 and FMyGPA >=2.0:
        print("You received a C")

    else:
        print("Retake the course")
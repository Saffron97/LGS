# Version 1: Manually input each grade
def list_grades ():
    while True:
        grade = input("What is your grade? ")
        if grade == "done" : break 
        try:
            grade = float(grade)
            if grade >= 8.5:
              print("\n", "Let's post this one on LinkedIn: ", grade,"\n")
        except:
            print ("\n", "Numerical values only! Please try again.", "\n")
    print ("That's all for now, then! See you next time.")
list_grades()

# Version 2: Input all grades at once WITHIN the program (!= input)
# grades = [7.0, 9.9, "tbd", 5.9, 10.0, 7.2, "pass"]

# def list_grades ():
#     for grade in grades:
#         try:
#             grade = float(grade)
#             if grade >= 8.5:
#                 print("\n", "Let's post this one on LinkedIn: ", grade,"\n")
#         except:
#             print ("\n", "Numerical values only! Please try again.", "\n")

# list_grades()
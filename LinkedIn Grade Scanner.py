# Version 1: Manually input each grade
# def list_grades ():
#     while True:
#         grade = input("What is your grade? ")
#         if grade == "done" : break 
#         try:
#             grade = float(grade)
#             if grade >= 8.5:
#               print("\n", "Let's post this one on LinkedIn: ", grade,"\n")
#         except:
#             print ("\n", "Numerical values only! Please try again.", "\n")
#     print ("That's all for now, then! See you next time.")
# list_grades()

# Version 2: Input all grades at once WITHIN the program (!= input)
# dictionary = {"subject":grade}
grades = {
    "Project": 7.0,
    "Accounting and Finance": 9.9,
    "Operations and Supply Chain": 8.8, 
    "Organisations and People": 8.4, 
    "Effective Communication Skills": 10.0, 
    "Additional Language": 7.2, 
    "Personal and Professional Development": "pass"
}

def list_grades ():
    for grade_key in grades:
        try:
            grade_value = float(grades[grade_key])
            if grade_value >= 8.5:
                print("\n", "Let's post this one on LinkedIn: ", grade_key, grade_value, "\n")
        except:
            print ("\n", "Numerical values only! Please try again.", "\n")

list_grades()
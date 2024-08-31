# Write a program that takes a student's score (0-100) 
# and prints their grade based on the following criteria:
# 90-100: "A"
# 80-89: "B"
# 70-79: "C"
# 60-69: "D"
# Below 60: "F"

def GradeCalc(score):
    if(score>=90 and score<=100):
        print("Grade A")
    elif (score>=80 and score<=89):
        print("Grade B") 
    elif (score>=70 and score<=79):
        print("Grade C")
    elif (score>=60 and score<=69):
        print("Grade D")
    elif (score<60):
        print("Need to Improvement :: Fail ")

print(GradeCalc(int(input())))
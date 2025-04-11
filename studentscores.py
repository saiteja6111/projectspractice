#writing a students scores program

student_scores = {}
n = int(input('Enter total no of students in the class: '))
your_total_marks = 100
for i in range(n):
    name = input("Enter Student full name : ")
    marks = int(input(f"Enter students marks out of {your_total_marks} : "))
    student_scores[name] = marks


students_grades = {}
for i in student_scores:
    if student_scores[i] >= 90:
        students_grades[i] = "Grade A"
    elif 90 > student_scores[i]>= 80:
        students_grades[i] = "Grade B"
    elif 80 > student_scores[i] >= 70:
        students_grades[i] = "Grade C"
    elif 70 > student_scores[i] >= 60:
        students_grades[i] = "Grade D"
    elif 60 > student_scores[i] >=50:
        students_grades[i] = "Grade E"
    elif 50 > student_scores[i]:
        students_grades[i] = "Fail"

for i in students_grades.items():
    print(i)
students = {
    "Ali": 85, 
    "Sara": 92, 
    "Ahmed": 76, 
    "Hina": 58, 
    "Bilal": 64
    }
for student_Name, marks in students.items():
    if marks >= 90:
        grade = "A"
    elif marks >= 80:
        grade = "B"
    elif marks >= 70:
        grade = "C"
    elif marks >= 60:
        grade = "D"
    else:
        grade = "F"
    print(f"{student_Name}  and received  grade {grade}.")
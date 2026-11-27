students = [
{"name": "Ali",   "marks": [80, 75, 90]},
{"name": "Sara",  "marks": [95, 88, 92]},
{"name": "Ahmed", "marks": [55, 62, 48]},
]

for student in students:
    name = student["name"]
    marks = student["marks"]
    average = sum(marks) / len(marks)

    if average >= 60:
        print(f"{name} has passed the exam with an average of {average:.2f}.")
        if average >= 90:
            print(f"{name} has topper of the class.")
    else:
        print(f"{name} has failed the exam with an average of {average:.2f}.")
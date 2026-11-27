marks = [78, 45, 92, 33, 67, 88]
passed = 0

for i in marks:
    if i >= 40:
        print(f"You have passed the exam with marks: {i}.")
    else:
        print(f"You have failed the exam with marks: {i}.")

passed_students = sum(1 for i in marks if i >= 40)
print(f"Number of students who passed: {passed_students}")
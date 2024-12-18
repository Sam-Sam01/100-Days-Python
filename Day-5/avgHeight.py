student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

totalHeight = 0
for height in student_heights:
    totalHeight += height

number_of_students = 0
for student in student_heights:
    number_of_students += 1

averageHeight = totalHeight / number_of_students
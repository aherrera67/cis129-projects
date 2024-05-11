with open('grades.txt', 'w') as file:
    while True:
        grade = input("enter a grade (or 'e' to exit): ")
        if grade.lower() == 'e':
            break
        file.write(grade + '\n')

# ------------------------------------------------------------- 

with open('grades.txt', 'r') as file:
    grades = file.readlines()

grades = [int(grade.strip()) for grade in grades]
total = sum(grades)
count = len(grades)
average = total / count

print("individual grades:", grades)
print("total:", total)
print("count:", count)
print("average:", average)

# --------------------------------------------------------------

import csv 

with open('grades.cvs', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    while True:
        first_name = input("enter student's first name (or 'e' to exit):")
        if first_name.lower() == 'e':
            break
        last_name = input("enter student's last name:")
        exam1 = int(input("enter exam 1 grade:"))
        exam2 = int(input("enter exam 2 grade:"))
        exam3 = int(input("enter exam 3 grade:"))

        writer.writerow([first_name, last_name, exam1, exam2, exam3])

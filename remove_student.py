import os
import csv

students_file = "students.csv"

students = []
with open(students_file, "r") as f:
    reader = csv.reader(f)
    students = list(reader)

student_name = input("Enter student name to remove: ")

found = False
updated_students = [students[0]]

for row in students[1:]:
    if row[0] == student_name:
        found = True
        # Delete the student's image
        image_path = f"faces/{student_name}.jpg"
        if os.path.exists(image_path):
            os.remove(image_path)
            print(f"🗑️ Deleted image: {image_path}")
    else:
        updated_students.append(row)

if found:
    with open(students_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(updated_students)
    print(f"✅ {student_name} removed successfully!")
else:
    print(f"❌ Student '{student_name}' not found.")

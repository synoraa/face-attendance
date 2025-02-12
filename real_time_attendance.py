import cv2
import face_recognition
import numpy as np
import os
import csv
from datetime import datetime

students_file = "students.csv"
attendance_file = "attendance.csv"

if not os.path.exists(attendance_file):
    with open(attendance_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "time"])

known_face_encodings = []
known_face_names = []

with open(students_file, "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        name, encoding_str = row
        encoding = np.array([float(x) for x in encoding_str.split(",")])
        known_face_encodings.append(encoding)
        known_face_names.append(name)

marked_students = set()

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        if True in matches:
            matched_index = matches.index(True)
            name = known_face_names[matched_index]

            if name not in marked_students:
                # Mark Attendance in CSV
                with open(attendance_file, "a", newline="") as f:
                    writer = csv.writer(f)
                    writer.writerow([name, datetime.now().strftime("%Y-%m-%d %H:%M:%S")])

                print(f"✅ Marked attendance for {name}")
                marked_students.add(name)  # Add to marked list
            else:
                print(f"⚠️ {name} already marked present!")

        # Display Results
        top, right, bottom, left = face_location
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

    cv2.imshow("Face Recognition Attendance", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

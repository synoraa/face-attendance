import cv2
import face_recognition
import numpy as np
import os
import csv

# Create required folders/files
if not os.path.exists("faces"):
    os.makedirs("faces")

csv_file = "students.csv"

# Ensure CSV exists with headers
if not os.path.exists(csv_file):
    with open(csv_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "encoding"])  # Column headers

# Ask for Student Name
student_name = input("Enter Student Name: ")

# Capture Image from Webcam
cap = cv2.VideoCapture(0)
print("Press 's' to capture an image.")

while True:
    ret, frame = cap.read()
    cv2.imshow("Capture Face", frame)

    key = cv2.waitKey(1)
    if key == ord('s'):  # Press 's' to save
        image_path = f"faces/{student_name}.jpg"
        cv2.imwrite(image_path, frame)
        break

cap.release()
cv2.destroyAllWindows()

# Load and Encode Face
img = face_recognition.load_image_file(image_path)
face_encodings = face_recognition.face_encodings(img)

if face_encodings:
    encoding_str = ",".join(map(str, face_encodings[0]))  # Convert encoding to string
    
    # Append to CSV
    with open(csv_file, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([student_name, encoding_str])

    print(f"✅ {student_name} registered successfully and stored in 'faces/'!")

else:
    print("❌ No face detected. Try again.")

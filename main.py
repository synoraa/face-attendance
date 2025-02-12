import os

def register_student():
    os.system("python3 face_registration.py")

def mark_attendance():
    os.system("python3 real_time_attendance.py")

def remove_student():
    os.system("python3 remove_student.py")

while True:
    print("FACE RECOGNITION ATTENDANCE SYSTEM")
    print("1️ Register a Student")
    print("2️ Mark Attendance")
    print("3️ Remove a Student")
    print("4️ Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        register_student()
    elif choice == "2":
        mark_attendance()
    elif choice == "3":
        remove_student()
    elif choice == "4":
        print("👋 Exiting... Have a great day!")
        break
    else:
        print("❌ Invalid choice! Please enter a valid option.")

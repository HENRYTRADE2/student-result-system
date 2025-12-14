import json
import os

FILE_NAME = "students_data.json"

# Load data from file
def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}

# Save data to file1
def save_data():
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

students = load_data()

def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")

    if student_id in students:
        print("❌ Student already exists!")
    else:
        students[student_id] = {
            "name": name,
            "courses": {}
        }
        save_data()
        print("✅ Student added successfully.")

def add_course():
    student_id = input("Enter Student ID: ")

    if student_id not in students:
        print("❌ Student not found!")
        return

    course = input("Enter Course Name: ")

    if course in students[student_id]["courses"]:
        print("❌ Course already exists for this student.")
        return

    score = input("Enter Score (0 - 100): ")

    if not score.isdigit():
        print("❌ Score must be a number.")
        return

    score = int(score)

    if score < 0 or score > 100:
        print("❌ Invalid score range.")
        return

    students[student_id]["courses"][course] = score
    save_data()
    print("✅ Course added successfully.")

def calculate_gpa(courses):
    total_points = 0

    for score in courses.values():
        if score >= 70:
            total_points += 5
        elif score >= 60:
            total_points += 4
        elif score >= 50:
            total_points += 3
        elif score >= 45:
            total_points += 2
        elif score >= 40:
            total_points += 1

    if len(courses) == 0:
        return 0.0

    return round(total_points / len(courses), 2)

def view_result():
    student_id = input("Enter Student ID: ")

    if student_id not in students:
        print("❌ Student not found!")
        return

    student = students[student_id]
    courses = student["courses"]

    print("\n===== STUDENT RESULT =====")
    print(f"Name: {student['name']}")
    print(f"ID: {student_id}")

    if not courses:
        print("No courses recorded.")
        return

    print("\nCourses & Scores:")
    for course, score in courses.items():
        print(f"{course}: {score}")

    print(f"\n🎓 GPA: {calculate_gpa(courses)}")

def menu():
    while True:
        print("\n===== STUDENT RESULT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. Add Course & Score")
        print("3. View Student Result")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            add_course()
        elif choice == "3":
            view_result()
        elif choice == "4":
            print("👋 Exiting system...")
            break
        else:
            print("❌ Invalid option.")

menu()

# Student Result Manager CLI
import json

DATA_FILE = "students.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_data():
    with open(DATA_FILE, "w") as file:
        json.dump(students, file, indent=4)

students = load_data()

def add_student():
    student_id = input("Enter student ID: ").strip()
    name = input("Enter student name: ").strip()
    if not student_id or not name:
        print("ID and name cannot be empty!")
        return
    
    if student_id in students:
        print("Student ID already exists!")
    else:
        students[student_id] = {
            "name": name,
            "grades": {}
        }
        print(f"Student {name} added successfully!")
        save_data()

def add_grade():
    student_id = input("Enter student ID: ").strip()
    
    if student_id not in students:
        print("Student not found!")
        return
    
    subject = input("Enter subject: ").strip()
    while True:
        grade_input = input("Enter grade (0-100): ")
        try:
            grade = int(grade_input)
            if 0 <= grade <= 100:
                break
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Please enter a number.")    
    students[student_id]["grades"][subject] = grade
    print(f"Grade added for {students[student_id]['name']}")
    save_data()

def view_student():
    student_id = input("Enter student ID: ").strip()
    
    if student_id not in students:
        print("Student not found!")
        return
    
    student = students[student_id]
    print(f"\nName: {student['name']}")
    print("Grades:")
    
    if not student["grades"]:
        print("  No grades recorded.")
    else:
        for subject, grade in student["grades"].items():
            print(f"  {subject}: {grade}")

def view_all_students():
    if not students:
        print("No students added yet.")
    else:
        for student_id, info in students.items():
            print(f"{student_id} - {info['name']}")

def main():
    while True:
        print("\n--- Student Result Manager ---")
        print("1. Add student")
        print("2. Add grade")
        print("3. View student")
        print("4. View all students")
        print("5. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            add_grade()
        elif choice == "3":
            view_student()
        elif choice == "4":
            view_all_students()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

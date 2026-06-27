student_data = []
def update_student_data():
    sid = input("Enter Student's ID: ")
    found = False

    for student in student_data:
        if student["id"] == sid:
            print(f"\n Student found: {student['name']}")

            name = input("Enter new name (press Enter to keep current): ")
            age = input("Enter new age (press Enter to keep current): ")
            grade = input("Enter new grade (press Enter to keep current): ")
            d_o_b = input(
                "Enter new DOB (YYYY-MM-DD) (press Enter to keep current): ")
            subs = input(
                "Enter new subjects (comma-separated) (press Enter to keep current): ")

            if name:
                student["name"] = name
            if age:
                student["age"] = int(age)
            if grade:
                student["grade"] = grade
            if d_o_b:
                student["dob"] = d_o_b
            if subs:
                student["subjects"] = [sub.strip()
                                       for sub in subs.split(",")]

            print("Student updated successfully!")
            found = True
            break

    if not found:
        print("Student not found.")
while True:

    print("Welcome to the student Data Organizer!")
    print("Select an Option:")
    print("1. Add student")
    print("2. Display all students")
    print("3. Update student Information")
    print("4. Delete Student")
    print("5. Display subjects offered")
    print("6. Exit")

    choice = input("Enter your choice:")
    print("")
    print("")

    if choice == "1":
        print("Enter student details:")
        std_id = input("Enter student id: ")
        std_name = input("Enter student name: ")
        std_age = input("Enter student age: ")
        std_grade = input("Enter student grade:")
        std_birthdate = input("Enter studnet birthdate (YYYY-MM-DD):")
        std_subs = input("ENter student subjects(comma-separated):")
        print(f"Student {std_name} added successfully!")
        student_data.append({"id": std_id, "name": std_name, "age": std_age, "grade": std_grade, "birthdate": std_birthdate, "subjects": std_subs})

        print("")   
        print("")

        print("Select an option:")
        print("1. Add Student")
        print("2. Display all students")
        print(".....")
        print("")
        print("")

        print("--- Display All students ---")
        print("")
        print("")


    elif choice == "2":
        print(student_data )
    elif choice == "3":
        update_student_data()
    
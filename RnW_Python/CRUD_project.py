




all_students = []

while True:
    
    print("Welcome to the Student Data Organizer !")
    
    print("Select an option:")
    print("1. Add student")
    print("2. Display all student")
    print("3. Update student information")
    print("4. Delete student")
    print("5. Display subjects offered")
    print("6. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        
        print("Enter student details:")
        
        std = {
            "id" : int(input("Student ID: ")),
            "name" : input("Name: "),
            "age" : int(input("Age: ")),
            "grade" : input("Grade: "),
            "dob" : input("Date of Birth(YYYY-MM-DD): "),
            "subjects" : input("Subjects(comma-separated): "),
        }
        
        all_students.append(std)
        
        print("Student added successfully !")
        
    elif choice == 2:
        
        for student in all_students:
            print(f"ID : {student["id"]}, Name : {student["name"]}, Age : {student["age"]}, Grade : {student["grade"]}, DOB : {student["dob"]}, Subjects : {student["subjects"]}")
            
    elif choice == 3:
        
        stid = int(input("Enter student id to update: "))
        
        if stid == student["id"]:
            student["name"] = input("Enter student name: ")
            student["age"] = int(input("Enter student age: "))
            student["grade"] = input("Enter student grade: ")
            student["dob"] = input("Enter student's date of birth(YYYY-MM-DD): ")
            student["subjects"] = input("Enter student subjects(comma-separated): ")
            
            print("Student updated successfully !")
        else:
            print("Invalid ID !")
            
    elif choice == 4:
        
        stid = int(input("Enter student id to delete: "))
        
        for student in all_students:
            if stid == student["id"]:
                all_students.remove(student)
                
                print("Student deleted successfully !")
                
            else:
                print("Invalid ID !")
                
    elif choice == 5:
        
        print("Enter 1 to choose Gujarati.")
        print("Enter 2 to choose Hindi.")
        print("Enter 3 to choose English.")
        print("Enter 4 to choose Maths.")
        print("Enter 5 to choose Science.")
        print("Enter 6 to choose Social Science.")
        
        stid = int(input("Enter your choice: "))
        
        if stid == 1:
            print("You choose Gujarati.")
        elif stid == 2:
            print("You choose Hindi.")
        elif stid == 3:
            print("You choose English.")
        elif stid == 4:
            print("You choose Maths.")
        elif stid == 5:
            print("You choose Science.")
        elif stid == 6:
            print("You choose Social Science.")
                
    elif choice == 6:
        
        print("Exiting")
        break
    
    else:
        print("Invalid choice !")

                
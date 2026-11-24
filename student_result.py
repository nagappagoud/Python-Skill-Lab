#Mini Project
# Student Result Management System

students = {}

while True:
    print("\n--- STUDENT RESULT MANAGEMENT ---")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        roll = input("Enter Roll Number: ")

        if roll in students:
            print("Student Already Exists!")
            continue

        name = input("Enter Student Name: ")
        marks = [int(input(f"Subject {i} Marks: ")) for i in range(1, 4)]

        total = sum(marks)
        avg = total / 3

        if avg >= 90:
            grade = "A+"
        elif avg >= 80:
            grade = "A"
        elif avg >= 70:
            grade = "B"
        elif avg >= 60:
            grade = "C"
        elif avg >= 35:
            grade = "D"
        else:
            grade = "F"

        result = "PASS" if all(m >= 35 for m in marks) else "FAIL"

        students[roll] = [name, marks, total, avg, grade, result]
        print("Student Added Successfully!")

    elif choice == "2":
        for roll, d in students.items():
            print("\nRoll Number:", roll)
            print("Name:", d[0])
            print("Marks:", d[1])
            print("Total:", d[2])
            print("Average:", round(d[3], 2))
            print("Grade:", d[4])
            print("Result:", d[5])

    elif choice == "3":
        roll = input("Enter Roll Number: ")
        if roll in students:
            print("Student Details:", students[roll])
        else:
            print("Student Not Found!")

    elif choice == "4":
        roll = input("Enter Roll Number: ")
        if roll in students:
            del students[roll]
            print("Student Deleted Successfully!")
        else:
            print("Student Not Found!")

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")

class Student:
    def __init__(self, roll, name):
        self.roll = roll
        self.name = name

students = []

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        roll = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")

        student = Student(roll, name)
        students.append(student)

        print("Student Added Successfully!")

    elif choice == "2":
        print("\nStudent List")

        if len(students) == 0:
            print("No Students Found")
        else:
            for s in students:
                print("Roll:", s.roll, "| Name:", s.name)

    elif choice == "3":
        roll = input("Enter Roll Number to Search: ")

        found = False

        for s in students:
            if s.roll == roll:
                print("Student Found")
                print("Roll:", s.roll)
                print("Name:", s.name)
                found = True

        if not found:
            print("Student Not Found")

    elif choice == "4":
        roll = input("Enter Roll Number to Delete: ")

        found = False

        for s in students:
            if s.roll == roll:
                students.remove(s)
                print("Student Deleted Successfully!")
                found = True
                break

        if not found:
            print("Student Not Found")

    elif choice == "5":
        print("Thank You!")
        break

    else:
# %%
        print("Invalid Choice")

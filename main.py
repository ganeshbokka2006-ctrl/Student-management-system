def add_student():
    name = input("Enter Student Name: ")
    roll = input("Enter Roll Number: ")
    course = input("Enter Course: ")

    with open("students.txt", "a") as file:
        file.write(f"{name},{roll},{course}\n")

    print("✅ Student Added Successfully!")


def view_students():
    print("\n----- Student Records -----")

    try:
        with open("students.txt", "r") as file:
            data = file.readlines()

            if not data:
                print("No Records Found!")
            else:
                for student in data:
                    print(student.strip())

    except FileNotFoundError:
        print("No Records Found!")


while True:
    print("\n========== STUDENT MANAGEMENT SYSTEM ==========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")